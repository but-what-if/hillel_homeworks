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
        for _ in critery:
            if _ in item:
                authors.append(item)
    return authors
words_sorted_authors_list = sort_words(file_authors_list)


# Вытягиваем из списка даты для форматирования. Возвращает список дат
def sort_date(authors_info_list: list):
    dates = []
    for item in authors_info_list:
        item.split('-')
        dates.append(item.split('-')[0].strip(' '))
    return dates
dates = sort_date(words_sorted_authors_list)
print(dates)


