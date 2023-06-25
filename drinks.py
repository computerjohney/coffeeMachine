# In drinks.py
# espresso/latte/cappuccino

# TODO: check resources, use the resources


class DrinksMaker:
    def __init__(self, the_menu, the_resources):
        # menu is a constant MENU
        self.the_menu = the_menu
        self.resources = the_resources
        self.choice = ""

    def checkResources(self, choice):
        self.choice = choice
        # print("chose: " + self.choice)

        ingredients = self.the_menu.MENU[self.choice]["ingredients"]
        water = int(ingredients["water"])
        coffee = int(ingredients["coffee"])
        # my_dict.get('keyname', 'something else')
        milk = int(ingredients.get("milk", 0))
        if (int)(self.resources.resources["water"]) < water:
            return "Sorry, there is not enough water"
        if (int)(self.resources.resources["coffee"]) < coffee:
            return "Sorry, there is not enough coffee"
        # got < needed by ingredients menu?
        if (int)(self.resources.resources["milk"]) < milk:
            return "Sorry, there is not enough milk"
        return "OK"

    def makeCoffee(self, choice):
        self.choice = choice
        # print("chose: " + self.choice)

        ingredients = self.the_menu.MENU[self.choice]["ingredients"]
        # print(str(ingredients))

        water = int(ingredients["water"])
        coffee = int(ingredients["coffee"])
        # my_dict.get('keyname', 'something else')
        milk = int(ingredients.get("milk", 0))
        self.resources.resources["water"] = (int)(
            self.resources.resources["water"]
        ) - water
        self.resources.resources["coffee"] = (int)(
            self.resources.resources["coffee"]
        ) - coffee
        self.resources.resources["milk"] = (int)(
            self.resources.resources["milk"]
        ) - milk

        return "OK"

    def addRevenue(self, revenue):
        self.resources.resources["money"] = (int)(
            self.resources.resources["money"]
        ) + revenue
        return "OK"
