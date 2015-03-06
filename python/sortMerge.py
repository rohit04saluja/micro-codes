def merge(a, b):
	al = len(a)
	bl = len(b)
	l = al + bl
	c = []
	i=j=0
	for k in range(0,l):
		if(i<al):
			if(j<bl):
				if(a[i]<b[j]):
					c.append(a[i])
					i=i+1
				else:
					c.append(b[j])
					j=j+1
			else:
				c.append(a[i])
				i=i+1
		else:
			c.append(b[j])
			j=j+1
	return c
	

def sortMerge(a=[]):
	l = len(a)
	if(l!=1):
		pl = int(l/2)
		p = []
		q = []
		for i in range(0,pl):
			p.append(a[i])
		for i in range(pl,l):
			q.append(a[i])
		p = sortMerge(p)
		q = sortMerge(q)
		a = merge(p,q)
	return a
		
def main():
	a = [3,6,2,4,1,7]
	print(a)
	a = sortMerge(a)
	print(a)

main()
