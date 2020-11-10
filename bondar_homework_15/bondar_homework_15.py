import json
import csv

path = 'authors.json'

# Читаем файл

def read_json_file(filename_with_path):
    with open(filename_with_path) as json_file:
        return json.load(json_file)


data = read_json_file(path)


# Сортируем авторов по фамилии


def sort_authors(dict_: dict):
    return dict_["last_name"].strip().split(" ")[-1]


data = sorted(data, key=sort_authors)


# Записываем csv файл


def write_csv(datafile, filename_with_path):
    fieldsnames = list(datafile[0].keys())
    with open(filename_with_path, 'w') as outfile:
        csvwriter = csv.DictWriter(outfile, fieldnames=fieldsnames, delimiter=';')
        csvwriter.writeheader()
        csvwriter.writerows(datafile)


csv_writer = write_csv(data, 'authors_XX_France.csv')