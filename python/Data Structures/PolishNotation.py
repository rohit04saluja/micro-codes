# function to split the input string into operands and operators
def splitNote(s, operand, operator):
	# declaring the output list after splitting
	outList = []
	# traversing all the characters in the string
	for i in range(0, len(s)) :
		# check if character in operand
		if s[i] in operand :
			# traverse for all characters that conform to operand
			j = i
			while j<len(s) and s[j] in operand :
				j += 1
			# update the output list
			outList.append(s[i:j])
			i += j-1
		# check if character is operator
		elif s[i] in operator :
			# update the output list
			outList.append(s[i])
		# check is character is paranthesis
		elif s[i] in ['(', ')'] :
			# update the output list
			outList.append(s[i])
		# invalid character found
		else :
			# display error message
			return ["Invalid Character in string"]

	# return the split list
	return outList


# funciton to convert inffix to postfix
def InfixToPostfix(infix, operand=[], operator={'+':1,'-':1,'/':2,'*':2}):
	# set default value for operand if operand is empty
	if len(operand) == 0 :
		operand += map(chr, range(97, 123)) + map(chr, range(65, 91)) + ["_"] + map(chr, range(48, 58))
	# variable to ouput postfix notation
	postfix = []
	# create stack for convertion
	stack = []
	# remove spaces from the input expression
	infix = infix.replace(' ', '')
	# split the infix string into a list
	infix = splitNote(infix, operand, operator)
	# traverse for all elements in the infix list
	for i in range(0, len(infix)) :
		# left paranthesis found, push on stack
		if infix[i] == '(' :
			stack.append('(')
		# right paranthesis found, pop untill left paranthesis found
		elif infix[i] == ')' :
			while True :
				popEle = stack.pop()
				if popEle == '(' :
					break
				else :
					postfix.append(popEle)
		# operator found, pop till operator of lower precedence found
		elif infix[i] in operator :
			if len(stack) == 0 :
				stack.append(infix[i])
			else :
				prec = operator[infix[i]]
				for j in range(0, len(stack)) :
					temp = stack.pop()
					if operator[temp] > prec :
						postfix.append(temp)
					else :
						stack.append(temp)
						break
				stack.append(infix[i])
		# operand found
		else :
			postfix.append(infix[i])
	# pop everything left in stack
	for i in range(0, len(stack)) :
		postfix.append(stack.pop())

	# return the final postfix list
	return postfix
