import random as r


class BankHolder:
    def __init__(self, name, age, bank, accountnumber):
        try:
            self.name = name
            if len(self.name) <= 2:
                raise ValueError("Your name shouldn't be two characters")

            self.age = age
            if self.age < 18:
                raise ValueError("You are a minor")
            else:
                pass
            upper_bank = bank.upper()
            self.bank = upper_bank
            if len(self.bank) == 0 or len(self.bank) == 0:
                raise ValueError("You didn't select a bank")
            elif upper_bank == "FNB" or upper_bank == "NEDBANK" or upper_bank == "PRIVATE BANK":
                pass
            else:
                raise ValueError("Invalid bank selected")
            self.accountnumber = accountnumber
        except ValueError as ve:
            print("Value Error:", ve)

    def details(self):
        return f"Welcome, {self.name}! You have successfully created an account with {self.bank}.Your account number is {self.accountnumber}. Your current balance is R0."


try:
    user_name = input("Enter your name: ")
    user_age = int(input("Enter age: "))
    user_bank = input("What bank do you wish to use (FNB/NEDBANK/PRIVATE BANK): ")
    user_aN = r.randint(1000000, 1999999)
    user_information = BankHolder(user_name, user_age, user_bank, user_aN)
    print(user_information.details())

except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)
