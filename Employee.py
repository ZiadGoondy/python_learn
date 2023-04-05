class Employee:
    def __init__(self, name, age, department, is_manger, rating, salary):
        self.name = name
        self.age = age
        self.department = department
        self.is_manger = is_manger
        self.rating = rating
        self.salary = salary

    def is_excellent(self):
        if self.rating >= 4:
            return True
        else:
            return False

    def bonus(self):
        if self.age >= 22:
            self.salary += 1510
            print("salary increased to "+str(self.salary))
        else:
            print("salary does not increase")

