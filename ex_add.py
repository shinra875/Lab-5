import re

def anti_spaces(mass):
    new_list = []
    for iter in mass:
        if len(iter)>0:
            new_list.append(iter)
    return new_list

def norm_vid(mass):
    norm_vid_list = []
    mass = anti_spaces(mass)
    for iter in mass:
        norm_vid_list.append(*iter)
    return norm_vid_list



date_list = []  # 5 дат через Ctrl + F и маску \s+[0-9]{1,4}[-./][0-9]{1,4}[-./][0-9]{1,4}
email_list = []  # 5 адресов через Ctrl + F и маску \s[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
site_list = []  # 5 сайтов через Ctrl + F и маску \s{1}http[s]?://[0-9a-zA-Z.-]+


with open('task_add.txt', encoding='utf-8') as file:
    for string in file:
        date_list.append(re.findall(r'\s{1}[0-9]{1,4}[-./][0-9]{1,4}[-./][0-9]{1,4}', string))
        email_list.append(re.findall(r'\s[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', string))
        site_list.append(re.findall(r'\s{1}http[s]?://[0-9a-zA-Z.-]+', string))

print(f'колво дат = {len(norm_vid(date_list))} список: {norm_vid(date_list)}')
print(f'колво адресов почты = {len(norm_vid(email_list))} список: {norm_vid(email_list)}')
print(f'колво сайтов = {len(norm_vid(site_list))} список: {norm_vid(site_list)}')