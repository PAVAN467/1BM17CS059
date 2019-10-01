

with open('something.txt') as primesfile:
	line = primesfile.read()
	
with open('data.txt') as happiesfile:
	line1= happiesfile.read()

line=line.split(" ")
line1=line1.split(" ")


overlaplist = []
for num in line:
    if num in line1:
        overlaplist.append(num)
overlaplist.pop()
		
print(overlaplist)



