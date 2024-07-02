import imagehash
import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import filetype


# Подсчет хэш-суммы изображения
def calculate_hash(path_file):
    img = Image.open(path_file)
    hash_img = str(imagehash.phash(img))
    img.close()
    return hash_img


# Получение списка всех изображений
def get_list_path_image(directories):
    list_path = []
    error_files = []
    formate = ['image/jpeg', 'image/png', 'image/bmp', 'image/gif']
    for directory in directories:
        file_names = os.listdir(directory)
        for file_name in file_names:
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                file_format = filetype.guess(file_path)
                if file_format is None:
                    error_files.append(file_path)
                elif file_format.mime in formate:
                    list_path.append(file_path)
    result = pd.DataFrame(list_path, columns=['File Path'])
    return result, error_files


# Запись хэш-суммы изображения в таблицу
def get_list_hash(image_df):
    image_df['Image Hash'] = image_df['File Path'].apply(calculate_hash)
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


def draw_duplicate_image(group_hash, num_cols, num_rows):
    fig = plt.figure(figsize=(10, 6))
    axes = []
    for i, (_, item) in enumerate(group_hash.iterrows()):
        file_path = item['File Path']
        img = Image.open(file_path)
        ax = fig.add_subplot(num_rows, num_cols, i + 1)
        ax.imshow(img)
        ax.set_title(f'Image {i + 1}')
        ax.axis('off')
        axes.append(ax)
        img.close()

    plt.tight_layout()
    plt.show()


def search_dupl(list_dir):
    image_list, error_files = get_list_path_image(list_dir)
    image_hash_list = get_list_hash(image_list)
    group_hash_result = group_hash(image_hash_list)
    count_images = len(group_hash_result)
    if count_images == 0:
        return False, group_hash_result
    else:
        return True, group_hash_result


def show_dupls(pd_group_dupl):
    count_dupl = len(pd_group_dupl)
    num_cols = min(count_dupl, 2)
    num_rows = (count_dupl + num_cols - 1) // num_cols
    draw_duplicate_image(pd_group_dupl, num_cols, num_rows)


# Save the DataFrame duplicates to an .xlsx file in the current directory
def save_to_xlsx(pd_dupls, path_save_xlsx):
    if path_save_xlsx != '':
        file_path = os.path.join(path_save_xlsx, 'result.xlsx')
        pd_dupls.to_excel(file_path, sheet_name='duplicates')
