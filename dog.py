#Inheritance in python class
class Animal:
    test = "Animal class test.."

    def __init__(self):
        print("Animal is created...")

    def speak(self):
        return "Animal is speaking.."


class Dog(Animal):
    dog_test = "Dog class test...."

    def __init__(self):
        super().__init__()  
        print("Dog is created..")
    dog_test2 = "Dog class test 2..."    

    def speak(self):
        return "Dog is barking.."


dog1 = Dog()
dog2 = Dog()
dog3 = Dog()

dog1.dog_test = "Dog1 test has been modified...."
print(dog1.dog_test)
print(dog2.dog_test)
print(dog3.dog_test)

print("===================================================")

dog1.dog_test2 = "Dog test has been postponed..."
print(dog1.dog_test2)
print(dog2.dog_test2)
print(dog3.dog_test2)
