# Import the necessary files
import sys, os, tokenize, io, re
from header import dataFromFile, preprocess
from optparse import OptionParser
from coverage import Coverage
from random import random

# Function to feed input to the code with the given test cases
def feedInput(code, test) :
	# Initial variable declaration
	temp = 0
	i = 0
	limit = len(test)
	# Tokenize the code
	g = tokenize.generate_tokens(io.BytesIO("\n".join(code)).readline)
	result = []
	# Traverse for each token
	for toknum, tokval, _, _, _ in g:
		# True if an input statement wasnt found 3 tokens prior
		if(temp==0) :
			# True is there are test cases to be inputed and token found happens to be input
			if(i<limit and tokval=="input") :
				# replace token with value
				result.append((toknum, test[i]))
				i += 1
				temp = 3
			else :
				result.append((toknum, tokval))
		else :
			# Input was found
			temp -= 1
	# Return the untokenized form of code in form of list
	return tokenize.untokenize(result).split("\n")

# Function to read the line numbers covered by given test case
def stmtCovered(code, test) :
	# Replace input lines with values
	code = feedInput(code, test)
	# Initialize the coverage object
	cov = Coverage()
	# Create a temporary file with the code
	fname = "tmp"+str(int(random()*100000))
	f = open(fname, 'w')
	f.write("\n".join(code))
	f.close()
	# Capture statement coverage
	print("Test case is: "+str(test))
	cov.start()
	out = execfile(fname)
	cov.stop()
	# Obtain the report of coverage and remove the temporary file
	report = cov.analysis(fname)
	os.remove(fname)
	# Return the executed line numbers
	return set(range(1, len(code)+1)) - set(report[2])

# Function to determine the statement coverage of the code with the given test suit
def stmtCoverage(code, test) :
	covered = set()
	# Execute for every test case in the test suit
	print("# Multiple executions of statement with their outputs (Ignore)")
	# Loop over every test case
	for t in test :
		covered |= stmtCovered(code, t)
	# Check of non executable code
	limit = set(range(1, len(code)+1))
	uncovered = limit - covered
	temp = set()
	for i in covered :
		flag = False
		i -= 1
		g = tokenize.generate_tokens(io.BytesIO(code[i]).readline)
		for toknum, tokval, _, _, _ in g :
			# Check if else exists in tokens
			if(tokval == "else" and ((i+2) in uncovered) and ((i) not in covered)):
				flag = True
				break
		if(flag) :
			temp.add(i+1)
	# Update the sets
	covered -= temp
	print("# Executions completed")
	coverage = float((len(covered)+1) * 100)/float(len(code))
	# Return the determined values
	return coverage, covered

# Check if the file is run directly
if(__name__ == '__main__') :
	# Declare options for the parsing with the file
	optparser = OptionParser()
	optparser.add_option('-f', '--inputFile',
			dest='inFile',
			help='filname of the source file',
			default=None)
	optparser.add_option('-t', '--testFile',
			dest='testFile',
			help='filename of the test cases file',
			default=None)

	# Parse the option available with input
	(options, args) = optparser.parse_args()

	# Grab the source code
	code = None
	if(options.inFile is None) :
		code = sys.stdin
	elif(options.inFile is not None) :
		code = dataFromFile(options.inFile)
	else :
		print("No file specified, system will exit")
		sys.exit("System will exit now")

	# Grab the all the test cases
	test = None
	if(options.testFile is None) :
		test = sys.stdin
	elif(options.testFile is not None) :
		test = dataFromFile(options.testFile)
	else :
		print("No test case file specified, system will exit")
		sys.exit("Software will exit now")
	
	# Split the test case string into specific test cases in form of 2D array
	test = test.strip()
	test = test.split("\n")
	for i in range(len(test)) :
		test[i] = test[i].split()

	# Apply preprocessors to the code
	code = preprocess(code)
	code = code.split("\n")

	# Determind the statement coverage
	coverage, covered = stmtCoverage(code, test)
	
	# Report generation
	print("Statement coverage for the given test suit and program is {:.2f}%".format(coverage))
	if(coverage != 100) :
		print("Statements covered are:")
		print(covered)
