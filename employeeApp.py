from Employee import Employee

employee1 = Employee("ziad", 23, "EED", True, 5, 15000)
employee2 = Employee("Amr", 21, "PED", False, 3.5, 7000)

print(employee1.salary)
employee1.bonus()
print(employee2.salary)
employee2.bonus()
print(employee1.salary)
employee1.bonus()
print(employee2.salary)
employee2.bonus()
