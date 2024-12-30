import re

def count_func(mass):
    for line in mass:
        if len(line)>0:
            for necessary_line in line:
                total_list.append(necessary_line)
    return total_list

pixel_count = []
total_list = []

string = open('task2.html', "r", encoding='utf-8')
for line in string:
    pixel_count.append(re.findall(r'\d+px', line))

count_func(pixel_count)
print(f'Всего элементов {len(total_list)} штук \nСписок элементов: \n{total_list}')