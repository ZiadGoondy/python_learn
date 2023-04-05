from datetime import date

class Student:
    student_no = 0

    def __init__(self, name, age=0, courses='null'):
        self.__name = name
        self.__age = age
        self.courses = courses
        Student.student_no += 1

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age

    def describe(self):
        print(f"My name is {self.__name} and my age is {self.__age} ")

    def is_old(self, num):
        if self.__age > num:
            print("Student is old")
        else:
            print("student is not old")

    @classmethod
    def init_from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)



student1 = Student("ziad", 23, ["math", "cs"])
student2 = Student("ziad", 23, ["math", "cs"])
student3 = Student.init_from_birth_year("ali", 1993)
print(Student.student_no)

student1.describe()
student1.is_old(27)

print(student1.get_name())
student1.set_name("nader")
print(student1.get_name())

student1.set_name("mohammed")
student1.set_age(45)

student1.describe()
student3.describe()

