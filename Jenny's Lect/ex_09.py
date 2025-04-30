#Pizza Order Programme
print("HELO! WELCOME YOU ALL FOR PIZZA HUT,SRI_LANKA")
print("---------- Price Menu ----------- \n01 Small Pizza is 100RS \n02 Medium Pizza is 200RS \n03 Large Pizza is 300RS")
size_pizza = input("What Size Pizza You want (S/M/L) :")
bill = 0
if size_pizza == 'S' or size_pizza == 's':
    bill = 100
    print(f"You should be pay {bill}")
    want_pepperoni = input("Do you want pepperoni (Y/N) : ")
    if want_pepperoni == 'Y' or want_pepperoni == 'y':
        bill = bill + 30
        print(f"You Should Pay {bill}")
elif size_pizza == 'M' or size_pizza == 'm':
    bill = 200
    print(f"You should be pay {bill}")
    want_pepperoni = input("Do you want pepperoni (Y/N) : ")
    if want_pepperoni == 'Y' or want_pepperoni == 'y':
        bill = bill + 50
        print(f"You Should Pay {bill}")
elif size_pizza == 'L' or size_pizza == 'l':
    bill = 300
    print(f"You should be pay {bill}")
    want_pepperoni = input("Do you want pepperoni (Y/N) : ")
    if want_pepperoni == 'Y' or want_pepperoni == 'y':
        bill = bill + 50
        print(f"You Should Pay {bill}")
want_cheese = input("Do you want extra cheese (Y/N) : ")
if want_cheese == 'Y' or want_cheese == 'y':
    bill = bill + 20
print(f"Your total bill payment for the pizza is {bill}")
print("WELCOME OUR KIND CUSTOMER!")