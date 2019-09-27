n=int(input("enter the number"))
x=int(input("width"))
y=int(input("height"))
a='-'*x*2
b='|'
b1=(b+'  '*x)*n


a1=(' '+a)*n

for i in range(n):
  print(a1)
  for i in range(y):
    print(b1+b)

 
print(a1)


