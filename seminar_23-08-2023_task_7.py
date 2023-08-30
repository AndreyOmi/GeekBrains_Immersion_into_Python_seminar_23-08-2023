'''
Задание № 7: Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.

'''

default_value = "Мама мыла раму."
user_input = input(f"Введите строку текста (по умолчанию будет введено: {default_value}): ")

if user_input == "":
    user_input = default_value


frequency_dict = {}  # Dictionary to store letter frequencies


### Решение без count()

print('\nРешение без count()\n')

for letter in user_input:
    if letter.isalpha():  # Check if the character is a letter
        if letter in frequency_dict:
            frequency_dict[letter] += 1
        else:
            frequency_dict[letter] = 1

print("Частоты букв (без использования count()):")

for letter, frequency in frequency_dict.items():
    print(f"{letter}: {frequency}")

### Решение без count()

print('\nРешение c count()\n')

for letter in user_input:
    if letter.isalpha():  
        frequency_dict[letter] = user_input.count(letter)

print("Частоты букв (с использованием count()):")

for letter, frequency in frequency_dict.items():
    print(f"{letter}: {frequency}")

print('''\nПорядок ключей (букв) совпадает в обоих решениях,
потому что в этом порядке в обоих решениях буквы добавляются в словарь.
''')











