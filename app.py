class ATM:
       def __init__(self):
              """Initialize the ATM with a default Pin and Balance"""
              self.pin = "1234"
              self.balance = 1000.0
              self.is_authenticated=False
       def check_pin(self,input_pin):
              """Verify the entered PIN"""
              if input_pin==self.pin:
                     self.is_authenticated=True
                     print("Pin is correct.\n")
              else:
                     print("Pin is incorrect.\n")
       def check_balance(self):
              """"Display the current balance"""
              if self.is_authenticated:
                     print(f"Current balance is RS.{self.balance:.2f}\n")
              else:
                     print("Please enter your correct PIN to check your balance.\n")
       def deposit(self,amount):
              """Deposit the amount into the ATM"""
              if self.is_authenticated:
                     if amount>0:
                        self.balance+=amount
                        print(f"Amount deposited is RS.{amount:.2f}\n")
                        print(f"New balance is RS.{self.balance:.2f}\n")
                     else:
                        print("Invalid amount.\n")
              else:
                     print("Please enter your correct PIN to deposit.\n")
       def withdraw(self,amount):
              """Withdraw the amount from the ATM"""
              if self.is_authenticated:
                    if amount<=0:
                          print("Amount to withdraw cannot be negative.\n")
                    elif amount>self.balance:
                                 print("Insufficient balance.\n")
                    else:
                           self.balance -=amount
                           print(f"Amount withdrawn is RS.{amount:.2f}\n")
                           print(f"New balance is RS.{self.balance:.2f}\n")
              else:
                     print("Please enter your correct PIN to withdraw.\n")
       def exit(self):
              """Exit the ATM"""
              print("Thank you for using the ATM.\n")
              return False #indicates to exit the loop
       def menu(self):
              """Display the menu"""
              print("Welcome to the ATM.\n")
              attempts=0
              while attempts<3:
                     input_pin=input("Enter your PIN: ")
                     if input_pin==self.pin:
                            self.is_authenticated=True
                            print("You have successfully logged in.\n")
                            break
                     else:
                            attempts+=1
                            print(f"Incorrect PIN. Attempts left: {3- attempts}\n")
              else:
                     print("Too many incorrect attempts. Exiting the ATM.\n")
                     return
              while True:
                     print("ATM Menu\n")
                     print("1. Check Balance\n")
                     print("2. Deposit\n")
                     print("3. Withdraw\n")
                     print("4. Exit\n")
                     choice=input("Please select an option(1-4):")
                     if choice=="1":
                            self.check_balance()
                     elif choice=="2":
                            try:
                                   amount=float(input("Enter the amount to deposit:.\n"))
                                   self.deposit(amount)
                            except ValueError:
                                   print("Invalid amount.\n")
                     elif choice=="3":
                            try:
                                   amount=float(input("Enter the amount to withdraw:.\n"))
                                   self.withdraw(amount)
                            except ValueError:
                                   print("Invalid amount.\n")
                     elif choice=="4":
                            if not self.exit():
                                   break
                     else:  
                            print("Invalid option.\n")    

#Create an instance of the ATM class and start the menu
if __name__=="__main__":
       atm=ATM()
       atm.menu()
                                