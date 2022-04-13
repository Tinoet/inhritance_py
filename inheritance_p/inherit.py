class mammal:
  def walk(self):
    print("walk")


class Dog(mammal):
  pass

class Cat(mammal):
  pass

dog1=Dog()
dog1.walk()