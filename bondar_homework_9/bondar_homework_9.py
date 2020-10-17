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
    add_list = ['st', 'nd', 'rd', 'th']
    for item in dates_list:
        end_exist = False
        end_count = 0
        while not end_exist and end_count < len(add_list):
            if add_list[end_count] in item:
                formated_dates.append(re.sub(add_list[end_count], '', item))
                end_exist = True
            end_count += 1
    return formated_dates
formated_dates = change_data(dates)


# Вытягиваем имена со списка авторов. Список имен
def create_names_list(authors_info_list: list):
    add_list = [item.split("'s") for item in authors_info_list]
    names = [item[0].split('-')[1].strip() for item in add_list]
    return names
names = create_names_list(words_sorted_authors_list)

