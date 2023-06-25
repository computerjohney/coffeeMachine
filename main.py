# In main.py

import sys
from drinks import DrinksMaker
from money import CheckMoney


class Menu:
    def __init__(self):
        self.MENU = {
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "coffee": 18,
                },
                "cost": 1.5,
            },
            "latte": {
                "ingredients": {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
                "cost": 2.5,
            },
            "cappuccino": {
                "ingredients": {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
                "cost": 3.0,
            },
        }


class Resources:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0,
        }

    def __str__(self):
        lines = self.resources
        # return (str)(lines["water"])
        return f"there is...\n water: {lines['water']}ml\n mik: {lines['milk']}ml\n coffee:{lines['coffee']}g\n money: ${lines['money']}\n"

    # return "\n".join(lines)
    # if self.street2:
    #     lines.append(self.street2)
    # lines.append(f'{self.city}, {self.state} {self.zipcode}')
    # print("__str__() string: ", mydate.__str__())
    # print("str() string: ", str(mydate))
    # print("__repr__() string: ", mydate.__repr__())
    # print("repr() string: ", repr(mydate))


# The menu .MENU is constant, the resources is only in drink!
# the_resources (including money) is updated by drink object ONLY!!!
the_menu = Menu()
the_resources = Resources()
drink = DrinksMaker(the_menu, the_resources)
the_money = CheckMoney(the_menu)


# CONTROLLER
def main():
    while True:
        choice = ""
        try:
            user_input = input("\nWhat would you like? (espresso/latte/cappuccino):\n")

            if user_input.lower() == "off":
                sys.exit(0)
            elif user_input.lower() == "resources" or user_input.lower() == "r":
                #  print(str(res))
                print(the_resources.resources)
            elif user_input.lower() == "espresso" or user_input.lower() == "e":
                choice = "espresso"
            elif user_input.lower() == "latte" or user_input.lower() == "l":
                choice = "latte"
            elif user_input.lower() == "cappuccino" or user_input.lower() == "c":
                choice = "cappuccino"

            if choice == "espresso" or choice == "latte" or choice == "cappuccino":
                output = makeIt(choice)
                print(output + "\n")

        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(e)


def makeIt(choice):
    message = ""
    revenue = 0
    message = drink.checkResources(choice)
    if message != "OK":
        return message
    revenue = the_money.checkMoney(choice)
    print("revenue added: " + str(revenue))

    # add revenue to money in resources
    message = drink.addRevenue(revenue)
    message = drink.makeCoffee(choice)
    return message


if __name__ == "__main__":
    main()
