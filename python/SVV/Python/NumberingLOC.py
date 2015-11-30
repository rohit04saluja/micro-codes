# Import the necessary files
import sys
from header import dataFromFile, preprocess
from optparse import OptionParser

# Function to add a number in each line of code
def numberCode(code) :
	# Apply preprocessers
	code = preprocess(code)

	result = []
	temp = code.split("\n")
	for i in range(len(temp)) :
		result.append(str(i+1)+"\t"+temp[i])
	return "\n".join(result)

# Check if the file is run directly
if(__name__ == '__main__') :
	# Declare options for the parsing with the file
	optparser = OptionParser()
	optparser.add_option('-f', '--inputFile',
			dest='inFile',
			help='filname of the source file',
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
		sys.exit("System will exit")

	# Do processing
	code = numberCode(code)
	# Print the modified code
	print(code)
