# Find Bill amount for Ride with Multiple If Statement
height = float(input("Enter your height in ft. : "))
bill = 0
if height >= 3:
    print("You can ride this Roller-Coaster Ride")
    age = int(input("Enter your age : "))
    if age < 12:
        bill = 150
        print(f"Your ticket price is {bill}")
    elif age < 18:
        bill = 250
        print(f"Your ticket price is {bill}")
    else:
        bill = 500
        print("your ticket price is {bill}")
    #NOw, Start the line of code for photos
    want_photo = input("Do you wanna capture your beautiful moments for your memory(Y/N) : ")
    if want_photo == "Y" or want_photo == 'y':
        bill = bill + 50
        print(f"Your Total Bill Payment is {bill}")
    else:
        bill = bill
        print(f"Your Total Payment Should be paid is {bill}")
else:
    print("Sorry!, You cannot be able to ride this due to your less height")
print("Bye!, Thanx for come to our Peace Land. \nCOME AGAIN!")