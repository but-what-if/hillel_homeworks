# task 1 ##############################

number = 40509960880000
print(str(number).count('0'))

# task 2 ##############################

number = 40509960880000
str_num_reversed = str(number)[::-1]
zero_count = ''
for _ in str_num_reversed:
    if _ == '0':
        zero_count += _
    else:
        break
print(len(zero_count))

# task 3 ##############################

my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [10, 15, 20, 25]
my_result = []
for sym in my_list_1:
    if sym % 2 == 0:
        my_result.append(sym)
for sym in my_list_2:
    if sym % 2 != 0:
        my_result.append(sym)
print(my_result)

# task 4 ##############################

my_list = [1, 2, 3, 4]
new_list = []
new_list.extend(my_list[1:])
new_list.append(my_list[0])
print(new_list)

# task 5 ##############################

my_list = [1, 2, 3, 4]
my_list.append(my_list.pop(0))
print(my_list)

# task 6 ##############################

my_str = '43 больше чем 34 но меньше чем 56'
my_result = 0
new_str = ''
for sym in my_str:
    if not sym.isalpha():
        new_str += sym
add_list_1 = new_str.split(' ')
add_list_2 = []
for index in range(len(add_list_1)):
    if add_list_1[index].isdigit():
        add_list_2.append(int(add_list_1[index]))
for value in add_list_2:
    my_result += value
print(my_result)

# task 7 ##############################

my_str = 'asdfjuu'
my_list = []
if len(my_str) % 2 != 0:
    my_str += '_'
for index in range(0, len(my_str), 2):
    my_list.append(my_str[index:index+2])
print(my_list)

# task 8 ##############################

my_str = 'My_long str'
l_limit = 'o'
l_limit_index = my_str.index(l_limit)
r_limit = 't'
r_limit_index = my_str.index(r_limit)
sub_str = f'{my_str[l_limit_index+1:r_limit_index]}'
print(sub_str)

# task 9 ##############################

my_str = 'My long string'
l_limit = 'o'
l_limit_index = my_str.index(l_limit)
r_limit = 'g'
r_limit_index = my_str.rindex(r_limit)
sub_str = f'{my_str[l_limit_index+1:r_limit_index]}'
print(sub_str)

# task 10 #############################

my_list = [2, 4, 1, 5, 3, 9, 0, 7]
result_list = []
for index in range(len(my_list)):
    if index != 0 and index != len(my_list)-1:
        if my_list[index] > (my_list[index-1] + my_list[index+1]):
            result_list.append(my_list[index])
print(result_list)
print(len(result_list))
