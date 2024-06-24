import imagehash
import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


# Подсчет хэш-суммы изображения
def cal_hash(path_file):
    img = Image.open(path_file)
    hash_img = str(imagehash.phash(img))
    img.close()
    return hash_img


# Получение списка всех изображений в папке
def get_list_image(directory):
    list_path = []
    directory_list = list(os.walk(directory))
    for item in directory_list:
        dir_path, _, file_names = item
        for file_name in file_names:
            if file_name.endswith('.jpg'):
                list_path.append(os.path.join(dir_path, file_name))
    result = pd.DataFrame(list_path, columns=['File Path'])
    return result


# Запись хэш-суммы изображения в таблицу
def get_list_hash(image_df):
    image_df['Image Hash'] = image_df['File Path'].apply(cal_hash)
    return image_df


# Группировка по хэш-сумме
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


input_directory_path = input()
request_directory = []
while 1:
    if input_directory_path == 'q':
        break
    else:
        request_directory.append(input_directory_path)
        input_directory_path = input()
image_list = pd.concat([get_list_image(directory_path) for directory_path in request_directory], ignore_index=True)
image_hash_list = get_list_hash(image_list)
group_hash_result = group_hash(image_hash_list)
count_images = len(group_hash_result)
if count_images > 0:
    num_cols = min(count_images,2)
    num_rows = (len(group_hash_result) + num_cols - 1) // num_cols
    fig = plt.figure(figsize=(10, 6))
    axes = []
    for i, (_, item) in enumerate(group_hash_result.iterrows()):
        file_path = item['File Path']
        file_hash = item['Image Hash']
        img = Image.open(file_path)
        ax = fig.add_subplot(num_rows, num_cols, i+1)
        ax.imshow(img)
        ax.set_title(f'Image {i + 1}')
        ax.axis('off')
        axes.append(ax)
        img.close()

    plt.tight_layout()
    plt.show()
else:
    print("Not found duplicate")
