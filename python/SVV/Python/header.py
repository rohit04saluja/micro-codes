# Import the pyparsing package for removing comments
import tokenize, io, re

# Function to collect data from a given file
def dataFromFile(fileName) :
	f = open(fileName, 'r')
	data = f.read()
	f.close()
	return data

# Function to remove comments from given source code
def rmComments(code) :
	# List to store uncommented part of code
	result = []
	# Process each line for tokenizing it
	g = tokenize.generate_tokens(io.BytesIO(bytes(code)).readline)
	for toknum, tokval, _, _, _ in g:
		# Remove corresponding token if it is a # comment
		if toknum != tokenize.COMMENT :
			result.append((toknum, tokval))
	
	# Return the untokenized form of the so opbtained code
	return tokenize.untokenize(result)

# Function to remove empty lines from the code
def pruneCode(code) :
	code = filter(lambda line: re.search("\S", line), code.split("\n"))
	return "\n".join(code)

# Function to compline all necessary preprocessors together
def preprocess(code) :
	code = rmComments(code)
	code = pruneCode(code)
	return code
