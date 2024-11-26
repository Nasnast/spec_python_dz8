'''Задача2.Объединение данных из нескольких JSON файлов

 Напишите скрипт,который объединяет данные из нескольких JSON файлов в
 один. Каждый файл содержит список словарей, описывающих сотрудников
 компании(имя, фамилия, возраст, должность). Итоговый JSON файл должен
 содержать объединённые списки сотрудников из всех файлов.

 Пример: У вас есть три файла employees1.json, employees2.json,
 employees3.json. Нужно объединить их в один файл all_employees.json.'''

import os
import json
from pathlib import Path
import glob

def merge_json_file(file_path: Path, new_file: Path) -> None:
    merge_data = []
    for file in glob.glob(str(file_path) + '/*.json'):
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            merge_data.extend(data)

    with open(new_file, 'w', encoding='utf-8') as f_all:
        json.dump(merge_data, f_all, ensure_ascii=False, indent=4)

    #print(merge_data)




if __name__ == '__main__':
    merge_json_file(Path.cwd(), 'all_employees.json')
