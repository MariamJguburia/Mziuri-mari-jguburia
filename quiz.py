with open('titanic.txt','r') as titanic1:
    titanic = titanic1.read(int(79))
    print(titanic)
    # hey = titanic.read()
    # print(hey)
    count_yall = []
    fem = []
    mal =[]
    fem_survived = []
    fem_did_not_survived = []
    mal_survived = []
    mal_did_not_survived = []
    fem_per = []
    fem_sur_per = []
    fem_did_not_sur_per = []
    mal_per = []
    mal_sur_per = []
    mal_did_not_sur_per = []
    all_ticket = []
    first_class_ppl = []
    second_class_ppl = []
    third_class_ppl = []
    first_class_ppl_per = []
    second_class_ppl_per = []
    third_class_ppl_per = []
    for i in titanic:
        data = i.strip().split(",")
        name = data[5].split(" ")
        for ii in titanic:
            count_yall += 1
        if data[4] == "female":
            fem += 1
            fem_per = fem * 100 / count_yall #qalebis %
            if data[2] == 1:
                fem_survived += 1
                fem_sur_per = fem_sur_per * 100 / fem # gadar qalebis %
            elif data[2] == 0:
                fem_did_not_survived += 1
                fem_did_not_sur_per = fem_did_not_sur_per * 100 / fem # ver gadar qalebi %

        else:
            mal += 1
            mal_per = mal * 100 / count_yall
            if data[2] == 1:
                mal_survived += 1
                mal_survived_per = mal_survived * 100 / mal
            else:
                mal_did_not_survived +=1
                mal_did_not_survived_per = mal_did_not_survived * 100 / mal

        for i in data[3]:
            all_ticket +=1
        if data[3] == 1:
            first_class_ppl += 1
            first_class_ppl_per = first_class_ppl * 100 / all_ticket
        elif data[3] == 2:
            second_class_ppl += 1
            second_class_ppl_per = second_class_ppl * 100 / all_ticket
        else:
            third_class_ppl += 1
            third_class_ppl_per = third_class_ppl * 100 / all_ticket

        average = []
        av_count = []
        for fare in data[10]:
            av_count +=1
            average += fare
            print(average/av_count)


#სავარჯიშოები
#1
# r - წაკითხვის
# w - ჩაწერის
# a - ჩამატების
# a+ - წაკითხვა და ჩამატება
# r+ - წაკითხვა და ჩაწერა
#2
# ახალი შეიქმნება
#3
#არ გვაქვს ინდექსები, ფრჩხილები განსხვავდება
#4
#Key
