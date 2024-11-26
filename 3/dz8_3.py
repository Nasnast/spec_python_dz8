'''Задача 3. Агрегирование данных из CSV файла
 Напишите скрипт, который считывает данные из JSON файла и сохраняет их в CSV
 файл.
 JSON файл содержит данные о продуктах (название, цена, количество на
 складе).
 В CSV файле каждая строка должна соответствовать одному продукту.
 Пример: Из файла products.json нужно создать products.csv'''

import json
import csv
from pathlib import Path

def product_json_to_csv(json_file: Path) -> None:
    with open(json_file, 'r', encoding='utf-8') as json_f:
        data = json.load(json_f)

    row = []
    for product in data:
        row.append(product)
        print(product)

    with open(f'{json_file.stem}.csv', 'w', encoding='utf-8', newline='') as csv_f:
        csv_writer = csv.DictWriter(csv_f, fieldnames=data[0].keys(), dialect='excel-tab')
        csv_writer.writeheader()
        csv_writer.writerows(row)
        csv_f.close()

if __name__ == '__main__':
    product_json_to_csv(Path('products.json'))