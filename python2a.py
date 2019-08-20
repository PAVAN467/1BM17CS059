lis=[]






def search(lis,a):
    print(lis)
    if a in lis:
        return True
    else:
        return False
    
while True:
    a=int(input("enter the elements"))
    if a!=-1:
        lis.append(a)

    else:
        break


b=int(input("enter element to be searched"))
x=search(lis,b)
print(x)

