import random
import time
import os
balence = random.randint(1000,25000000)
ToF = int(2)

print("Welcome to Python Bank")
time.sleep(1)
cardNum = int(input("Please enter card number:\n"))
time.sleep(1)
pin = int(input("Please enter pin number:\n"))

if cardNum == 4160211518824561 and pin == 1208:
    while ToF == 2:
        print("Please type in your command")
        time.sleep(0.5)
        print("1 for checking balence")
        time.sleep(0.5)
        print("2 for Cash Withdrawal")
        time.sleep(0.5)
        print("3 for Adding Cash into account")
        time.sleep(0.5)
        command = int(input("4 to exit operation\n"))
        time.sleep(0.5)
        if command == 1:
            print("Your current bank balence is ", balence, "\n")
        elif command == 2:
            withdrawalAmount = int(input("How much do you want to withdraw:\n"))
            if withdrawalAmount > balence:
                print("Insufficient fund\n")
            else:
                balence = balence - withdrawalAmount
                print("Your bank balence is now ", balence)
        elif command == 3:
            addingAmount = int(input("Insert cash amount\n"))
            balence = balence + addingAmount
            print("Account succesfully updated\n")
        else:
            ToF = ToF + 1
            print("Exiting operation")
            time.sleep(0.5)
            print("Thank you for visiting")
            time.sleep(0.5)
            print("Hope to see you next time")

else:
    if cardNum != 4160211518824561:
        print("Account not found")
    else:
        print("Incorrect pin")