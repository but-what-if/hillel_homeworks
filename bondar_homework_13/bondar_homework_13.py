import random
import string
import os
import json


# Треугольники #######################################


def create_random_triangle():
    x1 = random.uniform(0, 300)
    x2 = random.uniform(0, 300)
    x3 = random.uniform(0, 300)
    y1 = random.uniform(0, 300)
    y2 = random.uniform(0, 300)
    y3 = random.uniform(0, 300)
    tri_coords = [(x1, y1), (x2, y2), (x3, y3)]
    if (x1 == x2 == x3) or (y1 == y2 == y3) or abs(((y1 - y2) / (x1 - x2)) - ((y1 - y3) / (x1 - x3))) < 0.01:
        tri_coords[2] = (random.uniform(0, 300),) + tri_coords[2][1:]
        tri_coords[2] = tri_coords[2][:1] + (random.uniform(0, 300),)
        return tuple(tri_coords)
    else:
        return tuple(tri_coords)


def create_right_triangle(vert: tuple, area=100):
    x1 = vert[0]
    y1 = vert[1]
    x2 = x1
    y2 = area / 0.5
    x3 = y2
    y3 = y1
    tri_coords = [(x1, y1), (x2, y2), (x3, y3)]
    return tuple(tri_coords)


tri_coords = create_right_triangle((1, 1))


def calculate_triangle_area(tri_coords: tuple):
    ((x1, y1), (x2, y2), (x3, y3)) = tri_coords
    area = ((x1 - x3) * (y2 - y3) - (y1 - y3) * (x2 - x3)) / 2
    return area


# Задание 2 ##########################################



def generate_str():
    numbers = ''.join(random.choice(string.digits + '_') for i in range(4))
    letters = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
    random_str = numbers + letters
    return random_str


file = generate_str()


try:
    os.mkdir('tmp_folder')
except:
    pass


def create_file(data, filename, path='./'):
    with open(f'{path}{filename}', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


def generate_json_data(filename):
    number = list(filename[:4])
    random_width = random.randint(0, 400)
    file_name = {'filename': filename}
    width = {'width': random_width}
    objects = {'objects': []}
    segment_width = {
        '0': {
            'xmin': 0,
            'xmax': random_width / 4
        },
        '1': {
            'xmin': random_width / 4,
            'xmax': random_width / 2
        },
        '2': {
            'xmin': random_width / 2,
            'xmax': 3 * (random_width / 4)
        },
        '3': {
            'xmin': 3 * (random_width / 4),
            'xmax': random_width
        }
    }
    for i in range(len(number)):
        exit_door = False
        counter = 0
        while not exit_door and counter <= len(number):
            if number[i] != '_':
                objects['objects'].append({"object": {"class": number[i], "xmin": segment_width[str(i)]['xmin'],
                                                              "xmax": segment_width[str(i)]['xmax']}})
                exit_door = True
            counter += 1

    return {**file_name, **width, **objects}


create_file(generate_json_data(file), file, path='tmp_folder/')
