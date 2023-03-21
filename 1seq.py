count = input('Введите количество элементов: ')

# Проверка на то, что введенные данные являются цифрами
while count.isdigit() == False:
    count = input('Вы ввели не число. Попробуйте еще: ')
count = int(count)

digits = []

# Формирование количества запросов в зависимости от count
for i in range(1, count + 1):
    question = input(f'Введите {i} элемент: ')
    while question.isdigit() == False:
        question = input('Вы ввели не число. Попробуйте еще: ')
    question = int(question)
    digits.append(question)

# Сортировка по возрастанию
digits.sort()
print(digits)