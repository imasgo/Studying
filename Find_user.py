user_list = ['Вася','Маша','Петя','Валера','Саша','Даша']
i=0
flag = False
while flag == False:
    name_in_list = user_list[i]
    if name_in_list == 'Валера':
        print('Валера нашелся')
        flag = True
    i+=1

def find_person(name):
    for i in user_list:
        if i == name:
            print(name + ' нашелся')


print(find_person('Маша'))

def ask_user():
    flag = False
    while not flag:
        user_ansewer = input('Как дела?')
        user_ansewer=user_ansewer.lower()
        if user_ansewer == 'хорошо':
            flag = True




def ask_user():
        flag = False
        while flag == False:
            user_ansewer = input('Как дела?')
            user_ansewer = user_ansewer.lower()
            if user_ansewer == 'хорошо':
                flag = True
    # except KeyboardInterrupt:
    #     return "Пока!"
    # except:
    #     print(111)


try:
    ask_user()
except:
    print(111)
