class Person:
    def __init__(self, name, age, address, height):
        self.name = name
        self.age = age
        self.address = address
        self.height = height

    def display_user(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}, Height: {self.height}")

# Create objects
person1 = Person("Ganesh", "infinity", "everywhere", "infinity")
person2 = Person("Ram", 21, "Karnataka", 130)
person3 = Person("Ichimoku", 45, "Tokyo", 190)

# Display details
person3.display_user()
print(person1.name)
print(person2.name)
print(person3.name)
