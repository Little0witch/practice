import os
import pandas as pd

def get_subdirectories(directory):
    # директории, поддиректории, файлы
    directory_all = list(os.walk(directory))
    for item in directory_all:
        _, _,file_names = item # название файлов
    list_path = []
    for file_name in file_names:
        list_path.append(os.path.join(directory,file_name))
    result = pd.DataFrame(list_path)
    return (result)

directory_path = r"C:\Users\Татьяна\Desktop\modsen\5 Flower Types Classification Dataset-1\5 Flower Types Classification Dataset\Lilly"
subdirectories = get_subdirectories(directory_path)

print(subdirectories)
