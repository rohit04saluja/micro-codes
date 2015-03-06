def swap(a, b):
	c = a
	a = b
	b = c
	return a,b

def sortSelection(a=[]):
	l = len(a)
	for i in range(0,l-1):
		temp = i
		for j in range(i+1,l):
			if(a[temp]>a[j]):
				temp = j
		a[i], a[temp] = swap(a[i], a[temp])
	return a

def main():
	a = [4,2,7,3,6,1,45,4]
	print(a)
	a = sortSelection(a)
	print(a)

main()
