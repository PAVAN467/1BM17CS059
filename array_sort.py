"""

def fib(n ):
    if n<=1:
        return n
    else :
        return fib(n-1)+fib(n-2)
    



a=int(input("enter  elements "))
if a<=0:
    print("enter valid")

for i in range (a):
    print(fib(i)) 
    

"""

def fact(n):
    if n==1 or n==0:
        return 1
    else :
        return n*fact(n-1)


print(fact(5))    







    
   
