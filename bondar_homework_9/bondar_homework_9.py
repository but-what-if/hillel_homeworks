import os
import re



# task authors.txt ###############################################################



# Читаем файл в список. Возвращает список
def read_file(filename):
    with open(filename, 'r') as file:
        file_list = [line.rstrip().strip() for line in file.readlines()]
        return file_list
file_authors_list = read_file('authors.txt')


# Выбираем из прочитанного файла строки, в которых есть рождение или смерть авторов. Возвращает список
def sort_words(fileinfo: list):
    critery = ['birthday,', 'death,', 'Birthday,', 'birthday -', 'death -', 'death', 'died']
    authors = []
    for item in fileinfo:
        word_exist = False
        critery_count = 0
        while not word_exist and critery_count < len(critery):
            if critery[critery_count] in item:
                authors.append(item)
                word_exist = True
            critery_count += 1
    return authors
words_sorted_authors_list = sort_words(file_authors_list)


# Вытягиваем из списка даты для форматирования. Возвращает список дат
def sort_date(authors_info_list: list):
    dates = []
    for item in authors_info_list:
        dates.append(item.split('-')[0].strip(' '))
    return dates
dates = sort_date(words_sorted_authors_list)


# Форматируем даты, убирая буквы с чисел. Список форматированных дат
def change_data(dates_list: list):
    formated_dates = []
    for item in dates_list:
        if not item[1].isdigit():
            item = item[0] + item[3:]
        else:
            item = item[:2] + item[4:]
        formated_dates.append(item)
    return formated_dates
formated_dates = change_data(dates)



# Вытягиваем имена со списка авторов. Список имен
def create_names_list(authors_info_list: list):
    add_list = []
    for item in authors_info_list:
        add_list.append(item.split("'s"))
    names = [item[0].split('-')[1].strip() for item in add_list]
    for item in names:
        if len(item) > 30:
            f = item.split(" d")
            names[names.index(item)] = f[0]
    return names
names = create_names_list(words_sorted_authors_list)


def turn_month_into_number(month: str):
    month_dict = {'January': '01',
                 'February': '02',
                 'March': '03',
                 'April': '04',
                 'May': '05',
                 'June': '06',
                 'July': '07',
                 'August': '08',
                 'September': '09',
                 'October': '10',
                 'November': '11',
                 'December': '12'}
    return month_dict[f'{month}']

# task 2 - Возвращаем словарь ИМЯ: ДАТА для каждой строки


# Соединяем списки имен и даты. Возвращает список длинной 120

def chain_list(names: list, dates: list):
    names_dates = []
    for i in range(0, len(names)):
        names_dates.append(names[i])
        names_dates.append(dates[i])
    return names_dates
names_dates = chain_list(names, formated_dates)


# Создаем словари для каждой "строки". Возвращает словарь

def create_authors_dict(names_dates_list: list):
    for i in range(len(names_dates_list)):
        authors_dict = {'name': '', 'date': ''}
        if i % 2 != 0:
            date = names_dates_list[i]
            authors_dict['date'] = f'{date.split(" ")[0]}/{turn_month_into_number(date.split(" ")[1])}/{date.split(" ")[2]}'
        else:
            name = names_dates_list[i]
            authors_dict['name'] = name
    return authors_dict
authors_dict = create_authors_dict(names_dates)
print(authors_dict)



# dict.setdefault('name', name)
#             dict.setdefault('date', date.split(" ")[0] + '/' + turn_month_into_number(date.split(" ")[1]) + '/' + date.split(" ")[2])
