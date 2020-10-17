import random


# task 1 ##############################################

def get_domains(file):
    with open(file, 'r') as domains:
        domains_list = [line.rstrip().strip('.') for line in domains.readlines()]
        return domains_list


# task 2 ##############################################

def get_names(file):
    with open(file, 'r') as people_info:
        people_info_list = [line.strip() for line in people_info.readlines()]
        print(people_info_list)
        names = []
        for val in people_info_list:
            names.append(val.split()[1])
        print(names)
get_names('names.txt')


# task 3 ##############################################

def get_random_number():
    return random.randint(100, 999)

def get_random_string():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=(random.randint(5, 7))))


def generate_email(name, number, string, domain):
    email = f'{name}.{number}@{string}.{domain}'
    print(email)

name = random.choice(get_names('names.txt'))
number = get_random_number()
string = get_random_string()
domain = random.choice(get_domains('domains.txt'))


generate_email(name, number, string, domain)



