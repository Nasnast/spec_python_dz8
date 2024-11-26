'''Задание 1. Работа с основными данными
 Напишите функцию, которая получает на вход директорию и рекурсивно обходит
 её и все вложенные директории.
 Результаты обхода сохраните в файлы json, csv и pickle.
 Для дочерних объектов указывайте родительскую директорию.
 Для каждого объекта укажите файл это или директория.
 Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
 файлов идиректорий.
 Соберите из созданных на уроке и в рамках домашнего
 задания функций пакет для работы с файлами разных форматов'''

import os
import csv
import json
import pickle
from pathlib import Path

def go_directory(directory: Path) -> list:
    data = []

    for dir_path, dir, file in os.walk(directory):
        for f in dir + file:
            fp = os.path.join(dir_path, f)
            is_dir = os.path.isdir(fp)

            if os.path.isfile(fp):
                size = os.path.getsize(fp)
            elif os.path.isdir(fp):
                total_size = 0
                for dirs, _, files in os.walk(fp):
                    for f_n in files:
                        fp = os.path.join(dirs, f_n)
                        total_size += os.path.getsize(fp)

            parent = os.path.dirname(fp)
            data.append({'name': f,
                         'type': 'Directory' if is_dir else 'File',
                         'size': total_size if is_dir else size,
                         'parent': parent})


    convert_to_json(data)
    convert_to_csv(data)
    convert_to_pickle(data)


def convert_to_json(data: list) -> None:
    with open('info.join', 'w', encoding='utf-8') as file_json:
        json.dump(data, file_json, ensure_ascii=False, indent=4)

def convert_to_csv(data: list) -> None:
    with open('info.csv', 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=['name', 'type', 'size', 'parent'], dialect='excel-tab')
        csv_writer.writeheader()
        csv_writer.writerows(data)

def convert_to_pickle(data: list) -> None:
    with open('info.bin', 'wb') as file_picle:
        pickle.dump(data, file_picle)



if __name__ == '__main__':
    go_directory(Path(r'D:\Anastasi\geekBrains\Погружение в Python 07.10.2024\Sem8\DZ8'))
