# Necesaary import for analyzing file and finding complexity
from radon.visitors import ComplexityVisitor
# Import for option parsing
import sys
from header import dataFromFile
from optparse import OptionParser

# Declare options for inputting the file
optparser = OptionParser()
optparser.add_option('-f', '--inputFile',
			dest='inFile',
			help='file name of the source file',
			default=None)

# Check if the file is run directly
if(__name__ == '__main__') :
	# Parse the available options
	(options, args) = optparser.parse_args()

	# Grab the source code
	code = None
	if(options.inFile is None) :
		code = sys.stdin
	elif(options.inFile is not None) :
		code = dataFromFile(options.inFile)
	else :
		print("No file specified, system will exit")
		sys.exit("System will exit now!")

	# print the complexity of the program
	print("Cyclomatic complexity of the given source code is "+str(ComplexityVisitor.from_code(code).complexity))
