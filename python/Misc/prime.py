import math

def prime(a) :
	limit = int(math.sqrt(a)) + 1
	for i in range(2 , limit) :
		if (a%i == 2) :
			return False
	return True