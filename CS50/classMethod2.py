class Student:

  def __init__(self, name, house):
    self.name = name
    self.house = house

  def __str__(self):
    return f"{self.name} from {self.house} house"

  @classmethod
  def get(cls):
    name   = input("Name: ")
    house  = input("House: ").capitalize()
    return cls(name, house)

  #getter
  @property
  def name(self):
    return self._name


  #setter
  @name.setter
  def name(self, name):
    if not name:
      raise ValueError("Missing Name")
    self._name = name

  #getter
  @property
  def house(self):
    return self._house

  #setter
  @house.setter
  def house(self, house):
    if house not in ['Red', 'Yellow', 'Green', 'Blue']:
      raise ValueError(f"Invalid house color: {house} ")
    self._house = house


def main():

  student = Student.get()
  print(student)



if __name__ == "__main__":
  main()
