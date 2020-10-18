import random
import json
import csv
import string


# Generate data for writting txt file - task 1

def generate_data_txt():
    n = '\n'
    print(n)
    for paragraph in range(3):
        print(''.join(random.choice(string.ascii_letters + string.punctuation + string.digits + string.whitespace + n) for i in range(100)))

generate_data_txt()