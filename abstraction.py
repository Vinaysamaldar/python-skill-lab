from abc import ABC, abstractmethod

# Define an abstract base class
class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass  # subclasses must override this method

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

dog = Dog()
print(dog.make_sound())  

cat = Cat()
print(cat.make_sound())  

