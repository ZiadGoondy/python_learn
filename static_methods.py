class Pizza:
    def __init__(self, ingredients, radius):
        self.ingredients = ingredients
        self.radius = radius

    def __str__(self):
        return f"the ingredients is {self.ingredients}"

    def area(self):
        return Pizza.circle_area(self.radius)

    @staticmethod
    def pi():
        return 3.14

    @staticmethod
    def circle_area(rad):
        return rad ** 2 * Pizza.pi()


pizza1 = Pizza(["tomato", "sauce", "cheese"], 25)

print(pizza1.area())
print(Pizza.circle_area(4))
x = "https://www.youtube.com/watch?v=A9kSngn7254&list=PLuXY3ddo_8nzrO74UeZQVZOb5-wIS6krJ&index=35"
print(x)
