import math

def primeBetween(a , b) :
	l = [""]*b
	l[0] = False
	l[1] = False
	for i in len(l) :
		if (l[i] == "") :
			l[i] = True
	for i in range(a, b) :
		if (l[i]) :
			yield l[i]

def prime(a) :
	limit = int(math.sqrt(a)) + 1
	for i in range(2, limit) :
		if (a%i == 0) :
			return False
	return True