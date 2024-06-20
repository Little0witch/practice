import hashlib
import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def cal_hash(path_file):
    return hashlib.md5(open(path_file, 'rb').read()).hexdigest()

def get_subdirectories(directory):
    directory_all = list(os.walk(directory))
    for item in directory_all:
        dir_path, _, file_names = item
    list_path = []
    for file_name in file_names:
        list_path.append(os.path.join(dir_path, file_name))
    result = pd.DataFrame(list_path, columns=['File Path'])
    result['Image Hash'] = result['File Path'].apply(cal_hash)
    return result

def group_hash(table_hashsum):
    grouped = table_hashsum.groupby(["Image Hash"], as_index=False)
    duplicates = []
    for _, group in grouped:
        if len(group) > 1:
            duplicates.append(group)
    if duplicates:
        duplicates_df = pd.concat(duplicates)
        duplicates_df.reset_index(drop=True, inplace=True)
        return duplicates_df
    else:
        return pd.DataFrame()


directory_path = r"C:\Users\Татьяна\Desktop\modsen\5 Flower Types Classification Dataset-1\5 Flower Types Classification Dataset\tmp"
subdirectories = get_subdirectories(directory_path)
group_hash_result = group_hash(subdirectories)
fig = plt.figure(figsize=(10, 6))
num_images = len(group_hash_result)
num_cols = min(num_images, 2)  # количество столбцов в сетке
num_rows = (num_images + num_cols - 1) // num_cols  #  количество строк в сетке

for i, (_, item) in enumerate(group_hash_result.iterrows()):
    file_path = item['File Path']
    img = Image.open(file_path)

    ax = fig.add_subplot(num_rows, num_cols, i+1)
    ax.imshow(img)
    ax.set_title(f'Image {i+1}')

plt.tight_layout()
plt.show()