import menu
import os

profit = 0


def report(resources):
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${profit:.2f}")

def GetMoney():
    change = []
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    change.append(quarters/4)
    dimes = int(input("How many dimes?: "))
    change.append(dimes/10)
    nickels = int(input("How many nickels?: "))
    change.append(nickels/20)
    pennies = int(input("How many pennies?: "))
    change.append(pennies/100)
    return sum(change)

def checkResources(choice, menu, resources):
    water = menu[choice]["ingredients"]["water"]
    milk = menu[choice]["ingredients"]["milk"]
    coffee = menu[choice]["ingredients"]["coffee"]

    if resources["water"] < water:
        print("Sorry. There is not enough water")
        return False

    if resources["milk"] < milk:
        print("Sorry. There is not enough milk")
        return False

    if resources["coffee"] < coffee:
        print("Sorry. There is not enough coffee")
        return False
    
    return True

# def changeMoney(coins):
#     quarters = (coins[0]/4)
#     dimes = (coins[1]/10)
#     nickels = (coins[2]/20)
#     pennies = (coins[3]/100)
#     total = quarters + dimes + nickels + pennies
#     return total


while True:
    choice = str(input("What would you like? (espresso/latte/cappccino): ")).lower()

    if choice == "off":
        print("Thanks for playing")
        exit()

    if choice == "report":
        report(menu.resources)
    elif choice in menu.MENU:
        if checkResources(choice, menu.MENU, menu.resources):
            money = GetMoney()
            if money >= menu.MENU[choice]["cost"]:
                change = money - menu.MENU[choice]["cost"]
                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {choice}. Enjoy!")
                # Deduct resources after a successful purchase
                menu.resources["water"] -= menu.MENU[choice]["ingredients"].get("water", 0)
                menu.resources["milk"] -= menu.MENU[choice]["ingredients"].get("milk", 0)
                menu.resources["coffee"] -= menu.MENU[choice]["ingredients"]["coffee"]
                profit += menu.MENU[choice]["cost"]
            else:
                print("Sorry not enough money. Money refunded")
        else:
            print("Not enough resources")
    else:
        print("Invalid choice please try again. Or type 'off' to quit the program")
        

