class ShoppingList:
    
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe, portions):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled_recipe = recipe.scale(portions)
        for ing in scaled_recipe.ingredients:
            self._items.append((ing, recipe.title))

    def remove_recipe(self, title: str):
        self._items = [i for i in self._items if i[1] != title]

    def get_list(self):
        dic = {}
        for ing, j in self._items:
            key = (ing.name, ing.unit)
            if key in dic:
                dic[key] += ing.quantity
            else:
                dic[key] = ing.quantity
        
        result = [Ingredient(name, qty, unit) for (name, unit), qty in dic.items()]
        return sorted(result, key=lambda x: x.name)

    def __add__(self, other):
        new_list = ShoppingList()
        new_list._items = self._items + other._items
        return new_list
