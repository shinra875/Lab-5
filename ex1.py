# Все слова, после которых стоит точка; все дробные числа.
import re

def count_func(mass):
    for line in mass:
        if len(line)>0:
            for necessary_line in line:
                total_list.append(necessary_line)
    return total_list

letters_mass = []
float_nums_mass = []
total_list = []

with open("task1-en.txt") as string:
    for line in string:
        letters_mass.append(re.findall(r'\w+\.', line))
        float_nums_mass.append(re.findall(r'\d+\.\d+', line))

count_func(letters_mass)
count_func(float_nums_mass)

print(f'Всего элементов {len(total_list)} штук \nСписок элементов: \n{total_list}')