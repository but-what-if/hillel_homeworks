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

def change_data(dates_list: list):
    list_dates = []
    formated_dates = []
    for item in dates_list:
        if not item[1].isdigit():
            item = item[0] + item[3:]
        else:
            item = item[:2] + item[4:]
        list_dates.append(item)
    for date in list_dates:
        formated_dates.append(f'{date.split(" ")[0]}/{turn_month_into_number(date.split(" ")[1])}/{date.split(" ")[2]}')

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


# task 2 - Возвращаем словарь ИМЯ: ДАТА для каждой строки

def sort_authors_list_with_dates(names: list, dates: list):
    names_dates = sorted([f'{i}-{j}' for i, j in zip(names, dates)])
    return names_dates
authors_list_with_dates = sort_authors_list_with_dates(names, formated_dates)


def create_authors_dicts(sorted_names_dates_list: list):
    names_dates_1 = []
    for item in sorted_names_dates_list:
        names_dates_1.append(item.split('-'))
        for i in range(len(names_dates_1)):
            authors_dict_list = dict(name=names_dates_1[i][0], date=names_dates_1[i][1])
            return authors_dict_list
authors_dicts = create_authors_dicts(authors_list_with_dates)



# task 3 - Возвращаем список словарей ИМЯ: ДАТА для каждой строки

# Создаем список словарей для каждой "строки". Возвращает список

def create_authors_dict_list(names: list, dates: list):
    authors_dict_list = [dict(name=name, date=date) for name, date in zip(names, dates)]
    return authors_dict_list
authors_dict_list = create_authors_dict_list(names, formated_dates)



# task 4 - Создать список словарей автор: рождение: смерть:


def create_final_dict(authors_dict_list):
    res = [{"name": authors_dict_list[0]["name"], "date": []}]
    authors_dict_list.sort(key=lambda x: int(x["date"][-4:]))
    for dict_ in authors_dict_list:
        for i in range(len(res)):
            if res[i]["name"] == dict_["name"]:
                res[i]["date"].append(dict_["date"])
                break
        else:
            res.append({"name": dict_["name"], "date": [dict_["date"]]})
    final_authors_dict = []
    for dict_ in res:
        final_authors_dict.append({})
        final_authors_dict[-1]["name"] = dict_["name"]
        final_authors_dict[-1]["birth_date"] = dict_["date"][0]
        if len(dict_["date"]) > 1:
            final_authors_dict[-1]["dead_date"] = dict_["date"][1]
    return final_authors_dict
print(create_final_dict(authors_dict_list))

