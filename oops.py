# Base class
class Person:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    def __init__(self, name, age):
        self.name = name      
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id, grade):

        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def show_student_info(self):
        self.show_details()   
        print(f"Student ID: {self.student_id}, Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.__salary = salary    
        self.subject = subject

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")

    def show_teacher_info(self):
        self.show_details()
        print(f"Subject: {self.subject}, Salary: {self.__salary}")


student1 = Student("Alice", 20, "S101", "A")
teacher1 = Teacher("Mr. John", 40, "Math", 50000)

print("=== Student Info ===")
student1.show_student_info()

print("\n=== Teacher Info ===")
teacher1.show_teacher_info()


print("\nTeacher Salary (via getter):", teacher1.get_salary())
teacher1.set_salary(55000)
print("Updated Salary:", teacher1.get_salary())
