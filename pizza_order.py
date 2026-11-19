
print("WELCOME TO PIZZA ORDERING SYSTEM!")

pizza_size = input("Enter pizza size (Small/Medium/Large): ").lower()

total_bill = 0

if pizza_size == "small":
    total_bill += 100
    print("Small Pizza: Rs.100")

elif pizza_size == "medium":
    total_bill += 200
    print("Medium Pizza: Rs.200")

elif pizza_size == "large":
    total_bill += 300
    print("Large Pizza: Rs.300")

else:
    print("Invalid pizza size!")
    exit()

pepperoni_choice = input("Do you want pepperoni? (Yes/No): ").lower()

if pepperoni_choice == "yes":
    if pizza_size == "small":
        total_bill += 30
        print("Small Pepperoni: Rs.30")
    else:
        total_bill += 50
        print("Medium/Large Pepperoni: Rs.50")

cheese_choice = input("Do you want extra cheese? (Yes/No): ").lower()

if cheese_choice == "yes":
    total_bill += 20
    print("Extra Cheese: Rs.20")

print("--------------------------")
print(f"Your total bill is Rs.{total_bill}")
print("THANK YOU! HAVE A GOOD DAY!")
