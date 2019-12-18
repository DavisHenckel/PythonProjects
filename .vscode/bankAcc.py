#Object Oriented Programming Challenge
#For this challenge, create a bank account class that has two attributes:

#owner
#balance
#and two methods:

#deposit
#withdraw
#As an added requirement, withdrawals may not exceed the available balance.

#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn. 


class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return("Account Owner: {}\nAccount Balance: {}\n".format(self.owner, self.balance))

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful.Balance is now {}".format(self.balance))
    
    def withdraw(self, amount):
        if (amount >= self.balance):
            print("Insufficient Funds!")
        else:
            self.balance -= amount
            print("Withdraw successful. Balance is now {}".format(self.balance))






#Main
# 1. Instantiate the class
acct1 = Account('Jose',100)

# 2. Print the object
print(acct1)
# 3. Show the account owner attribute
acct1.owner
# 4. Show the account balance attribute
acct1.balance

# 5. Make a series of deposits and withdrawals
acct1.deposit(100)

acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)