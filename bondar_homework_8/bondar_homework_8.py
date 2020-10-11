# task 1 ##############################################

def get_domains(file):
    with open(file, 'r') as domains:
        domains_list = [line.strip() for line in domains.readline()]
    print(domains_list)

get_domains('domains.txt')