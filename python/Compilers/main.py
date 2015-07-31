# importing essential modules
import FSAGraph

# initializing the parameters for FSA
sigma = map(chr, range(65, 91)) + map(chr, range(97,123)) + map(chr, range(48, 58)) + ['_']

# user input of regualr expression
expr = raw_input("Enter the regular expression: ")

# convert postfix notation to NFA using thomspson
g = FSAGraph.Graph(sigma)
g.setRegExpr(expr)
g.createNFAFromRegExpr()
g.printFSA()
