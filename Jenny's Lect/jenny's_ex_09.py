size = input("What size of Pizza you prefer (S/M/L) :")
bill = 0
if size == "S" or size == 's':
    bill += 100
    print("You Selected Small Size Pizza and its prices is 100Rs")
elif size == "M" or size == 'm':
    bill += 200
    print("You Selected Medium Size Pizza and its prices is 200Rs")
else:
    bill += 300
    print("You Selected Large Size Pizza and its prices is 300Rs")

add_pepperoni = input("Do you want pepperoni (Y/N): ")
if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if size == "S" or size == 's':
        bill += 30
        print(f"You selected the pepperoni and then you should pay the amount of {bill}RS")
    else:
        bill+= 50
        print(f"You selected the pepperoni and then you should pay the amount of {bill}RS")
extra_cheese = input("Do you want extra cheese to add (Y/N) : ")
if extra_cheese == "y"  or extra_cheese == 'Y':
    bill += 20
total_bill = bill
print(f"Finally, You wanna pay {total_bill}RS for the Pizza!")
print("Bye! WELCOME GAIN!")
