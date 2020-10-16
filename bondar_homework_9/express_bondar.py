import os

# 0-express ##############################################################

def get_dir_items(path='./'):
    list_dir = sorted(os.listdir(path))
    dir_items = {'files': [],
                'folders': []
                }
    for item in list_dir:
        path_item = os.path.join(path, item)
        if os.path.isfile(path_item):
            dir_items['files'].append(item)
        else:
            dir_items['folders'].append(item)
    print(dir_items)


get_dir_items(path='../bondar_homework_9')