
"""
class CallDetail:

    def __init__(self,list1):
        self.dialn=list1[0]
        self.rcvn=list1[1]
        self.duration=list1[2]
        self.calltype=list1[3]

    def print1(self):
        print(self.dialn, self.rcvn,self.duration,self.calltype)
        
    
        
        
    
    

listobj=[]
class Util:
    def parse_customer(self,list_of_call_string):
        for i in list_of_call_string:
            li1=i.replace("'","")
            li1=li1.split(",")
            ob=CallDetail(li1)
            listobj.append(ob)
            
             
        
        




call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'
list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)
for obj in listobj:
    obj.print1()
    
    
"""
class Student:
    def __init__(self,age,marks):
        self.age=age
        self.marks=marks

  
            
         
    def validate1(self):
        if(self.age<=20):
            print("age  not eligible")
            return 0
        while True:
            if self.marks<0 or self.marks>100:
                self.marks=int(input("enter the valid marks"))
            else:
                break
                
    def validate(self):
           if(self.age<=20 or self.marks<65): print(" not eligible ")
           else : print("eligible ")      
             



b=int(input("enter age"))
a=int(input("enter the marks"))


c1=Student(b,a)
c1=Student(b,a)
c1.validate1()
c1.validate()
              
