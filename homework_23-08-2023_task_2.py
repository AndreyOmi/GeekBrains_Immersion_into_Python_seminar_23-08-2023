'''
Задача № 2: Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
'''

import random 

### Функция для поиска дубликатов в списке
def find_duplicates(input_list):
    frequency_dict = {}
    duplicates = []

    for item in input_list:
        if item in frequency_dict:
            if frequency_dict[item] == 1:
                duplicates.append(item)
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1

    return duplicates

# Генерация случайного списка с повторяющимися элементами. Т.к. генерация случайная, если исходный список оказался без повторяющихся элементов, то запустите программу еще раз.

MIN_SIZE = 1
MAX_SIZE = 40

input_list = [random.choice([random.randint(1, MAX_SIZE) for _ in range(MAX_SIZE)]) for _ in range(random.randint(MIN_SIZE, MAX_SIZE))]
print("Исходный список с повторяющимися элементами:", sorted(input_list))
duplicate_list = find_duplicates(input_list)
print("Список дублирующихся элементов: ", sorted(duplicate_list))

 