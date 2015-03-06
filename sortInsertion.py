def sortInsertion(a=[])
	for i in range(1,len(a)):
		temp = a[i]
		j = i-1
		while j>=0 and a[j]>temp:
			a[j+1] = a[j]
			j = j-1
		a[j+1] = temp
	return a

def main():
	a = [2,1,7,3,68,2,47,4]
	print(a)
	a = sortInsertion(a)
	print(a)
