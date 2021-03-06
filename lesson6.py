users = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
    {'name': 'Эдувард', 'age': 48, 'job': 'Big Boss'},
    ]
  
import csv

with open('user_list.csv', 'w', encoding='utf-8') as file:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(file, fields, delimiter=',')
    writer.writeheader()
    for user in users:
        writer.writerow(user)