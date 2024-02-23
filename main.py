#from functools import lru_cache

#@lru_cache(maxsize=200)

#def fib(n: int) -> int:
 # if n <=1:
  #  return n
  #else:
   # return fib(n-1) + fib(n-2)

#for i in range(0, 100):
#  print(f"{i}: {fib(i)}")




class Student:
  pass


def main():
  student = get_student()
  print(f"{student.name} from {student.house}")


def get_student():
  student = Student()
  student.name = input("Name: ")
  student.house = input("House: ")
  return student
if __name__ == "__main__":
  main()

