import cv2
import numpy as np


def pHash(image_path, block_size):
    # Загрузка изображения, изменение размера и преобразование в оттенки серого
    image = cv2.imread(image_path)
    image = cv2.resize(image, (block_size, block_size))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Выполнение дискретного косинусного преобразования (DCT)
    dct = cv2.dct(np.float32(image))

    # Сокращение DCT до левого верхнего блока 8x8
    dct_block = dct[:8, :8]

    # Вычисление среднего значения DCT
    mean_val = np.mean(dct_block[1:])

    # Бинаризация DCT на основе среднего значения
    hash_bits = (dct_block > mean_val).astype(int)

    # Преобразование битов в хэш
    hash_value = ''.join(str(bit) for bit in np.reshape(hash_bits, -1))

    return hash_value


def compare_hashes(hash1, hash2):
    if len(hash1) != len(hash2):
        raise None

    # Подсчет числа несовпадающих битов
    mismatch_count = sum(bit1 != bit2 for bit1, bit2 in zip(hash1, hash2))
    # Вычисление коэффициента сходства
    similarity = 1 - (mismatch_count / len(hash1))

    return similarity