def swap(a,b):
	c = a
	a = b
	b = c
	return a,b

def sortBubble(a=[]):
	l = len(a)
	for i in range(0,l-1):
		for j in range(0,l-1):
			if(a[j]>a[j+1]):
				a[j], a[j+1] = swap(a[j], a[j+1])
	return a

def main():
	a=[2,4,1,6,3,5]
	print(a)
	a = sortBubble(a)
	print(a)

main()
