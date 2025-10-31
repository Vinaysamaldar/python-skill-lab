class Person:
    #private variable
    __no_of_eyes = 2#class variable
    def __init__(self, name, age, address, height):
        print("Object is being created..")
        self.name = name
        self.age = age
        self.address = address
        self.height = height

    def display_user(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}, Height: {self.height}")

    def get_no_of_eyes(self):
        return Person.__no_of_eyes

    def set_up_of_eyes(self,no_of_eyes):
        if no_of_eyes < 0:
            print("Invalid number of eyes")
        else:
            Person.__no_of_eyes = no_of_eyes

    def get_user_name(self):
        return self.name
    def set_user_name(self, name):
        self.name = name        


# Create objects
person1 = Person("Ganesh", "infinity", "everywhere", "infinity")
person2 = Person("Ram", 21, "Karnataka", 130)

print(person1.get_user_name())


#person1.set_user_name("Lord ganesh")
print(person1.get_user_name())
#accessing private variable directly using __classname_variablename hack


# Display details
#person1.__no_of_eyes = 500
#print(person1.__no_of_eyes)
#print(person2.name)


