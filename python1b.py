list1=[]

a=int(input("enter the elements"))

while a!=-1:
    list1.append(a)
    a=int(input("enter remaining elements"))
          
print(list1)
i=0
anotherlist=[]
for i in range(len(list1)):
          
          if(i%2==0):
              anotherlist.append(list1[i])

print(anotherlist)

          
          
          
          
          



