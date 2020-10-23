import json

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





