class User:       
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        
    def make_deposit(self, amount):
        self.account_balance += amount
        
    def make_withdrawal(self, amount):
        if(amount > self.account_balance):
            print('No enough balance for withdrawal amount!!')
        else:
            self.account_balance -= amount
        
    def transfer_money(self, other_user, amount):
        if(amount > self.account_balance):
            print('No enough balance for this transfer!!')
        else:
            self.account_balance -= amount
        other_user.account_balance += amount
        
    def display_user_balance(self):
        print(f'User: {self.name}, Balance: ${self.account_balance}')
       
# Create 3 instances of the User class 
user_1 = User("User 1", "user.1@axsos.academy")
user_2 = User("User 2", "user.2@axsos.academy")
user_3 = User("User 3", "user.3@axsos.academy")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
user_1.make_deposit(500)
user_1.make_deposit(100)
user_1.make_deposit(150)
user_1.make_withdrawal(150)
user_1.display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
user_2.make_deposit(500)
user_2.make_deposit(100)
user_2.make_withdrawal(150)
user_2.make_withdrawal(50)
user_2.display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
user_3.make_deposit(200)
user_3.make_withdrawal(150)
user_3.make_withdrawal(150)
user_3.make_withdrawal(150)
user_3.display_user_balance()

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
user_1.transfer_money(user_3, 50)
user_1.display_user_balance()
user_3.display_user_balance()



