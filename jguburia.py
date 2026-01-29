#1
with open('file.txt','r') as files:
    count = []
    for i in files:
        number = int(i.strip())
        count.append(number**2)
    print(count)

with open('squared numbers.txt', 'w') as output:
    for num in count:
        output.write(str(num) + '\n')


#2


age = []
name = []
with open('oscar.txt', 'r') as file:
    for line in file:
        parts = line.split(',')
        age.append(int(parts[2]))
        name.append(parts[3] + ' ' + parts[4])

minimum_age = min(age)
index = age.index(minimum_age)

print('\n','name, surname:', name[index])
print('age:', minimum_age)

with open('oscar.txt', 'r') as oscar_file:
    year= input('Year: ')
    for char in oscar_file:
        if year in char:
            print(char.strip())
