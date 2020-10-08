import random

# task 1 ############################################

my_list = [random.randint(1, 100) for sym in range(20)]
print(my_list)


# task 2 ############################################

triangle = dict(A=(random.randint(0, 100), random.randint(0, 100)),
                B=(random.randint(0, 100), random.randint(0, 100)),
                C=(random.randint(0, 100), random.randint(0, 100)))
print(triangle['B'])


# task 3 ############################################

def my_print(my_str):
    print(f'***{my_str}***')

my_print("I'm a string")



# task 4 ############################################

my_dict_1 = dict(a=1, b=4, c='hello', r=True, key_1='here')
my_dict_2 = dict(key_1='val_1', key_2=890, key_3=False, a='item')

# a)
my_list = [key for key in my_dict_1.keys()]
my_list.extend(key for key in my_dict_2.keys())
print(my_list)

# б)
my_list = [key for key in my_dict_1.keys() if key not in my_dict_2.keys()]
print(my_list)

# в)
new_dict = {}
my_list = [key for key in my_dict_1.keys() if key not in my_dict_2.keys()]
for key, value in my_dict_1.items():
    if key in my_list:
        new_dict.setdefault(key, value)
print(new_dict)

# г)
new_dict = {}
keys_list = [key for key in my_dict_1.keys() if key not in my_dict_2.keys()] + [key for key in my_dict_2.keys() if key not in my_dict_1.keys()]
for key, value in my_dict_1.items():
    if key in keys_list:
        new_dict.setdefault(key, value)
    else:
        new_dict.setdefault(key, [my_dict_1[key], my_dict_2[key]])
for key, value in my_dict_2.items():
    if key in keys_list:
        new_dict.setdefault(key, value)
    else:
        new_dict.setdefault(key, [my_dict_1[key], my_dict_2[key]])
print(new_dict)
