class Animal:
    def __init__(self, name):
        self.ScientificName = name
        self.foot=0

class Dog(Animal):
    def __init__(self):
        super().__init__("Dog")
        self.foot=4

    @property
    def Color(self):
        return self.__color

    @Color.setter
    def Color(self, value):
        self.__color = value

class Chicken(Animal):
    def __init__(self):
        super().__init__("Chicken")
        self.foot=2

print("\r\n")

dog = Dog()
dog.Color="yellow"
print(dog.ScientificName)
print("foot=",dog.foot)
print(dog.Color)
print("type=",type(dog))
print("\r\n")

chicken = Chicken()
print(chicken.ScientificName)
print("foot=",chicken.foot)
print("type=",type(chicken))
print("\r\n")

