# Задача: Написать программу, которая из имеющегося массива строк формирует новый массив из строк,
# длина которых меньше, либо равна 3 символам.
# Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма.
# При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.


def filter_string(names, lenght_filter = 3):
    result = []

    for name in names:
        if len(name) <= lenght_filter:
            result.append(name)

    return result

names = ['Russia', 'Denmark', 'Saratov', 'RSA']
result = filter_string(names)

print(f'{names}.\n\n'
      f'{result}.')