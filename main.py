from menu import MENU

starting_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee_options = []
for i in MENU:
    coffee_options.append(i)


while True:
    user_choice = input("which coffee do you want? We've got espresso, latte and cappuccino\n")
    if user_choice == "report":
        print(starting_resources)
    elif user_choice in coffee_options:
        user_choice_ingredients = MENU[user_choice]['ingredients']
        user_choice_price = MENU[user_choice]['cost']
        missing_resources = []

        for resource in user_choice_ingredients:
            if starting_resources[resource] - user_choice_ingredients[resource] < 0:
                missing_resources.append(resource)
            else:
                starting_resources[resource] -= user_choice_ingredients[resource]

        if missing_resources:
            print(f"sorry, there is not enough {', '.join(missing_resources)} to make {user_choice}")
        else:
            total_money = int(input("how many quarters?: ")) * 0.25
            total_money += int(input("how many dimes?: ")) * 0.1
            if total_money < user_choice_price:
                print(f"inserted amount is not enough. please add ${round(user_choice_price - total_money,2)}")
            else:
                print(f"please take change of ${round(total_money - user_choice_price,2)}")
                print(f"enjoy your {user_choice}")
    else:
        print("incorrect input")
