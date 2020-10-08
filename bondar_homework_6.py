# # task 1 ###############################################
#
# my_list = ['qwe', 'qwe', 'qwe', 'qwe', 'qwe']
# new_list = []
# for index, value in enumerate(my_list):
#     if index % 2 == 0:
#         new_list.append(value)
#     else:
#         new_list.append(value[::-1])
# print(new_list)
#
#
#
# # task 2 ##############################################
#
# my_list = ['qwe', 'asd', 'fgh', 'aer', 'aty', 'uty']
# new_list = [value for value in my_list if value[0] == 'a']
# print(new_list)
#
#
#
# # task 3 ##############################################
#
# my_list = ['qwe', 'asd', 'fgah', 'aer', 'aty', 'uty']
# new_list = [value for value in my_list if 'a' in value]
# print(new_list)
#
#
#
# # task 4 ##############################################
#
# my_list = ['qwe', 765, 'fgah', 1954, 'aty', -8]
# new_list = [value for value in my_list if type(value) == str]
# print(new_list)
#
#
#
# # task 5 ##############################################
#
# my_str = 'blablacar'
# new_list = [sym for sym in my_str if my_str.count(sym) == 1]
# print(new_list)
#
#
# # task 6 ##############################################
#
# my_str_1 = 'aabcddet'
# my_str_2 = 'test'
# new_list = list(set(my_str_1).intersection(set(my_str_2)))
# print(new_list)
#
#
# # task 7 ##############################################
#
# my_str_1 = 'aabcddet'
# my_str_2 = 'test'
# my_set_1 = set(sym for sym in my_str_1 if my_str_1.count(sym) == 1)
# my_set_2 = set(sym for sym in my_str_2 if my_str_2.count(sym) == 1)
# new_list = list(my_set_1.intersection(my_set_2))
# print(new_list)
#
#
#
# # task 8 ##############################################
#
# person = {'Фамилия': 'Бондарь',
#           'Имя': 'Вова',
#           'Возраст': 26,
#           'Проживание': {
#               'Страна': 'Украина',
#               'Город': 'Днепр',
#               'Улица': 'Гагарина'
#           },
#           'Работа': {
#               'Наличие': True,
#               'Должность': 'Инженер'
#           },
# }
# print(person['Работа']['Наличие'])
#
#
# # task 9 #############################################
#
# cakes = {
#     'Мука': 400,
#     'Молоко': 200,
#     'Масло': 200,
#     'Яйцо': 2
# }
# cream = {
#     'Сахар': 500,
#     'Масло': 200,
#     'Ваниль': 30,
#     'Сметана': 500
# }
# glaze = {
#     'Какао': 100,
#     'Сахар': 100,
#     'Масло': 100,
# }
#
# fake_cake = {
#     'Коржи': cakes,
#     'Крем': cream,
#     'Глазурь': glaze,
# }
#
# print(fake_cake['Коржи']['Молоко'])