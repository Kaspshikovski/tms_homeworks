import csv

with open(input('Введите название (путь) документа: '), 'r', encoding='utf-8') as file:
    rows: csv._reader = csv.reader(file, delimiter=input('Укажите разделитель: '))

    for row in rows:
        if int(row[-1]) < 3:
            print(f' Учащийся: {row[0]} {row[1]}, оценка: {row[-1]}')
