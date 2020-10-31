import random
import string
import json
import csv


class FileWriter():

    def __init__(self, filename, file_data=None):
        self.filename = filename
        self.file_data = file_data if file_data is not None else self._create_data()

    def _generate_random_string(self):
        new_random_list = []
        last_random_str = (''.join(random.choice(' ' + string.digits + ' ' + random.choice(
            [' ', '.', ',', ';', '...', '-', '"', '(', ')', '?', '!']) + ' ' + string.ascii_letters) for i in range(100)))
        for i in range(9):
            random_str = (''.join(random.choice(string.ascii_letters + ' ' + string.digits + ' ' + random.choice(
                [' ', '.', ',', ';', '...', '-', '"', '(', ')', '?', '!']) + ' ') for i in range(100)))
            new_random_list.append(random_str + '\n')
        new_random_list.append(last_random_str)
        random_string = ''.join(new_random_list)
        return random_string

    def _generate_random_dict(self):
        keys_list = [(''.join(random.choice(string.ascii_lowercase) for i in range(5))) for i in range(random.randint(5, 20))]
        values_list = random.choices([random.randint(-100, 100), True, False, random.uniform(0, 1)], k=len(keys_list))
        random_dict = dict((key, value) for key, value in zip(keys_list, values_list))
        return random_dict

    def _generate_random_table(self):
        n = random.randint(3, 10)
        m = random.randint(3, 10)
        random_table = [[random.choice([0, 1]) for i in range(m)] for i in range(n)]
        return random_table

    def _create_data(self):
        file_extansion = self.filename.rsplit('.')[-1]
        if file_extansion == 'txt':
            self.file_data = self._generate_random_string()
        elif file_extansion == 'json':
            self.file_data = self._generate_random_dict()
        elif file_extansion == 'csv':
            self.file_data = self._generate_random_table()
        else:
            raise Exception('Unsupported file format!')
        return self.file_data

    def _write_txt(self):
        with open(self.filename, 'w') as txtfile:
            txtfile.write(self.file_data)

    def _write_json(self):
        with open(self.filename, 'w') as jsonfile:
            json.dump(self.file_data, jsonfile, indent=4)

    def _write_csv(self):
        with open(self.filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=";", lineterminator='\n')
            csvwriter.writerows(self.file_data)

    def write(self):
        file_extansion = self.filename.rsplit('.')[-1]
        if file_extansion == 'txt':
            data = self._write_txt()
        elif file_extansion == 'json':
            data = self._write_json()
        elif file_extansion == 'csv':
            data = self._write_csv()
        else:
            raise Exception('Unsupported file format!')
        return data

test_str = 'It is a string for testing'
txt_writer = FileWriter('test.txt', file_data=None)
txt_writer.write()

test_dict = {'name': 'Vova', 'age': 26}
json_writer = FileWriter('test.json', file_data=None)
json_writer.write()

test_table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
csv_writer = FileWriter('test.csv', file_data=None)
csv_writer.write()