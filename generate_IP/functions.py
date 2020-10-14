from random import randint


def get_rand_0_255(mask_val_length=3):
    max_range_value = 255 if mask_val_length > 2 else (10 ** mask_val_length) - 1
    min_range_value = 10 ** (mask_val_length - 1)
    return randint(min_range_value, max_range_value)


# Более простой вариант функции

# def get_rand_0_255(mask_val_length):
#     if mask_val_length <= 1:
#         min_val = 0
#         max_val = 9
#     elif mask_val_length == 2:
#         min_val = 10
#         max_val = 99
#     else:
#         min_val = 100
#         max_val = 255
#     return randint(min_val, max_val)

def get_ip(mask="xxx.xx.xx.x"):
    return ".".join([str(get_rand_0_255(len(x))) for x in mask.split(".")])



def sort_ip_key(ip):
    ip_parts = ip.split(".")
    key_list = []
    for part in ip_parts:
        key_list.append(int(part))
    return key_list
    # return [int(part) for part in ip.split(".")]


def generate_list_ip_address(number: int, repeat=True, sort=False) -> list:
    ip_list = []
    for _ in range(number):
        ip_list.append(get_ip())
    if not repeat:
        ip_list = list(set(ip_list))
    if sort:
        ip_list.sort(key=sort_ip_key)
    return ip_list