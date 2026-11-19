
print("WELCOME TO PIZZA ORDERING SYSTEM!")

a = input("Enter pizza size (Small/Medium/Large): ").lower()

bill = 0

if a == "small":
    bill += 100
    print("Small Pizza: Rs.100")
elif a == "medium":
    bill += 200
    print("Medium Pizza: Rs.200")
elif a == "large":
    bill += 300
    print("Large Pizza: Rs.300")
else:
    print("Invalid pizza size!")
    exit()

b = input("Do you want pepperoni? (Yes/No): ").lower()

if b == "yes":
    if a == "small":
        bill += 30
        print("Small Pepperoni: Rs.30")
    else:
        bill += 50
        print("Medium/Large Pepperoni: Rs.50")

c = input("Do you want extra cheese? (Yes/No): ").lower()

if c == "yes":
    bill += 20
    print("Extra Cheese: Rs.20")

print("--------------------------")
print(f"Your total bill is Rs.{bill}")
print("THANK YOU! HAVE A GOOD DAY!")
