'''Задача4. Агрегирование данных из CSV файла
 Напишите скрипт, который считывает данные из CSV файла, содержащего
 информацию о продажах (название продукта, количество, цена за единицу), и
 подсчитывает общую выручку для каждого продукта. Итог должен быть сохранён в
 новом CSV файле.
 Пример:Из файла sales.csv нужно создать файл total_sales.csv, где для каждого
 продукта будет указана общая выручка'''

import csv
from itertools import product
from pathlib import Path

def sales_to_total_csv(sales_file: Path, total_file: Path) -> None:
    data_dict = {}
    with open(sales_file, 'r', newline='', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            product_name = row['product']
            quantity = int(row['quantity'])
            price = float(row['price'])
            total_sales = quantity * price
            if product_name in data_dict:
                data_dict[product_name] += total_sales
            else:
                data_dict[product_name] = total_sales

    with open(total_file, 'w', newline='', encoding="utf-8") as csv_file:

        csv_writer = csv.DictWriter(csv_file, dialect='excel-tab', fieldnames=['product', 'total_sales'])
        csv_writer.writeheader()

        for product_name, total_sales in data_dict.items():
            csv_writer.writerow({'product': product_name, 'total_sales': total_sales})
            print(product_name, total_sales)


if __name__ == '__main__':
    sales_to_total_csv(Path('sales.csv'), Path('total_sales.csv'))




