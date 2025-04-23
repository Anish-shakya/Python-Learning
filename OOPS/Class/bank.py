class BankAccount():
    bank_name = 'Standard Chartered Bank'
    
    def __init__(self,account_holder,account_no,account_type,balance=0.0):
        self.account_holder=account_holder
        self.account_number = account_no
        self.account_type = account_type
        self.balance = balance
        self.statement = []
        
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.statement.append(f'Deposited Rs.{amount}')
        else:
            print('Deposited amount cannot be less than 0')
    
    def withdrawal(self,amount):
        if amount < 0:
            print('Withdrawal amount must be greater than 0')
        elif amount <= self.balance:
            self.balance -= amount
            self.statement.append(f'Withdrawal Rs.{amount}')
        else:
            print('Insufficent Fund')
        
    def transaction(self,beneficiary,amount):
        if amount <= self.balance:
            self.withdrawal(amount)
            beneficiary.deposit(amount)
            self.statement.pop()
            self.statement.append(f"Transferred Rs.{amount} to {beneficiary.account_holder}")
            beneficiary.statement.pop()
            beneficiary.statement.append(f"Received Rs.{amount} from {self.account_holder}")
        else:
            print("Insufficient funds for transfer.")
            
    
    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return (f'-----------------------------------\n'
                f'-----{BankAccount.bank_name}------\n'
                f'Account Holder : {self.account_holder}\n'
                f'Account Number: {self.account_number}\n'
                f'Account Type: {self.account_type}\n'
                f'Bank Balance: Rs.{self.balance:.2f}\n'
                f'Statement: {self.statement}')
               
customer1 = BankAccount('Alice','123456789','Current Account')

customer2= BankAccount('Bob','987654321','Saving Account')

print(customer1)
print(customer2)

customer1.deposit(100000)
customer1.withdrawal(2000)

customer1.transaction(customer2,5000)
customer1.transaction(customer2,20000)


customer2.deposit(75000)
customer1.deposit(27000)

customer1.withdrawal(75000)
customer2.withdrawal(50000)

customer2.transaction(customer1,12500)

print(customer1)
print(customer2)