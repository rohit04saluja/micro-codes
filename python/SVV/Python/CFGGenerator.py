# Import the necessary files
import sys, _ast, ast
from header import dataFromFile, preprocess
from optparse import OptionParser

# List to show statement classes
stmtS = [_ast.Assign, _ast.Delete, _ast.Return, _ast.Print]
stmtC = [ _ast.For, _ast.While, _ast.If]
stmt = stmtS + stmtC

# Function to traverse ast to get nodes and add to cfg
def traverseAST(g, cfg) :
	# Loop over every given node in AST body
	for i in range(len(g)) :
		# Traverse further is node is a defined node
		if(type(g[i]) in stmt) :
			# Traverse further if it is complex node
			if('body' in g[i]._fields) :
				# If node is of type _ast.If
				if(type(g[i]) in stmtC) :
					cfg[g[i].lineno-1][g[i].body[0].lineno-1] = 1
					if(g[i].orelse) :
						cfg[g[i].lineno-1][g[i].orelse[0].lineno-1] = 1
				# Traverse the child nodes
				cfg = traverseAST(map(lambda a: a, ast.iter_child_nodes(g[i])), cfg)
			# Procedure for all nodes except the first and if previous node is a defined stmt type and a simple statement
			if((i > 0) and (type(g[i-1]) in stmt)) :
				cfg[g[i-1].lineno-1][g[i].lineno-1] = 1
	# Return the generated CFG
	return cfg

# Function to create CFG from given source code
def codeToCFG(code) :
	# Obtain the Abstract Syntax Tree of the code
	g = ast.parse(code).body
	n = len(code.split("\n"))
	cfg = [[0 for i in range(n)] for j in range(n)]

	# Traverse the ast
	cfg = traverseAST(g, cfg)
	# Return the obtained CFG
	return cfg

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

	# Apply preprocessors to the code
	code = preprocess(code)

	# Obtain CFG of code
	cfg = codeToCFG(code)
	for i in cfg : print i
