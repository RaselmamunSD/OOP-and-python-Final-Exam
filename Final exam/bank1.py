class Bank:
    def __init__(self):
        self.accounts = {}
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature = True

    def create_account(self, account_number, initial_balance=0):
        if account_number in self.accounts:
            print("Account already exists ")
        else:
            self.accounts[account_number] = initial_balance
            self.total_balance += initial_balance
            print("Account created successfully ")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            self.total_balance += amount
            print("Deposit successful ")
        else:
            print("Account does not exist ")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                self.total_balance -= amount
                print("Withdrawal successful ")
            else:
                print("Insufficient balance ")
        else:
            print("Account does not exist ")


    def check_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account does not exist ")

    def transfer(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            if self.accounts[from_account] >= amount:
                self.accounts[from_account] -= amount
                self.accounts[to_account] += amount
                print("Transfer successful ")
            else:
                print("Insufficient balance ")
        else:
            print("One or both accounts do not exist ")

    def check_transaction_history(self, account_number):
        if account_number in self.accounts:
            
            print("Transaction history for account:", account_number)
        else:
            print("Account does not exist ")

    def take_loan(self, account_number):
        if self.loan_feature:
            if account_number in self.accounts:
                total_amount = self.accounts[account_number] * 2
                self.accounts[account_number] += total_amount
                self.total_balance += total_amount
                self.total_loan_amount += total_amount
                print("Loan of", total_amount, "taken successfully ")
            else:
                print("Account does not exist ")
        else:
            print("Loan feature is currently disabled ")

class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, account_number, initial_balance=0):
        self.bank.create_account(account_number, initial_balance)

    def check_total_balance(self):
        return self.bank.total_balance

    def check_total_loan_amount(self):
        return self.bank.total_loan_amount

    def toggle_loan_feature(self):
        self.bank.loan_feature = not self.bank.loan_feature



bank = Bank()
admin = Admin(bank)


bank.create_account("user1", 10000)
bank.deposit("user1", 1000)
bank.withdraw("user1", 3000)
balance = bank.check_balance("user1")
print("User1 balance:", balance)
bank.transfer("user1", "user2", 500)
bank.check_transaction_history("user1")
bank.take_loan("user1")


admin.create_account("user2", 2000)
total_balance = admin.check_total_balance()
print("Total balance:", total_balance)
total_loan_amount = admin.check_total_loan_amount()
print("Total loan amount:", total_loan_amount)
admin.toggle_loan_feature()
