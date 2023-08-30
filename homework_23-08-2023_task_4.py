'''
Задача № 4: Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. 
* Верните все возможные варианты комплектации рюкзака.
'''

from itertools import combinations

def select_elements(dictionary, limit):
    selected_elements = {}
    current_sum = 0
    
    for key, value in dictionary.items():
        if current_sum + value <= limit:
            selected_elements[key] = value
            current_sum += value
        else:
            break
    
    return selected_elements

def generate_combinations(dictionary):
    keys = list(dictionary.keys())
    all_combinations = []

    for i in range(1, len(keys) + 1):
        key_combinations = combinations(keys, i)
        for combo in key_combinations:
            new_dict = {key: dictionary[key] for key in combo}
            all_combinations.append(new_dict)

    return all_combinations

items = { "палатка": 2,
    "спальный мешок": 3,
    "консервы" : 5,
    "вода": 6,
    "одежда": 2,
    "фонарь": 1,
    "нож" : 1
     }

sorted_items = dict(sorted(items.items(), key=lambda x: x[1]))

max_sum = 10  # максимальная грузоподъёмность

selected_items = select_elements(sorted_items, max_sum)

print("\nВещи, которые можно взять:\n")
for key, value in selected_items.items():
    print(f"{key}: {value}")

##### Решение задачи выбора всех возможных вариантов комплектации рюкзака

combinations_list = generate_combinations(items)

print("\nВещи, которые можно взять (все комбинации):\n")
combinations_number = 0

for combo_dict in combinations_list:
    if sum(combo_dict.values()) <= max_sum:
        combinations_number += 1
        print(f'Вариант № {combinations_number} : {combo_dict}')

#### выбор лучшего варианта из всех возможных вариантов комплектации рюкзака       

print("\nЛучший вариант из всех возможных:\n")
print(max([combo_dict for combo_dict in combinations_list if sum(combo_dict.values()) <= max_sum], key=lambda d: len(d)))