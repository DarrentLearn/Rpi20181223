class Animal:
    def __init__(self, name):
        self.ScientificName = name

class Dog(Animal):
    def __init__(self):
        return super().__init__("Dog")

class Cat(Animal):
    def __init__(self):
        return super().__init__("Cat")

dog = Dog()
print(dog.ScientificName)
print(type(dog))

cat = Cat()
print(cat.ScientificName)
print(type(cat))

catabc = Cat()
print(catabc.ScientificName)
