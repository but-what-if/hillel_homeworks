import json


def read_json_file(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        print(data, type(data))


read_json_file('data.json')