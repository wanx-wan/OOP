class base(object): 
   def base_func(self): 
      print('Method of base class')
class child(base): 
   def base_func(self): 
      print('Method of child class')

class next_child(child): 
   def base_func(self): 
      print('Method of next_child class')
obj = next_child()
obj.base_func()
