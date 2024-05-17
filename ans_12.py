class BankAccount:
    
    def __init__(self,acc_name,acc_num,acc_balance,acc_pin):
        self.acc_name = acc_name
        self.acc_num = acc_num
        self.acc_balance = acc_balance
        self.acc_pin = acc_pin

    def __str__(self):
        user_entered_pin = int(input("Enter PIN of your bank :- "))
        if self.acc_pin == user_entered_pin:
            return f"Acc_Name :- {self.acc_name} \nAcc_Num :- {self.acc_num} \nAcc_Balance :- {self.acc_balance}"
        else:
            print("Please Enter Correct PIN")
    
    def deposit(self):
        user_entered_pin = int(input("Enter PIN of your bank :- "))
        if self.acc_pin == user_entered_pin:
            money_to_be_added = int(input("How much money you want to add :- "))
            self.acc_balance += money_to_be_added

            print(f"{money_to_be_added} Rs. added to your account successfully")
        else:
            print("Please Enter Correct PIN")

    def withdraw(self):
        user_entered_pin = int(input("Enter PIN of your bank :- "))
        if self.acc_pin == user_entered_pin:
            money_to_be_withdraw = int(input("How much money you want to withdraw :- "))
            if money_to_be_withdraw > self.acc_balance:
                print("Your account don't have sufficient balance")
            else:
                self.acc_balance -= money_to_be_withdraw
                print(f"{money_to_be_withdraw} Rs. debited from your account successfully")
        else:
            print("Please Enter Correct PIN")

b1 = BankAccount(acc_name='Ram',acc_num='123456789',acc_balance=10000,acc_pin=0000)

info = """1. Press 'd' for your bank details
2. Press 'D' for deposit
3. Press 'W' for withdraw
4. Press 'Q' for quit the program"""
print(info)

while True:
    opt = input("\nEnter Your Choice :- ")
    
    match(opt):
        case 'd' : 
            print(b1)
            continue

        case 'D' :
            b1.deposit()
            continue

        case 'W' :
            b1.withdraw()
            continue

        case 'Q' :
            break