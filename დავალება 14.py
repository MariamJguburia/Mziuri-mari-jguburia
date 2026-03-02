#1
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        if amount > 2500:
            print('რაამბავია, ეგ არ გამოვა')
        else:
            self.balance += amount
    def withdraw(self,amount):
        if amount > self.balance :
            print('მაგდენი არ გაქვთ')
        else:
            self.balance -= amount
    def display_balance(self):
        print('შენი ბალანსი: 'f'{self.balance}')
owner = input('თქვენი სახელი: ')
print(f'{owner}, ხელმისაწვდომია: 1000.00')
objectt = BankAccount(owner, 1000)
objectt.deposit(int(input('შესატანი თანხა: ')))
objectt.withdraw(int(input('გამოსატანი თანხა: ')))
objectt.display_balance()

#2
