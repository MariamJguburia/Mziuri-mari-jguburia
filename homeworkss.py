# 1
ff_text = "'If you truly love nature, you will find beauty everywhere'"
with open('ff.txt', 'w') as hola:
    hola.write(ff_text)
# 2
count = 0
with open('ff.txt', 'r') as f_file:
    for i in f_file:
        count += len(i)
        print(i)
        print('Numbers of symbols: ',count)
# 3
with open('ff.txt', 'a') as ffile:
    ffile.write(' - Vincent Van Gogh')
# # 4
with open('ff.txt','r', encoding='utf-8') as hehe, open('NewFile.txt','w', encoding='utf-8') as hihi:
    con = hehe.read()
    hihi.write(con)

#5
with open('NewFile.txt','r', encoding='utf-8') as f1:
    con1 = f1.read()
with open('ff.txt','r', encoding='utf-8') as f2:
    con2 = f2.read()
with open('both.txt','w', encoding='utf-8') as f3:
    f3.write(con1 + con2)

#6
with open('ff.txt', 'r') as new_file:
    for i in new_file:
        print(i.upper())

#7
texti = input('შეიყვანეთ(0 = დასრულება ☻ ): ')
with open('data.txt', 'w') as file:
    while texti != '0':
        file.write(texti)
        texti = input()

#8

