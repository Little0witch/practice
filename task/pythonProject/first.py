import imagehash
import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageOps


# подсчет хэш-суммы изображения
def cal_hash(path_file):
    img = Image.open(path_file)
    img = ImageOps.autocontrast(img)
    img = ImageOps.equalize(img)
    img = img.resize((32, 32))
    img = img.convert('L')
    hash_img = str(imagehash.phash(img))
    img.close()
    return hash_img


# получение списка всех изображений в папке
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


# подсчет хэш-суммы каждого изображения
def get_list_hash(image_list):
    image_list['Image Hash'] = image_list['File Path'].apply(cal_hash)
    return image_list


# группировка по хэш-сумме
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
count_group_list = group_hash_result['Image Hash'].value_counts().tolist()
num_images = len(group_hash_result)
if num_images > 0:
    current_group = 0
    count_group = 0
    num_cols = min(count_group_list[current_group], 2)
    num_rows = (count_group_list[current_group] + num_cols - 1) // num_cols
    num_subplots = num_rows * num_cols
    fig = plt.figure(figsize=(8, 5))
    axes = []
    for i, (_, item) in enumerate(group_hash_result.iterrows()):
        file_path = item['File Path']
        file_hash = item['Image Hash']
        if i == 0:
            count_group += 1
        if count_group_list[current_group] == count_group:
            current_group += 1
            count_group = 0
            num_cols = min(count_group_list[current_group], 2)
            num_rows = (count_group_list[current_group] + num_cols - 1) // num_cols
            num_subplots = num_rows * num_cols

        img = Image.open(file_path)
        ax = fig.add_subplot(num_rows, num_cols, i % num_subplots + 1)
        ax.imshow(img)
        ax.set_title(f'Image {i + 1}')
        ax.axis('off')
        axes.append(ax)
        img.close()
        if i != 0:
            count_group += 1

    plt.tight_layout()
    plt.show()
else:
    print("Not found duplicate")
