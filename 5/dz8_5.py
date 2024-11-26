'''Задача5. Конвертация CSV в JSON с изменением структуры данных
 Напишите скрипт, который считывает данные из CSV файла и сохраняет их в
 JSON файл с другой (структурой.
 CSV файл содержит данные о книгах (название, автор, годиздания).
 В JSON файле данные должны быть сгруппированы по авторам,
 а книги каждого автора должны быть записаны как список.
 Пример:Из файла books.csv нужно создать файл books_by_author.json, где
 книги сгруппированы по авторам.'''

import csv
import json
from pathlib import Path

def book_csv_to_json(csv_file: Path):
    data_books = {}
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            #id_book = row['bookID']
            authors = row['authors']
            title = row['title']

            if authors in data_books:
                data_books[authors].append(title)
            else:
                data_books[authors] = [title]

    #print(data_books)
    with open(csv_file.stem + '.json', 'w', newline='', encoding='utf-8') as json_f:
        json.dump(data_books, json_f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    book_csv_to_json(Path('books.csv'))


