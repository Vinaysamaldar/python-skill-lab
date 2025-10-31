class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

s1 = Student("Alice", 20)
s2 = Student("Bob", 22)

s1.show_info()
s2.show_info()
                                                                                             