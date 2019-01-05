class Animal:
    count=0
    def __init__(self, name):
        self.ScientificName = name
        self.foot=0
        Animal.count += 1

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

dog1 = Dog()
dog1.Color="yellow"
print(dog1.ScientificName)
print("foot=",dog1.foot)
print(dog1.Color)
print("type=",type(dog1))
print( "count=", Animal.count)
print("\r\n")

dog2 =Dog()
dog2.Color = "白"
print(dog2.ScientificName)
print(dog2.Color)
print("type=",type(dog2))
print( "count=", Animal.count)
print("\r\n")

chicken = Chicken()
print(chicken.ScientificName)
print("foot=",chicken.foot)
print("type=",type(chicken))
print( "count=", Animal.count)
print("\r\n")

