# #1
# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self,amount):
#         if amount > 2500:
#             print('რაამბავია, ეგ არ გამოვა')
#         else:
#             self.balance += amount
#     def withdraw(self,amount):
#         if amount > self.balance :
#             print('მაგდენი არ გაქვთ')
#         else:
#             self.balance -= amount
#     def display_balance(self):
#         print('შენი ბალანსი: 'f'{self.balance}')
# owner = input('თქვენი სახელი: ')
# print(f'{owner}, ხელმისაწვდომია: 1000.00')
# objectt = BankAccount(owner, 1000)
# objectt.deposit(int(input('შესატანი თანხა: ')))
# objectt.withdraw(int(input('გამოსატანი თანხა: ')))
# objectt.display_balance()

#2
class Shape:
    def describe(self):
        print('i am a shape')

class Polygon(Shape):
    def __init__(self,sides,color):
        self.color = color
        self.sides = sides

class Triangle(Polygon):
    def __init__(self,h,u,j):
        self.h = h
        self.u = u
        self.j = j
    def calculate_area(self):
        heron = (self.h + self.u + self.j) / 2
        return heron
obj_triangle = Triangle(4,8,8)
print(obj_triangle.calculate_area())