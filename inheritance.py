from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"name is {self.name} and age is {self.age}"

    @classmethod
    def init_from_birth_year(cls, name, birth_year, extra):
        return cls(name, date.today().year - birth_year, extra)


class Man(Person):
    gender = "Male"
    no_of_men = 0

    def __init__(self, name, age, voice):
        super().__init__(name, age)
        self.voice = voice
        Man.no_of_men += 1

    def display(self):
        string = super().display()
        return string + f" and voice is {self.voice} and gender is {self.gender}"


class Woman(Person):
    gender = "fe-Male"
    no_of_women = 0

    def __init__(self, name, age, hair):
        super().__init__(name, age)
        self.hair = hair
        Woman.no_of_women += 1

    def display(self):
        string = super().display()
        return string + f" and hair is {self.hair} and gender is {self.gender}"


man1 = Man("Ali", 35, "thin")
woman1 = Woman("Sara", 32, "blonde")
print(man1.display())
print(Man.no_of_men)

print(woman1.display())
print(Woman.no_of_women)

man2 = Man.init_from_birth_year("Ziad", 1999, "smooth")
print(man2.display())
print(isinstance(man1, Man))
print(isinstance(man1, Person))
