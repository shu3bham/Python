class Wizard:
  def __init__(self, name):
    if not name:
      raise ValueError("Missing name")
    self.name = name

  def __str__(self):
    return f"Wizard {self.name}"

class Student(Wizard):
  def __init__(self,name,house):
    super().__init__(name)
    self.house = house

class Professor(Wizard):
  def __init__(self,name,subject):
    super().__init__(name)
    self.subject=subject


wizard = Wizard("Shubham")
student= Student("Rahul","Green")
professor = Professor("Akshay","Dark Arts")

print(professor)
  
    







