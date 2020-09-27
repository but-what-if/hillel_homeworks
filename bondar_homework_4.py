# task 1 ####################

my_list = [23, 65, 5, 678, 7, 120]
for value in my_list:
    if value > 100:
        print(value)


# task 2 ####################

my_list = [23, 65, 5, 678, 7, 120]
my_results = []
for value in my_list:
  if value > 100:
      my_results.append(value)
print(my_results)

# task 3 ####################

my_list = [23, 76, 454, 8, 2]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)

# task 4 ####################

value = input('Enter the number: ')
try:
    value = float(value)
    value = value ** -1
except ValueError:
    print('You entered incorrect value')
    value = None
except ZeroDivisionError:
    print('0 cannot be raised to a negative power')
    value = None
except:
    print('Something has gone wrong')
    value = None
print(value)

# task 5 ####################

my_list = [12, 123, 234, 345, 456]
my_indexes = [0, 1, 2, 3, 4]
for index in my_indexes:
    print(my_list[index])

# task 6 ####################

my_list_1 = ['01', '02', '03']
my_list_2 = ['January', 'February', 'March']
my_indexes = [0, 1, 2]
for index in my_indexes:
    print(f'({my_list_1[index]}-{my_list_2[index]})')

# task 7 ####################

my_string = '0123456789'
add_list = []
for sym_1 in my_string:
    for sym_2 in my_string:
        add_list.append(int(sym_1 + sym_2))
print(add_list, type(add_list[5]))

