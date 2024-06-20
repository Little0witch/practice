import hashlib
import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


# подсчет хэш-суммы изображения
def cal_hash(path_file):
    return hashlib.md5(open(path_file, 'rb').read()).hexdigest()


# получение списка всех изображений в папке
def get_list_image(directory):
    directory_list = list(os.walk(directory))
    for item in directory_list:
        dir_path, _, file_names = item
    list_path = []
    for file_name in file_names:
        if file_name.endswith('.jpg'):
            list_path.append(os.path.join(dir_path, file_name))
    print('len list_image', len(list_path))
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


input_directory_path = r"C:\Users\Татьяна\Desktop\modsen\5 Flower Types Classification Dataset-1\5 Flower Types Classification Dataset\tmp"
request_directory = []
request_directory.append(input_directory_path)
image_list = []
image_list = pd.concat([get_list_image(directory_path) for directory_path in request_directory], ignore_index=True)
image_hash_list = get_list_hash(image_list)
group_hash_result = group_hash(image_hash_list)
fig = plt.figure(figsize=(8, 5))

num_images = len(group_hash_result)
print(num_images)
num_cols = min(num_images, 4)
if num_images > 0:
    num_rows = (num_images + num_cols - 1) // num_cols  # количество строк в сетке
else:
    num_rows = 1

for i, (_, item) in enumerate(group_hash_result.iterrows()):
    file_path = item['File Path']
    img = Image.open(file_path)
    ax = fig.add_subplot(num_rows, num_cols, i + 1)
    ax.imshow(img)
    plt.gca().set_axis_off()
    ax.set_title(f'Image {i + 1}')
plt.tight_layout()
plt.show()
