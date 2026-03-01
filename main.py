import random 
import json
from pathlib import Path


class Bank:
    database = "data.json"
    data = []

    try:
        if Path(database).exists():
            with open(database, "r") as f:
                data = json.load(f)
        else:
            data = []
    except Exception as error:
        print(f"An exception occurred: {error}")

    @classmethod
    def Update(cls):
        with open(cls.database, "w") as f:
            json.dump(cls.data, f, indent=4)

    @classmethod
    def Accountno(cls):
        account = random.randint(1000000000, 9999999999)
        return account

    def CreateAccount(self):
        print("-"*40)
        
        info = {
            "Name" : input("Enter your name: "),
            "Email" : input("Enter your Email: "),
            "Gender" : input("Enter your Gender: "),
            "Age" : int(input("Enter your age: ")),
            "Pin" : int(input("Enter your PIN: ")),
            "AccountNo." : Bank.Accountno(),
            "Balance" : 0
            }

        try:
            if len(str(info["Pin"])) != 4 or info["Age"] < 18:
                print("Sorry you cannot create your account")
            else:
                print("-"*40)
                print("Your Account has been created successfully")
                print("-"*40)
                print("Your Details are --------------->")
                print("-"*40)
                for i in info:
                    print(f"{i} : {info[i]}")
                print("-"*40)
                print("Please Save your Data !!!")
                print("-"*40)

        except Exception as error:
            print(f"There is an error of {error}")

        Bank.data.append(info)
        Bank.Update()


    def DepositMoney(self):

        account = int(input("Enter your Account Number: "))
        pin = int(input("Enter your PIN aswell: "))
        
        user_data = [i for i in Bank.data if i["AccountNo."] == account and i["Pin"] == pin]

        if user_data == False:
            print("Sorry no data found !!")
        else:
            amount = int(input("How much you want to deposite: "))
            if amount > 10000 or amount < 0:
                print("Sorry amount is to much to deposite and above 0")
            else:
                user_data[0]["Balance"] += amount
                Bank.Update()
                print("Amount Deposited successfully")
            

    def Withdraw(self):

        account = int(input("Enter your Account Number: "))
        pin = int(input("Enter your PIN aswell: "))
        
        user_data = [i for i in Bank.data if i["AccountNo."] == account and i["Pin"] == pin]

        if user_data == False:
            print("Sorry no data found !!")
        else:
            amount = int(input("How much you want to Withdraw: "))
            if user_data[0]["Balance"] < amount:
                print("You Dont have enough Money to withdraw")
            else:
                user_data[0]["Balance"] -= amount
                Bank.Update()
                print("Amount Withdrewn successfully")
            

    def Details(self):

        account = int(input("Enter your Account Number: "))
        pin = int(input("Enter your PIN aswell: "))
        
        user_data = [i for i in Bank.data if i["AccountNo."] == account and i["Pin"] == pin]
        print("Your Data  is --------->")
        for i in user_data[0]:
            print(f"{i} : {user_data[0][i]}")

    def updateDetails(self):
        account = int(input("Enter your Account Number: "))
        pin = int(input("Enter your PIN as well: "))

        user_data = [i for i in Bank.data if i["AccountNo."] == account and i["Pin"] == pin]

        if not user_data:
            print("No such user found")
            return

        user = user_data[0]

        print("You cannot change Age, Account Number, or Balance")
        print("Leave field empty if no change")

        new_name = input("Enter new Name or press Enter: ")
        new_email = input("Enter new Email or press Enter: ")
        new_pin = input("Enter new Pin or press Enter: ")

        # Update values only if provided
        if new_name != "":
            user["Name"] = new_name

        if new_email != "":
            user["Email"] = new_email

        if new_pin != "":
            if len(new_pin) == 4:
                user["Pin"] = int(new_pin)
            else:
                print("PIN must be 4 digits")
                return

        Bank.Update()
        print("Details updated successfully!")


    def delete(self):
        account = int(input("Enter your Account Number: "))
        pin = int(input("Enter your PIN as well: "))

        user_data = [i for i in Bank.data if i["AccountNo."] == account and i["Pin"] == pin]
        if user_data == False:
            print("Sorry no such User data found")
        else:
            check = input("press y if you actually want to delete the account or press n")
            if check == 'n' or check == "N":
                print("bypassed")
            else:
                index = Bank.data.index(user_data[0])
                Bank.data.pop(index)
                print("account deleted successfully ")
                Bank.update()
        

user = Bank()  
print("Press 1 for creating an Account")
print("Press 2 for Depositing the Money in the Bank")
print("Press 3 for Withdrawing the Money")
print("Press 4 for Details")
print("Press 5 for Updating the Details")
print("Press 6 for Deleting your Account")
print("-"*40)
Check = int(input("Tell your response :- "))

if Check == 1:
    user.CreateAccount()
if Check == 2:
    user.DepositMoney()
if Check == 3:
    user.Withdraw()
if Check == 4:
    user.Details()
if Check == 5:
    user.updateDetails()
if Check == 6:
    user.delete()