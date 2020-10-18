import random
import json
import csv
import string


# Generate data for writting txt file - task 1 #############################################

def generate_string():
    new_random_list = []
    last_random_str = (''.join(random.choice(' ' + string.digits + ' ' + random.choice(
        [' ', '.', ',', ';', '...', '-', '"', '(', ')', '?', '!']) + ' ' + string.ascii_letters) for i in range(100)))
    for i in range(9):
        random_str = (''.join(random.choice(string.ascii_letters + ' ' + string.digits + ' ' + random.choice([' ', '.', ',', ';', '...', '-', '"', '(', ')', '?', '!']) + ' ') for i in range(100)))
        new_random_list.append(random_str + '\n')
    new_random_list.append(last_random_str)
    random_string = ''.join(new_random_list)
    return random_string
random_string = generate_string()



def write_txt_file(data, filename_with_path='test.txt'):
    with open(filename_with_path, 'w') as txtfile:
        txtfile.write(data)
    return txtfile
write_txt_file(random_string)



# Generate data for writting json file - task 2 #############################################

def generate_dict():
    keys_list = [(''.join(random.choice(string.ascii_lowercase) for i in range(5))) for i in range(random.randint(5, 20))]
    values_list = random.choices([random.randint(-100, 100), True, False, random.uniform(0, 1)], k=len(keys_list))
    random_dict = dict((key, value) for key, value in zip(keys_list, values_list))
    return random_dict
random_dict = generate_dict()


def write_json_file(data, filename_with_path='test.json'):
    with open(filename_with_path, 'w') as jsonfile:
        jsonwriter = json.dump(data, jsonfile, indent=4)
    return jsonwriter
write_json_file(random_dict)



# Generate data for writting csv file - task 3 #############################################


def generate_table():
    n = random.randint(3, 10)
    m = random.randint(3, 10)
    random_table = [[random.choice([0, 1]) for i in range(m)] for i in range(n)]
    return random_table
random_table = generate_table()


def write_csv_file(data, filename_with_path='test.csv'):
    with open(filename_with_path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=";", lineterminator='\n')
        csvwriter.writerows(data)
    return csvwriter
write_csv_file(random_table)



# File writer function - main task ######################################

def file_writer(filename_with_path):
    mode = filename_with_path.rsplit('.')[-1]
    if mode == 'txt':
        data = write_txt_file(random_string, filename_with_path)
    elif mode == 'json':
        data = write_json_file(random_dict, filename_with_path)
    elif mode == 'csv':
        data = write_csv_file(random_table, filename_with_path)
    else:
        raise Exception('Unsupported file format!')
    return data
file_writer('../gffddyyyyy.csv')