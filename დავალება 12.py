print('#1')
#1
while True:
    try:
     first = input('პირველი რიცხვი: ')
     second = input('მეორე რიცხვი: ')
     answer = int(first)/int(second)
     print(answer)
     break
    except ZeroDivisionError:
     print("'ვერ გაგიყოფ ნულზე' - უთქვამს არისტოტელეს   \nთავიდან")
    except ValueError:
        print('თავიდაააააააააან')

print('#2')
#2
def two_number(first_num, second_num):
    try:
        first_num = int(first_num)
        second_num = int(second_num)
        if first_num % second_num == 0:
            print(first_num // second_num)
        else:
            print('naaah, არ იყოფა')
    except ValueError:
        print('nah,  რიცხვები მარტო')
    except ZeroDivisionError:
        print('naah, ნულზე ვერა')

two_number(input('first_num: '), input('second_num: '))

print('#3')
#3
list_mine = ['წყალს','ნაფოტი','ჩამოჰქონდა']
try:
 print(list_mine[3])
except IndexError:
    print('ჯერ ალვის არა')


print('#4')
#4
try:
 hey = open('myresult.txt')
 hey.close()
except FileNotFoundError:
    print('არ არსებობს ეს ფაილი')

print('#5')
#5
from math import sqrt
try:
    print('ax² + bx + c = 0')
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    D = (b**2) - (4 * a * c)
    if D < 0:
        print('ფესვები არა გვაქვს')
    elif D == 0:
        x1 = int((-b - sqrt(D)) / (2 * a))
        print('მარტო ერთი ფესვი გვაქვს',x1)
    else:
        x1 = int((-b - sqrt(D)) / (2 * a))
        x2 = int((-b + sqrt(D)) / (2 * a))
        print('აი ფესვები:',x1,'და',x2)
except ZeroDivisionError:
      print('შენი a ნულია, ნულზე გაყოფა no')
except ValueError:
    print('რიცხვები მხოლოდ')

print('#6')
#6
condition = 'ნებისმიერი ორი გვერდის სიგრძის ჯამი მესამე გვერდის სიგრძეზე მეტია'
try:
    num1 = int(input('პირველი: '))
    num2 = int(input('მეორე: '))
    num3 = int(input('მესამე: '))
    arithmetic_average = (num1 + num2 + num3) / 3
    if num1 + num2 > num3 and num2 + num3 > num1 and num1 + num3 > num2:
        print(arithmetic_average)
    else:
        raise ValueError
except:
   print('ეგ სამკუთხედი არაა')