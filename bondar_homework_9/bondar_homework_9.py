import os
import re



# task authors.txt ###############################################################


# def read_file(filename):
#     with open(filename, 'r') as file:
#         file_list = [line.rstrip().strip() for line in file.readlines()]
#         critery = ['birthday,', 'death,', 'Birthday,', 'birthday -', 'death -', 'death', 'died']
#         authors = []
#         for item in file_list:
#             for _ in critery:
#                 if _ in item:
#                     authors.append(item)
#         for item in authors:
#             items = item.split('-')
#             print(items)
#         # return authors
# read_file('authors.txt')


def read_file(filename):
    with open(filename, 'r') as file:
        file_list = [line.rstrip().strip() for line in file.readlines()]
        return file_list


# read_file('authors.txt')

def sort_words(function):
    critery = ['birthday,', 'death,', 'Birthday,', 'birthday -', 'death -', 'death', 'died']
    authors = []
    for item in function:
        for _ in critery:
            if _ in item:
                authors.append(item)
    return authors

def sort_date(function):
    # items = []
    dates = []
    for item in function:
        item.split('-')
        dates.append(item.split('-')[0].strip(' '))
    return dates
sort_date(sort_words(read_file('authors.txt')))

def change_data(function):
    new_dates = []
    add_list = ['st', 'nd', 'rd', 'th']
    for item in function:
        for i in add_list:
            new_dates.append(re.sub(i, '', item))
    print(new_dates)

change_data(sort_date(sort_words(read_file('authors.txt'))))

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




