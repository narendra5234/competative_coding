for t in range(int(input())):
	n,k=map(int,input().split())
	l=list(map(int,input().split()))
	c=0
	for i in l:
		if i%2==0:
			c+=1
	if c==k:
		print("YES")
	else:
		print("NO")