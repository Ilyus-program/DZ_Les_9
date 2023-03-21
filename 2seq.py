# Запрос пользователю на ввод данных
str_numbers = input('Введите элементы через запятую, либо точку с запятой, либо слеш: ')

# Замена разделителей на ','
numbers = str_numbers.replace(';', ',')
numbers = numbers.replace('/', ',')

# Преобразование введенных данных в список
numbers = numbers.split(',')
int_numbers = []
new_numbers = []

# Преобразование элементов списка в целое число
for i in numbers:
    i = int(i)
    int_numbers.append(i)

# Создание списка из чисел списка int_numbers, если это число в одном экземпляре
for j in int_numbers:
    if int_numbers.count(j) == 1:
        new_numbers.append(j)

# Вывод данных в консоль через запятую, согласно задания
for i in range(len(new_numbers)):
    if i != (len(new_numbers) - 1):
        print(f'{new_numbers[i]},', end='')
    else:
        print(new_numbers[i])