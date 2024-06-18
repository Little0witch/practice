import hashlib
import os
import pandas as pd
import cv2


# def get_image(file_name):
#     img = cv2.imread(file_name)
#     cv2.imshow('tmp', img)
#     cv2.waitKey(0)

def cal_hash(path_file):
    return hashlib.md5(open(path_file, 'rb').read()).hexdigest()


def get_subdirectories(directory):
    # директории, поддиректории, файлы
    directory_all = list(os.walk(directory))
    for item in directory_all:
        dir_path, _, file_names = item  # название файлов
    list_path = []
    for file_name in file_names:
        list_path.append(os.path.join(dir_path, file_name))
    result = pd.DataFrame(list_path, columns=['File Path'])
    result['Image Hash'] = result['File Path'].apply(cal_hash)
    return result

def group_hash(table_hashsum):
    grouped = table_hashsum.groupby(["Image Hash"], as_index=False)
    for hash_sum, group in grouped:
        # print("Image Hash:", hash_sum)
        print(group)
        print()  # Пустая строка между группами

directory_path = r"C:\Users\Татьяна\Desktop\modsen\5 Flower Types Classification Dataset-1\5 Flower Types Classification Dataset\tmp"
subdirectories = get_subdirectories(directory_path)
group_hash(subdirectories)
# print(subdirectories)
