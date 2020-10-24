import json
import requests
import csv

# task 1 ##################################################


path = 'data.json'


def read_json_file(filename_with_path):
    with open(filename_with_path, encoding='utf-8') as json_file:
        return json.load(json_file)


data = read_json_file(path)


def get_rows(data_list):
    for row in data_list:
        return row


def sort_surnames(dict_: dict):
    name = dict_["name"].split(" ")[-1]
    return name


sorted_surnames_list = sorted(data, key=sort_surnames)


def sort_death_date(dict_: dict):
    year = dict_["years"].split("–")[1]
    year = year.replace('c. ', '').replace('.', '')
    if len(year.strip('.').split()) == 1:
        return int(year.split()[0][:-1])
    return -int(year.split(" ")[-2])


sorted_death_date_list = sorted(data, key=sort_death_date)


def sort_text(dict_: dict):
    text = dict_["text"].split(" ")
    return len(text)


sorted_text_list = sorted(data, key=sort_text)


# task 2 ########################################################


url = 'https://api.forismatic.com/api/1.0/'


def get_response(url):
    res = requests.get(url, params={'method': 'getQuote', 'lang': 'ru', 'format': 'json'})
    return res


# quote = [res.json() for i in range(100) if res.json()['quoteAuthor'] != '']


i = 1
quote = []
while i <= 100:
    res = get_response(url)
    if (res.json()['quoteAuthor'] != '') and (res.json() not in quote):
        quote.append(res.json())
        i += 1


def write_json(data, filename_with_path, encoding='utf-8'):
    with open(filename_with_path, 'w', encoding=encoding) as outfile:
        json.dump(data, outfile, indent=2, ensure_ascii=False)


quote_data = write_json(quote, 'quotes.json')


def sort_authors(dict_: dict):
    name = dict_["quoteAuthor"].split(" ")[-1]
    return name

def write_csv(data, filename_with_path, encoding='utf-8'):
    fieldnames = ['Автор', 'Цитата', 'Ссылка']
    with open(filename_with_path, 'w', encoding=encoding) as outfile:
        csvwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
        csvwriter.writeheader()
        csvwriter.writerows(data)