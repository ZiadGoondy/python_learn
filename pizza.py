class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def veg(cls):
        return cls(["mushrooms", "olives", "onions"])

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "olives"])

    def __str__(self):
        return f"Pizza ingredients are {self.ingredients}"

pizza1 = Pizza(["tomato", "sauce", "cheese"])
pizza2 = Pizza.veg()
pizza3 = Pizza.margherita()
print(pizza1, pizza2, pizza3)
