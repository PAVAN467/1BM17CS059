a=input("enter the string")


def revlis(str1):
    lis=str1.split(" ")
    print(lis)
    lis.reverse()
    print(lis)
    print(" ".join(lis))



def revstring(str1):
    lis=str1.split(" ")
    print(lis)
    lis2= " "
    print(lis2)
    for i in lis:
        lis2+=i[::-1]
        lis2+=" "
    print(lis2)    

revlis(a)
revstring(a)

    
