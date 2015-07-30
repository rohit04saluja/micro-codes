# define 3 towers
t1 = []
t2 = []
t3 = []

# function to create the stack on the tower
def createTower(n, s):
	# push disc on the source tower
	for i in range(n, 0, -1):
		s.append(i)
	# return the ready tower
	return s

# function to transfer discs from source to destination tower
def transferTower(n, s, h, t):
	# if there exist any disc to shift
	if(n>0):
		# transfer n-1 disc from source to intermediate tower
		transferTower(n-1, s, t, h)
		
		# display stack status
		print (t1, t2, t3)
		
		# transfer the last disc from source to destination tower
		if s:
			t.append(s.pop())
		# transfer n-1 disc from intermediate to destination tower
		transferTower(n-1, h, s, t)
	# return the final towers
	return s, h, t

def main():
	n = int(input("Enter the number of disc on the tower: "))
	createTower(n, t1)
	print (t1, t2, t3)
	transferTower(n, t1, t2, t3)
	print (t1, t2, t3)

main()
