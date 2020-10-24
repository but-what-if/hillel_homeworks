import json
import requests
import csv

# task 1 ##################################################


path = 'data.json'

# Читаем файл

def read_json_file(filename_with_path):
    with open(filename_with_path, encoding='utf-8') as json_file:
        return json.load(json_file)


data = read_json_file(path)


def get_rows(data_list):
    for row in data_list:
        return row


# Сортировка по фамилии


def sort_surnames(dict_: dict):
    name = dict_["name"].split(" ")[-1]
    return name


sorted_surnames_list = sorted(data, key=sort_surnames)


# Сортировка по дате смерти


def sort_death_date(dict_: dict):
    year = dict_["years"].split("–")[1]
    year = year.replace('c. ', '').replace('.', '')
    if len(year.strip('.').split()) == 1:
        return int(year.split()[0][:-1])
    return -int(year.split(" ")[-2])


sorted_death_date_list = sorted(data, key=sort_death_date)


# Сортировка по количеству слов


def sort_text(dict_: dict):
    text = dict_["text"].split(" ")
    return len(text)


sorted_text_list = sorted(data, key=sort_text)


# task 2 ########################################################


url = 'https://api.forismatic.com/api/1.0/'


# Делаем запрос


def get_response(url):
    res = requests.get(url, params={'method': 'getQuote', 'lang': 'ru', 'format': 'json'})
    return res


# Формируем список из 100 цитат


i = 1
quote = []
while i <= 100:
    res = get_response(url)
    if (res.json()['quoteAuthor'] != '') and (res.json() not in quote):
        quote.append(res.json())
        i += 1


# Сортировка по фамилии автора


def sort_authors(dict_: dict):
    name = dict_["quoteAuthor"].strip().split(" ")[-1]
    return name


# Удаление лишних элементов со словарей списка


quote_list = []
for item in quote:
    d = {i:item[i] for i in item if (i != 'senderName') and (i != 'senderLink')}
    quote_list.append(d)


quote_list = sorted(quote_list, key=sort_authors)


# Замена наименований ключей словаря и перестановка элементов


sorted_quote_list = []
for item in quote_list:
    item['Цитата'] = item.pop('quoteText')
    item['Автор'] = item.pop('quoteAuthor')
    item['Ссылка'] = item.pop('quoteLink')
    item = {'Автор': item['Автор'], 'Цитата': item['Цитата'], 'Ссылка': item['Ссылка']}
    sorted_quote_list.append(item)


# Записываем json файл


def write_json(data, filename_with_path, encoding='utf-8'):
    with open(filename_with_path, 'w', encoding=encoding) as outfile:
        json.dump(data, outfile, indent=2, ensure_ascii=False)


quote_data = write_json(sorted_quote_list, 'quotes.json')


# Записываем csv файл


def write_csv(data, filename_with_path):
    fieldsnames = list(data[0].keys())
    with open(filename_with_path, 'w') as outfile:
        csvwriter = csv.DictWriter(outfile, fieldnames=fieldsnames, delimiter=';')
        csvwriter.writeheader()
        csvwriter.writerows(data)


csv_writer = write_csv(sorted_quote_list, 'quotes.csv')