# In money.py

# TODO: take in money - count, check resources, return it


class CheckMoney:
    def __init__(self, the_menu):
        self.choice = ""
        self.the_menu = the_menu

    def checkMoney(self, choice):
        self.choice = choice
        cost = (str)(self.the_menu.MENU[self.choice]["cost"])
        total = 0
        coins = ""
        print("The cost for choice: " + self.choice + " is: $" + cost)
        print(
            "Please enter your coins 1 at a time with a letter and enter, enter twice to finish"
        )
        print(
            "q for quarters = $0.25, d for dimes = $0.10, n for nickles = $0.05, p for pennies = $0.01 "
        )
        while True:
            coins = input("enter  q|d|n|p or enter\n")

            if coins == "q":
                total = round(total + 0.25, 2)
                print("total so far :" + str(total))
            elif coins == "d":
                total = round(total + 0.1, 2)
                print("total so far :" + str(total))
            elif coins == "n":
                total = round(total + 0.05, 2)
                print("total so far :" + str(total))
            elif coins == "p":
                total = round(total + 0.01, 2)
                print("total so far :" + str(total))

            else:
                break

        cost = round(float(cost), 2)
        if total < cost:
            print(f"sorry, not enough for a {choice}, returning {total}")
            return 0
        if total > cost:
            print(f"OK your change: {total-cost}")
            total = cost
        return total
