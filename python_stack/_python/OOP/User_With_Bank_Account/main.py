class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self 
    
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
    


class User:       
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}

    def add_account(self, account_name, int_rate=0.02, balance=0):
        self.accounts[account_name] = BankAccount(int_rate, balance)
        return self
            
    def make_deposit(self,account_name, amount):
        self.accounts[account_name].deposit(amount)
        return self
        
    def make_withdrawal(self,account_name, amount):
        self.accounts[account_name].withdraw(amount)
        return self
        
    def transfer_money(self, from_account, other_user, to_account, amount):
        if(amount > self.accounts[from_account].balance):
            print('No enough balance for this transfer!!')
        else:
            self.accounts[from_account].balance -= amount
            other_user.accounts[to_account].balance += amount
        return self
        
    def display_user_balance(self, account_name):
        print(f'User: {self.name}, Balance: ${self.accounts[account_name].balance}')
        return self
       


user1 = User("Mahmoud", "mahmoud@mail.com")
user2 = User("Ali", "ali@mail.com")

user1.add_account("checking", 0.02, 100)
user1.add_account("savings", 0.05, 500)

user2.add_account("checking", 0.02, 50)

user1.make_deposit("checking", 50).make_withdrawal("savings", 100)

user1.transfer_money("checking", user2, "checking", 30)

user1.display_user_balance("checking")
user1.display_user_balance("savings")