class atm:
    def __init__(self):
        self.pin = 0
        self.balance = 0
        self.menu()
    def menu(self):
        user_input = (input("""Hello how can I help you ?
              1.create pin
              2.change pin
              3.check balance
              4.withdraw
              5.Any thing else to exit"""))
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        elif user_input == '5':
            exit()

    def create_pin(self):
        user_pin = int(input("please enter your new pin"))
        self.pin = user_pin

        user_balance  = int(input("Enter your balance"))
        self.balance = user_balance

        print("pin created successfully")
        self.menu()

    def change_pin(self):
        n =  int(input("Enter your old pin = "))
        if (n == self.pin):
            new_pin = int(input("Enter your new pin = "))
            self.pin = new_pin
            print("your pin is changed to = ",self.pin)
        else:
            print("You entered wrong pin")
        self.menu()
    def check_balance(self):
        n = int(input("Enter your pin"))
        if (n==self.pin):
            print("your balance is = ",self.balance)
        else:
            print("you entered wrong pin")
        self.menu()
    def withdraw(self):
        n = int(input("Enter the amount to withdraw = "))
        if (n >= self.balance):
            print("Insufficient balance")
        else:
            self.balance = self.balance - n
            print("your balance is = ", self.balance )
        self.menu()
A = atm()