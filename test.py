def function(argument):
  return '{} function.' .format(argument)
  
print(function('Hi'))
 
  
  
#----
def function(argument,name='you'):
  return '{}, {} function.' .format(argument,name)
  
print(function('Hi'))
 
  
  
def student_info(*args,*kwargs):
  print(args)
  print(kwargs)

  
student_info('math','art',name='Pavan Kumar',Age=24)
