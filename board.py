n=int(input())
s1=' ---'*n
s2='|   '
for i in range(n) :
	print(s1)
	for j in range(n+1) :
		print(s2,end="")
	print()
print(s1)
