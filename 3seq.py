# Запрос пользователю на ввод данных 1 списка
str_one_list = input('Введите элементы 1 списка через запятую, либо точку с запятой, либо слеш: ')

# Замена разделителей на ','
one_list = str_one_list.replace(';', ',')
one_list = one_list.replace('/', ',')
one_list = one_list.split(',')
int_one_list = []

# Преобразование элементов списка в целое число
for i in one_list:
    i = int(i)
    int_one_list.append(i)
# Запрос пользователю на ввод данных 2 списка
str_two_list = input('Введите элементы 2 списка через запятую, либо точку с запятой, либо слеш: ')

# Замена разделителей на ','
two_list = str_two_list.replace(';', ',')
two_list = two_list.replace('/', ',')
two_list = two_list.split(',')
int_two_list = []

# Преобразование элементов списка в целое число
for j in two_list:
    j = int(j)
    int_two_list.append(j)

# print(int_one_list)
# print(int_two_list)

# Вычитание 2го списка из 1го
for k in int_two_list:
    for l in int_one_list:
        if l == k:
            for s in range(1, int_one_list.count(l) + 1):
                int_one_list.remove(l)

# Вывод данных в консоль через запятую, согласно задания
for i in range(len(int_one_list)):
    if i != (len(int_one_list) - 1):
        print(f'{int_one_list[i]},', end='')
    else:
        print(int_one_list[i])