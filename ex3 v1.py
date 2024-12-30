import re

ID_list = []  # 250 высчитывалось в отдельном блоке
lastname_list = []  # 250 высчитывалось в отдельном блоке

regdate_list = []  # 250 через Ctrl + F и маску \d{4}-\d{1,2}-\d{1,2}
site_list = []  # 250 через Ctrl + F и маску http[s]?://[a-zA-Z.-]+/
email_list = []  # 250 [a-zA-Z0-9-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-]+

total_without_email = []
total_without_date = []
total_without_site = []

with open('task3.txt') as file:
    for string in file: # одна единственная строка всего файла. перенесли ее из txt файла в отдельную перем
        site_list.append(re.findall(r'http[s]?://[a-zA-Z.-]+/', string))
        regdate_list.append(re.findall(r'\d{4}-\d{1,2}-\d{1,2}', string))
        email_list.append(re.findall(r'[a-zA-Z0-9-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-]+', string))
        list_of_all = [x for x in string.split()]  # возвращает список строк со ВСЕМИ элементами
        total_without_email.append(re.sub(r'[a-zA-Z0-9-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-]+', " ", string))


'''блок, где мы последовательно убираем лишние элементы (мыло, сайты, даты). 
Вероятно, это можно было сделать проще. но за ночь и утро я не придумал лучше варианта, 
как последовательно пройтись и удалить каждую группу'''

for without_email_iter in total_without_email:
    total_without_date.append(re.sub(r'\d{4}-\d{1,2}-\d{1,2}', " ", without_email_iter))
for without_date_iter in total_without_date:
    total_without_site.append(re.sub(r'http[s]?://[a-zA-Z.-]+/', " ", without_date_iter))
for without_site_iter in total_without_site:
    t = without_site_iter.split()
    
    for i in t:
        if i.isdigit():
            ID_list.append(i)
        else:
            lastname_list.append(i)

    for regdate in regdate_list:
        pass
    for email in email_list:
        pass
    for site in site_list:
        pass


    for i in range(0,250):
        print(ID_list[i], lastname_list[i], email[i], regdate[i], site[i])



import csv


# field names 
fields = ['Name', 'Branch', 'Year', 'CGPA'] 

# data rows of csv file 
rows = [ ['Nikhil', 'COE', '2', '9.0'], 
		['Sanchit', 'COE', '2', '9.1'], 
		['Aditya', 'IT', '2', '9.3'], 
		['Sagar', 'SE', '1', '9.5'], 
		['Prateek', 'MCE', '3', '7.8'], 
		['Sahil', 'EP', '2', '9.1']] 

with open('test csv', 'w') as f:
	
	# using csv.writer method from CSV package
	write = csv.writer(f)
	
	write.writerow(fields)
	write.writerows(rows)
