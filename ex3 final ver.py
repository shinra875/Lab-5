'''каждый логический блок код отделен от других тремя строками. логические блоки имеют свое краткое описание'''

'''импортируем библиотеку re для работы с регулярками, библиотеку csv для создания и сохранения csv таблицы'''
import re
import csv



'''набор списков, которые понадобятся для задачи. часть списков будут выполнять функцию времнного буфера'''
ID_list = []  # 250 высчитывалось в отдельном блоке
lastname_list = []  # 250 высчитывалось в отдельном блоке

regdate_list = []  # 250 через Ctrl + F и маску \d{4}-\d{1,2}-\d{1,2}
site_list = []  # 250 через Ctrl + F и маску http[s]?://[a-zA-Z.-]+/
email_list = []  # 250 [a-zA-Z0-9-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-]+



'''блок, где мы отделяем те элементы, которые легко определить по формату(даты, мыло, сайты)
с айди и фамилиями сложнее, об этом в следующем блоке'''
with open('task3.txt') as file:
    for string in file: # одна единственная строка всего файла. перенесли ее из txt файла в отдельную перем
        site_list.append(re.findall(r'http[s]?://[a-zA-Z.-]+/', string))
        regdate_list.append(re.findall(r'\d{4}-\d{1,2}-\d{1,2}', string))
        email_list.append(re.findall(r'[a-zA-Z0-9-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-]+', string))
        
        list_of_all = [x for x in string.split()]  # возвращает список строк со ВСЕМИ элементами
    
    
    print(email_list)
    # убираем вложенность
    email_list = [*email_list[0]]
    regdate_list = [*regdate_list[0]]
    site_list = [*site_list[0]]
    print(email_list)


    '''блок выделения айди'''
    for i in list_of_all:
        if i.isdigit():
            ID_list.append(i)



    '''блок выделения фамилий'''
    for i in list_of_all:
        if not (i in email_list) and not (i in regdate_list) and not (i in site_list) and not (i.isdigit()):
            lastname_list.append(i)



'''поиндексное чтение данных каждого пользователя'''
rows = []
for user_index in range(0,len(list_of_all)//5):  
    '''тут можно было бы написать 250, но я решил все расписать. 
    у нас есть файл с опред кол-вом данных от конкретного числа пользователей. 
    всего элементов len(list_of_all), каждый пользователей вводил 5 элементов. 
    следовательно, пользователей было len(list_of_all)/5'''
    
    # print([ID_list[user_index], lastname_list[user_index], email_list[user_index], regdate_list[user_index], site_list[user_index]])
    # строку выше можно раскомментировать, чтобы увидеть, как строки будут заноситься в csv таблицу
    
    rows.append([ID_list[user_index], lastname_list[user_index], email_list[user_index], regdate_list[user_index], site_list[user_index]])



'''перенос всего в csv таблицу'''
fields = ['ID', 'Lastname', 'Email', 'Date of registration', 'Site']

with open('CSV table file.csv','w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(rows)