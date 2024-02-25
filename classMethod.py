import random

class Hat:

  house = ['Red', 'Yellow', 'Green', 'Blue']

  @classmethod
  def sort(cls,name):
    print(name,'is from ', random.choice(cls.house))
    
  


Hat.sort("Shubham")