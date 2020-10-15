import os



# 0-express ##############################################################

# def get_dir_items(path='./'):
#     list_dir = sorted(os.listdir(path))
#     dir_items = {'files': [],
#                 'folders': []
#                 }
#     for item in list_dir:
#         path_item = os.path.join(path, item)
#         if os.path.isfile(path_item):
#             dir_items['files'].append(item)
#         else:
#             dir_items['folders'].append(item)
#     print(dir_items)
#
#
# get_dir_items(path='../bondar_homework_9')


# task authors.txt ###############################################################


def read_file(filename):
    with open(filename, 'r') as file:
        file_list = [line.rstrip().strip() for line in file.readlines()]
        critery = ['birthday,', 'death,', 'Birthday,', 'birthday -', 'death -', 'death', 'died']
        authors = []
        items = []
        for item in file_list:
            for _ in critery:
                if _ in item and item[0].isdigit():
                    authors.append(item)
        print(authors)
        # return authors
read_file('authors.txt')

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

# def create_authors_dictionary(function):
#     # author = {'name': None, 'date': 'dd/mm/yyyy'}
#     for item in function('authors.txt'):
#         print(item.split(' '))
#
# create_authors_dictionary(read_file)





