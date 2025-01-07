'''PYTHON'''
# Tab - отступ выделенного кода.
# Shift + tab - отмена отступа выделенного кода
# Ctrl + / - закомментировать выделенный код (либо строку, где находится курсор), повторное нажатие раскомментировать.
# Ctrl + shift + стрелка вверх - двигает выделенный блок или строку вверх.
# Ctrl + shift + стрелка вниз - двигает выделенный блок или строку вниз.
# Для редактирования нескольких строк зажать альт и нажать на места, где нужно, чтобы появился курсор.
# Ctrl + d - дублировать текущую строку, либо выделенные строки.
# \ - перенос кода на новую строку.
# Ctrl + shift + u - изменить регистр букв.
# Ctrl + alt + l - форматирование кода по стандарту PEP 8.
# Для изменения вида скобок, например, с круглых на фигурные выделить открывающуюся круглую скобку и нажать на фигурную.
# Для дебага программы установить красную точку (нажать правее номера строки) на место с которого
# необходимо осуществить проверку программы, затем нажать Debug 'имя модуля' (shift + f9)
# и пошагово выполнить программу.
# Чтобы сравнить свой код с другим кодом, нужно выделить свой код (либо не выделять, тогда сравниваться
# будет весь файл), нажать на него ПКМ -> Compare with Clipboard, в левом окошке вставить другой код.
# Ctrl + f - поиск в тексте.
# Ctrl + r - замена в тексте.
# Ctrl + g - переход на указанный номер строки кода.
# Ctrl + shift + f - поиск во всех файлах.
# Ctrl + shift + r - замена во всех файлах.
# Alt + shift + c - показать последние изменения.

'''
# ЧИСЛА (** возведение в степень; // деление без остатка; % вывод остатка)
x = 5
# Согласно PEP 8 если используются операторы с разными приоритетами, 
# то нужно поставить пробелы только вокруг операторов с наименьшим (и) приоритетом (ами):
print(5 * 4**2)  # 80 (приоритет возведения в степень выше, чем приоритет умножения)
print(x, type(x))  # 5 <class 'int'> (тип данных и класс - это одно и то же)
print(6 / 2, type(6 / 2))  # 3.0 <class 'float'> (при делении всегда получается число с плавающей точкой)
print(2e3, type(2e3))  # 2000.0 <class 'float'> (2 умножить на 10 в степени 3)
print(1e-1)  # 0.1 (1 умножить на 10 в степени -1)
print(int(5 / 2))  # 2
# Степени возводятся справа налево:
print(1 ** 2 ** 3)  # 1 (сначала возводится 2 в степень 3, затем результат в степень 1)
print(-5 // 2)  # -3 (отрицательные числа округляются в большую сторону отрицательного числа)
x *= 10 - 2 - 3  # оператор присваивания с другой операцией (*=, /= и т. д.) имеет наименьший приоритет
print('x =', x)  # x = 25, аналогично x = x * (10 - 2 - 3)
x = float('inf')  # задание бесконечности
print(x, type(x))  # inf <class 'float'>
print(25_000_000)  # 25000000 (нижнее подчёркивание в числах нужно для удобства отображения)

# округление чисел
b = 2245.329
print(round(b, 2))  # 2245.33 (округление числа до указанного количества знаков)
print(round(b, -1))  # 2250.0 (округление до десятков)
# Если число оканчивается на 5, то округляется до ближайшего чётного (1.5 -> 2; 2.5 -> 2):
print(round(1.5), round(2.5))  # 2 2

# сравнение чисел
a, b, c = 4, 5, 6
print(b >= a <= c, b <= a >= c)  # True False (поиск наименьшего или наибольшего из трёх чисел)
print(5 != 6 != 5)  # True (проверка идёт последовательно, а не каждого значения с каждым)

# перевод чисел из заданной системы счисления в десятичную
print(int('0101010', 2))  # 42
print(int('FF', 16))  # 255
'''

'''
# МОДУЛЬ OPERATOR
from operator import *         # импортируем все функции
# Модуль operator реализован на языке C, поэтому функции 
# этого модуля работают в разы быстрее, чем самописные функции в Python.
print(add(10, 20))             # add - сумма, sub - разность, mod - остаток (аналогично %)
print(contains([1, 2, 3], 3))  # проверка на входимость
print(mul(2, 5))               # mul - умножение, pow - возведение в степень
print(floordiv(20, 3))         # floordiv - целочисленное деление (//), truediv - деление (/)
print(neg(9))                  # neg - смена знака
print(lt(3, 3))                # lt (less than; <), le (less than or equal; <=)
print(gt(8, 8))                # gt (greater than; >), ge (greater than or equal; >=)
print(eq(5, 5))                # eq (equal; ==), ne (not equal; !=)
'''


# МОДУЛИ DECIMAL & FRACTIONS (более точные и медленные, чем int и float)
import decimal
import fractions
import math
'''
# Задавать числа нужно либо из целых чисел либо из строки (из float не рекомендуется):
a = decimal.Decimal('4.55')
b = fractions.Fraction('0.55')
c = fractions.Fraction(3, 4)  # либо c = fractions.Fraction('3/4')
print(a, b, c)  # 4.55 11/20 3/4
d = decimal.Decimal(0.1)  # из float идёт неправильное округление
print(d)  # 0.1000000000000000055511151231257827021181583404541015625

# округление
# ROUND_HALF_EVEN: округляет до ближайшего четного числа, если округляемая часть равна 5 (по умолчанию)
print(decimal.Decimal("10.025").quantize(decimal.Decimal("1.00"), decimal.ROUND_HALF_EVEN))  # 10.02
print(decimal.Decimal("10.035").quantize(decimal.Decimal("1.00"), decimal.ROUND_HALF_EVEN))  # 10.04
# ROUND_HALF_UP: округляет число в сторону повышения, если после него идет число 5 или выше
print(decimal.Decimal("10.024").quantize(decimal.Decimal("1.00"), decimal.ROUND_HALF_UP))  # 10.02
print(decimal.Decimal("10.025").quantize(decimal.Decimal("1.00"), decimal.ROUND_HALF_UP))  # 10.03
# ROUND_HALF_DOWN: округляет число в сторону понижения, если после него идет число 5 или меньше
print(decimal.Decimal("10.025").quantize(decimal.Decimal("1.00"), decimal.ROUND_HALF_DOWN))  # 10.02
print(decimal.Decimal("10.026").quantize(decimal.Decimal("1.00"), decimal.ROUND_HALF_DOWN))  # 10.03

num = decimal.Decimal('10.0')
print(num.sqrt())  # 3.162277660168379331998893544 (квадратный корень)
print(num.exp())  # 22026.46579480671651695790065 (e в степени 10)
print(num.ln())  # 2.302585092994045684017991455 (натуральный логарифм)
print(num.log10(), type(num.log10()))  # 1 <class 'decimal.Decimal'>
print(math.log10(num), type(math.log10(num)))  # 1.0 <class 'float'> (преобразование decimal во float)
print(num.as_tuple())  # DecimalTuple(sign=0, digits=(1, 0, 0), exponent=-1)
# sign – знак числа (0 для положительного числа и 1 для отрицательного числа)
# digits – цифры числа
# exponent – значение экспоненты (количество цифр после точки, умноженное на -1)
print(decimal.getcontext())  # Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, и т. д.)
decimal.getcontext().prec = 3  # устанавливаем точность в 3 знака
print(1000 * num / 3)  # 3.33E+3 (10000 / 3 = 3333.33333333)
print(num / 3000)  # 0.00333
num = fractions.Fraction(6, 4)
print(num)  # 3/2 (сокращает дроби)
print(num.numerator)  # 3 (нахождение числителя)
print(num.denominator)  # 2 (нахождение знаменателя)

# Метод limit_denominator(arg) возвращает самую близкую к данному числу рациональную дробь,
# чей знаменатель не превосходит переданного аргумента:
print('PI =', math.pi)  # PI = 3.141592653589793
num = fractions.Fraction(str(math.pi))
print('No limit =', num)  # No limit = 3141592653589793/1000000000000000
for d in [1, 5,  50, 90, 100, 500, 1000000]:
    limited = num.limit_denominator(d)
    print(limited)  # 3, 16/5, 22/7, 267/85, 311/99, 355/113, 3126535/995207

# комплексные числа
z = 5 + 7j  # используется буква 'j', а не стандартная в математике 'i'
print(z, type(z))  # (5+7j) <class 'complex'>
z2 = complex(6, -8)
print(z2)  # (6-8j)
print(z2.real, z2.imag)  # 6.0 -8.0
print(z2.conjugate())  # (6+8j); нахождение сопряженного комплексного числа
'''

'''
# МОДУЛЬ RANDOM
import random
num = random.randint(0, 17)  # случайное целое число от 0 до 17 включительно (2 аргумента: начало и конец, без шага)
print(num)
num = random.randrange(0, 10, 2)  # случайное целое число от 0 до 10 с шагом 2 не включая 10
print(num)
num = random.random()
print(num)  # выводит число с плавающей точкой от 0 до 1.0 (исключая 1.0)
print(num * 100)  # расширение диапазона до 100 (исключая 100)
num = random.uniform(1.5, 17.3)  # число с плавающей точкой от 1,5 до 17,3 включительно
print(num)
# random.seed(17) # явно устанавливаем начальное значение для генератора случайных чисел
for _ in range(10):
    print(random.randint(1, 100))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)  # перемешать список
print(numbers)  # [2, 8, 5, 6, 7, 4, 3, 1]  (возможный вариант)
print(random.sample('BEEGEEK', 2))  # выводит указанное число случайных элементов (список)
print(random.choice('BEEGEEK'))  # выводит случайный элемент
print(random.choice([1, 2, 3, 4]))  # выводит случайный элемент
print(random.choice(['a', 'b', 'c', 'd']))  # выводит случайный элемент

w = [7, 6, 5, 4, 3, 2, 1]  # чем больше вес элемента, тем больше вероятность вывода элемента
print(random.choices('ABCDEFG', weights=w, k=17))  # k - количество выводимых элементов
# Переменная weights = [1, 2, 3] аналогична cum_weights = [1, 3, 6],
# каждый последующий элемент weights суммируется в cum_weights (1, 1 + 2, 1 + 2 + 3).

# алгоритм Монте-Карло (метод статистических испытаний, вычисление площади фигуры под кривой)
n = 10000  # количество испытаний
k = 0  # количество попаданий точки в вычисляемую область
s = 16  # площадь участка 4х4, в которую входит искомая фигура
for _ in range(n):
    x = random.uniform(-2, 2)  # координаты в искомой области 'х'
    y = random.uniform(-2, 2)  # координаты в искомой области 'у'
    if y ** 3 - 2 * x ** 2 <= -1 and 2 * y + x ** 3 <= 3:  # уравнения кривой
        k += 1  # если точка попадает в нужную область
print((k / n) * s)  # 8.4272
'''

'''
# МОДУЛЬ NUMPY
import numpy as np
import pandas as pd
a = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
print(a.shape)  # (3, 3) (1-ое число - количество строк, 2-ое число - столбцов)
print(np.sum(a))  # 27
print(sum(a))  # [ 6  9 12]
b = np.zeros(10)
c = np.ones(4)
d = np.empty(5)
print(b)  # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
print(c)  # [1. 1. 1. 1.]
print(d)  # [4.94065646e-324 3.95252517e-323 3.95252517e-323 3.95252517e-323 1.29061685e-306]
f = np.arange(80, 70, -1)
print(f, type(f))  # [80 79 78 77 76 75 74 73 72 71] <class 'numpy.ndarray'>
print(f.argmin(), f.argmax())  # 9 0 (индекс минимального и максимального элементов)
print(f.argsort())  # [9 8 7 6 5 4 3 2 1 0] (список индексов отсортированных элементов массива)
print(np.linspace(0, 10, 5))  # [ 0.   2.5  5.   7.5 10. ]; 5 чисел с равным шагом от 0 до 10
print(np.linspace(0, 10, 5, endpoint=False))  # [0. 2. 4. 6. 8.]
print(a.ndim)  # 2 (количество измерений в массиве)
print(a.size)  # 9 (количество элементов в массиве)
print(a.reshape(9, 1))  # 9 строк, 1 столбец
print(a.flatten())  # [1 2 3 2 3 4 3 4 5] (конвертация в одномерный массив)
print(a.tolist())  # [[1, 2, 3], [2, 3, 4], [3, 4, 5]] (конвертация массива в список)
print(np.concatenate((a, a)))  # нужны двойные скобки (по умолчанию axis=0)
print(np.concatenate((a, a), axis=1))  # axis=0 по строкам, axis=1 по столбцам
print('a =', a)
print(a < 4)
print(a[a < 4])  # [1 2 3 2 3 3]
print(a[(a % 2 == 0) & (a < 4)])  # [2 2] (& - and, | - or)
print(np.zeros((3, 2)))
print(np.flip(a, axis=0))
print(np.flip(a, axis=1))

# арифметические операции с массивами (выполняются поэлементно, каждый элемент с каждым)
print(a + 100)
print(a + a)
print(a / a)
print(a ** 3)

# метод nonzero (возвращает индексы элементов, которые не равны нулю либо удовлетворяют заданному условию)
w = np.nonzero(a == 3)  # поиск всех элементов массива "a", которые равны 3
# в 1-ом массиве индексы строк, во 2-ом массиве индексы столбцов
# если поставить *w, то выведет только 2 массива
print('w =', w)  # w = (array([0, 1, 2], dtype=int64), array([2, 1, 0], dtype=int64))
list_of_coordinates = list(zip(w[0], w[1]))
for coord in list_of_coordinates:
    print(coord)
a = np.random.random(4)
print(a, type(a))  # [0.97854558 0.85042458 0.64105727 0.72833058] <class 'numpy.ndarray'>

# функция where (возвращает индексы элементов, удовлетворяющих определённому условию)
grades = np.array([1, 3, 4, 2, 5, 5])
print(np.where(grades > 3))  # (array([2, 4, 5], dtype=int64),)
# Функция может принимать два опциональных параметра:
# 1-ый заменит значения, удовлетворяющие условию, а 2-ой неудовлетворяющие условию:
print(np.where(grades > 3, 'gt3', 'lt3'))  # ['lt3' 'lt3' 'gt3' 'lt3' 'gt3' 'gt3']

# random
print(np.random.binomial(1, 0.2, size=100))  # список из нулей и единиц
print(np.random.binomial(100, 0.2))  # 24 (конверсия)

# метод Монте-Карло
# Пример, где фактическая конверсия в группе "a" больше конверсии в группе "b" из-за недостаточно большой выборки.
result = []
for i in range(1000):
    a = np.random.binomial(1, 0.03, size=1000).mean()
    b = np.random.binomial(1, 0.05, size=1000).mean()
    result.append((a, b))
df = pd.DataFrame(result, columns=['a', 'b'])
print(df[df['a'] > df['b']])
'''

'''
# СТРОКИ (STRING)
i = 5; print(i); print('y')  # ";" позволяет не переносить часть кода на новую строку
print('rtd\nsdf\n\tsdf')
text = ("способ переноса текста на другую "
        "строку (вывод не меняется)")  # либо использовать тройные кавычки, тогда текст будет на разных строках
print(text)
a = fr'Hello What iS It1'

# методы строк
print(a.count('lo'))  # 1 (считает количество совпадений)
print(a.find('iS', 1, 14))  # порядковый номер элемента, встречающегося 1-ый раз, если не встречается, то выводит -1
# rfind, rindex (порядковый номер символа с конца), index аналогичен find, однако если вхождения нет, то выводит ошибку
pattern = 'AT'
data = 'ATTAAAGGTTTATACCTTCCCAGGT1!# AT'
x = data.find(pattern, data.find(pattern) + 1)
print(x)  # 11 (2-ое вхождение значения)
x = data.find(pattern, x + 1)
print(x)  # 29 (3-ее вхождение значения)

# Метод join итерирует переданный аргумент и добавляет "разделитель" между проитерированными элементами.
# Все проитерированные элементы должны быть строками.
print('123'.join([a, 'q', 'e']))  # Hello What iS It1123q123e
print('123'.join(a))  # H123e123l123l123o123 123W123h123a123t123 123i123S123 123I123t1231
matrix = [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]
rix = '\n'.join(str(e) for e in matrix)
print(rix)
rix2 = '\n'.join(map(str, matrix))
print(rix2)

print(a.replace('l', 'SUBSTITUTION', 1))  # HeSUBSTITUTIONlo What iS It1 (тип данных - str)
print(a.partition('ha'))  # ('Hello W', 'ha', 't iS It1') (выводит tuple - кортеж)
print(a.split('l', 1))  # ['He', 'lo What iS It1'] (преобразует в list - список)
# Особенности работы split(sep=None) с пробелами:
print('/as////df/'.split('/'), ' as    df '.split())  # ['', 'as', '', '', '', 'df', ''] ['as', 'df']
# Для проверки начала и конца строк startswith() и endswith() предпочтительнее,
# чем срезы, т. к. код более чистый и меньше вероятность возникновения ошибки.
print('Take'.startswith('T'))  # True
print('Take'.endswith(('ke', 't', 'a')))  # True (можно задать кортеж из проверяемых значений)
# В методе strip символы рассматриваются не как последовательность, а как набор символов, которые необходимо удалить:
print(",,,,,rrttgg.....banana....rrr".strip(",.grt"))  # banana
print(' \n \t  sdf  \t \n '.strip())  # sdf (по умолчанию удаление пробелов, табуляций и пустых строк)
# lstrip (удаление символов с начала строки), rstrip (с конца)

# проверка строк
print('abc123'.isalnum())  # True (состоит ли исходная строка из буквенно-цифровых символов)
print('abc$*123'.isalnum())  # False
print(''.isalnum())  # False
print('ABCabc'.isalpha())  # True (состоит ли исходная строка из буквенных символов)
print('abc123'.isalpha())  # False
print(''.isalpha())  # False
print('1234567'.isdigit())  # True (состоит ли исходная строка из цифровых символов)
print('abc123'.isdigit())  # False
print(''.isdigit())  # False
print('abc'.islower())  # True (являются ли все буквенные символы исходной строки строчными)
print('abc1$d'.islower())  # True (все неалфавитные символы игнорируются)
print('Abc1$D'.islower())  # False (также можно осуществлять проверку на isupper и т. д.)
print('       '.isspace())  # True (состоит ли исходная строка только из пробельных символов)
print('abc1$d'.isspace())  # False
print('Хочешь'.istitle())  # True
print('хочешь'.istitle())  # False
print(''.isprintable())  # вернёт True, если строка пустая, либо если все её символы могут быть выведены на печать
print(''.isprintable())  # False

# форматирование строк
print('a'.ljust(5, '*'))    # a****
print('ab'.ljust(5, '$'))   # ab$$$
print('abc'.ljust(5, '#'))  # abc##
print('a'.rjust(3))    #   a
print('ab'.rjust(3))   #  ab
print('abc'.rjust(3))  # abc
print(a[::-1].upper())  # 1TI SI TAHW OLLEH (все буквы становятся заглавными и задом наперёд)
print(a.capitalize())  # Hello what is it1 (первая буква заглавная, остальные строчные)
print(a.title())  # Hello What Is It1 (первая буква каждого слова заглавная)
print(a.swapcase())  # hELLO wHAT Is iT1 (замена регистра букв)
print(a.center(25, '%'))  # 1-ый аргумент - это длина результирующей строки, 2-ой - символ заполнение
print(a.capitalize().center(25, '1').upper().lower())  # методы строк выполняются по порядку

a = '6539834dfg!'
print(a * 3)  # 6539834dfg!6539834dfg!6539834dfg!
print(len(a))  # 11 (количество символов в переменной "а")
print('he' in a.lower())  # False (проверяет наличие символов в последовательности)
print(a[-1000:1000:100])  # 6 (срезами можно выходить за пределы объекта, ошибки не будет)
print(max(a), min(a))  # g ! (значения определяются по порядковому номеру символа в таблице ASCII)
x = sorted(a)  # строка конвертируется в список
print(x, type(x))  # ['!', '3', '3', '4', '5', '6', '8', '9', 'd', 'f', 'g'] <class 'list'>
print(list(a))  # ['6', '5', '3', '9', '8', '3', '4', 'd', 'f', 'g', '!']
print(set(a))  # {'8', '9', 'f', '6', '!', '5', 'g', '4', 'd', '3'} (удаление дубликатов)
print(a.split())  # ['6539834dfg!'] (аналогично [a])
print(str(a))  # 6539834dfg! (строковое представление объекта в неформальном виде (понятному человеку))
print(repr(a))  # '6539834dfg!' (строковое представление объекта в формальном виде (понятному интерпретатору Python))
'''

'''
# МОДУЛЬ STRING
from string import ascii_lowercase, ascii_uppercase, punctuation
print(punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(ord('A'), ord('a'))  # 65 97 (код символа в таблице символов Unicode)
print(list(chr(i) for i in range(ord('a'), ord('z') + 1)))  # ['a', 'b', 'c', 'd', 'e', 'f', ...] (вывод всех букв)
'''

'''
# ФОРМАТИРОВАНИЕ СТРОК
# f-строки, %, .format и т. д. более предпочтительные варианты форматирования, чем складывание строк,
# так как при каждом складывании создаются временные строки, что использует много памяти:
# "y" + " " + "e" + " " + "s" - в данном примере создаются 3 временные строки (количество операторов минус 1)
x = 5 / 3
a = 'Anthony'
b = 'Joshua'
print(f'Hello {a + " " + b}! You are {x ** 2 % 70} years old')  # наиболее функциональный вариант
print('Hello %s %s! You just delved into Python' % (b, a))  # выводит переменные по порядку
print('Hello {} {}! You just delved into Python'.format(a, b))  # выводит переменные по порядку
print('Hello {f_name} {s_name}! You just delved into Python'.format(f_name=a, s_name=b))
print('Hello {1} {0}! You just delved into Python'.format(a, b))  # выводит переменные по номерам
print(f'{x = }, {a=}')  # x = 5, a='Anthony'
print("{:,.2f}".format(10000001.23554))  # 10,000,001.24 (2f - 2 знака после запятой)
print(f'{5:02}')  # 05
'''

'''
# РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ (REGEX)
import re
target_string = "Emma is a basketball player who was born on June 17, 1993. " \
                "She played 112 matches with scoring average 26.12 points per game. " \
                "Her weight is 51 kg. -1711.23"
result = re.findall(r'\d', target_string)  # найти все цифры
print(result)  # ['1', '7', '1', '9', '9', '3', '1', '1', '2', '2', '6', '1', '2', '5', ...]
print(re.findall(r'[^\W\d_]', target_string))  # ['E', 'm', 'm', 'a', 'i', ...] (найти все буквы)
# Некоторые метасимволы необязательно экранировать если они внутри квадратных скобок:
print(re.findall(f'[\w.,+-/*^$]', '.,+-5/*^$f_'))  # ['.', ',', '+', '-', '5', '/', '*', '^', '$', 'f', '_']

# Жадные квантификаторы (?, *, +, {,5}, {2,5}, {5,} и т. д.) пытаются захватить как можно больше символов.
# Ленивые квантификаторы (если после квантификаторов: ?, *, +, {,5}, {2,5}, {5,} и т. д. стоит знак ?)
# пытаются захватить как можно меньше символов.
print(re.findall(r'".+?"', '"123" "." "/" "h" "  " ""'))  # поиск выражений, окружённых двойными кавычками

# Non-capturing group (?:) - скобочное выражение, которое группирует регулярное выражение,
# но не захватывает в него группу (предпочтительнее для экономии памяти):
print(re.findall(r'(?:\d.){2}', '5t7est54test43test3'))  # ['5t7e']; (?:\d.){2} аналогично \d.\d.

# ссылки назад
text = 'текст, в котором в котором несколько слов    слов повторяются, хотя они и не не должны повторяться повторяться.'
print(re.findall(r'(\b\w+\b) +\b\1\b', text))  # ['слов', 'не', 'повторяться']

# методы и атрибуты объекта match (для search, match, fullmatch при ненахождении шаблона в строке возвращается None)
# re.search() - ищет первое совпадение в строке;
# re.match() - то же самое, что и re.search(), но ищет совпадение с начала строки;
# re.fullmatch() - определяет полное соответствие строки переданному шаблону,
# если вся строка соответствует шаблону - выводит объект Match, иначе - None;
# re.finditer() - возвращает итератор Match объектов с вхождениями pattern в строке string (все вхождения).
res = re.search(r'(\d+)([a-z]+)(\d+)', 'aa123asd322sd43')
print(res.group(), res[0], res.group(0))  # res.group() аналогично res[0], аналогично res.group(0)
print(res.start())  # 2 (индекс начала совпадения)
print(res.end())  # 11 (индекс конца совпадения)
print(res.span())  # (2, 11) (кортеж с индексом начала и конца совпадения)
print(res.pos)  # 0 (позиция, с которой функция начинает искать совпадения)
print(res.endpos)  # 15 (позиция, до которой функция ищет совпадения)
print(res.re)  # re.compile('(\\d+)([a-z]+)(\\d+)'); регулярное выражение, использовавшееся для поиска
print(res.string)  # aa123asd322sd43 (строка, в которой искались совпадения)
print(res.span(2), res.groups(), res.group())  # (5, 8) ('123', 'asd', '322') 123asd322
# Метод groups возвращает кортеж со всеми группами, кроме нулевой.
# Нулевая группа - это полное совпадение регулярного выражения (123asd322).
# Если какая-либо группа ничего не нашла, то вместо найденного
# совпадения будет значение аргумента default (по умолчанию - None).

# использование именованных групп (поиск двух одинаковых численных последовательностей)
r = re.search(r'(?P<num1>\d+)(?P<num2>\1)(?P<num3>\s+)?', '0.12354578857887897')
print(r.group(), r.group(1), r.group('num1'), r.groups(default='No'))  # 57885788 5788 5788 ('5788', '5788', 'No')
print(r.groupdict(default=None))  # {'num1': '5788', 'num2': '5788', 'num3': None}; все захваченные именованные группы

# Функция findall возвращает список всех найденных совпадений.
# Если есть группирующие скобки, кроме (?:), то выводится кортеж значений внутри скобок:
print(re.findall(r'(\w+) = (\d+)', 'width = 20 and height = 10'))  # [('width', '20'), ('height', '10')]
# Функция split разбивает строки по заданному шаблону:
print(re.split(r'\s\d{3}\s', 'abc 123 def 456 fed 321 cba', maxsplit=2))  # ['abc', 'def', 'fed 321 cba']
# Если в шаблоне регулярного выражения используются группы, то их значения будут вставлены между разделёнными строками:
print(re.split(r'\s[+*=]\s', '2 + 2 * 2 = 6'))  # ['2', '2', '2', '6']
print(re.split(r'\s([+*=])\s', '2 + 2 * 2 = 6'))  # ['2', '+', '2', '*', '2', '=', '6']
# Функция sub заменяет найденные вхождения на заданные символы и возвращает исправленную строку:
print(re.sub(r'[a-z]{3}', '111', 'abc 123 def 456 fed 321 cba', 2))  # 111 123 111 456 fed 321 cba
# Замена числа и месяца в дате, использую группы:
print(re.sub(r'(\d{2}[./])(\d{2}[./])(\d{4})', r'\2\1\3', 'Сегодня 04/24/2022.'))  # Сегодня 24/04/2022.
print(re.sub(r'(\d{2}[./])(\d{2}[./])(\d{4})', r'\g<2>\g<1>\g<3>', 'Сегодня 04/24/2022.'))  # \g<2>\g<1>\g<3> = \2\1\3
# В качестве заменяемой подстроки можно использовать функцию:
result = re.sub(r'\w+', lambda m: m.group().upper(), "ThiS WORLD doesN'T need A HeRo")
print(result)  # THIS WORLD DOESN'T NEED A HERO
# Функция subn выполняет ту же операцию, что sub, но возвращает кортеж (последний аргумент - количество замен):
print(re.subn(r'[a-z]{3}', '111', 'abc 123 def 456 fed 321 cba'))  # ('111 123 111 456 111 321 111', 4)
# Функция escape экранирует спецсимволы:
print(re.escape(r'https://stepik.org/lesson/42/step/1?unit=69'))  # https://stepik\.org/lesson/42/step/1\?unit=69
# Функция compile предварительно компилирует регулярное выражение и
# специальный объект, который можно повторно использовать позже:
regex_obj = re.compile('ba[rz]', flags=re.I)
print(regex_obj, type(regex_obj))  # re.compile('ba[rz]', re.IGNORECASE) <class 're.Pattern'>
result1 = re.search('ba[rz]', 'FOOBARBAZBAR', flags=re.I)
result2 = re.search(regex_obj, 'FOOBARBAZBAR')  # аналогично предыдущему
result3 = regex_obj.search('FOOBARBAZBAR')  # аналогично предыдущему
print(result1)  # <re.Match object; span=(3, 6), match='BAR'>
print(result2)  # <re.Match object; span=(3, 6), match='BAR'>
print(result3)  # <re.Match object; span=(3, 6), match='BAR'>
print(regex_obj.search('FOOBARBAZBAR', pos=4, endpos=10))  # <re.Match object; span=(6, 9), match='BAZ'>

# условие yes/no; (condition)(?(n)yes|no)
# Если у группы "n" нашлись совпадения - возвращается шаблон до |,
# в противном случае возвращается шаблон после |. Шаблон после | необязателен и может быть опущен.
# regex = r'(a)?(?(1)b|c)'
# Группа (a)? ищет букву "a". К группе применён квантификатор ?, т. к. этой буквы может не быть в тексте.
# Если в первой группе нашлась буква a, то условие (?(1)b|c) ищет букву "b",
# если первая группа ничего не нашла, то условие ищет букву "c".
# В нижеуказанном примере регулярное выражение найдёт все "ab" и "c" в тексте:
match = re.finditer(r'(a)?(?(1)b|c)', 'ab7c98acb2abc09cba')
for i in match:
    print(i)  # <re.Match object; span=(0, 2), match='ab'> (если совпадений нет, то ничего не выводит)
match = re.search(r'\+?\d(\()?\d{3}(?(1)\)|)\d{7}', 'gfd+7(978)6655917fg')  # поиск корректных номеров телефонов
print(match)  # <re.Match object; span=(3, 17), match='+7(978)6655917'> (при отсутствии совпадений выводит None)
print(match[0])  # +7(978)6655917 (также регулярное выражение найдёт +79786655917)
print(match.re)  # re.compile('\\+?\\d(\\()?\\d{3}(?(1)\\)|)\\d{7}')

# lookahead & lookbehind
# positive lookahead (?=) проверяет, что переданное выражение стоит после шаблона; не захватывает никаких символов
# negative lookahead (?!) проверяет, что переданное выражение не стоит после шаблона; не захватывает никаких символов
# positive lookbehind (?<=) проверяет стоит ли переданное выражение перед шаблоном; не захватывает никаких символов
# negative lookbehind (?<!) проверяет, что переданное выражение не стоит перед шаблоном; не захватывает никаких символов
result2 = re.findall(r'(?<!\S)-?\d+\.?\d*\b', target_string)  # выводит числа в строке
print(result2)  # ['17', '1993', '112', '26.12', '51', '-1711.23']
print(re.findall(r'(?<=\d)(?<!4)test(?=\d)(?!3)', '5test54test43test3'))  # ['test']
# Все выражения в lookbehind должны быть фиксированной длины, иначе будет ошибка:
# r'(?<=test{0,})regex' или r'(?<=g?)regex' или r'(?<!Python+)regex' вызовут ошибку;
# (?<=hi!|long_text) или (?<![abcdef]|\d{4}) или (?<=\w\s|\W) вызовут ошибку.
# Альтернативная запись вышеуказанных выражений, которая не вызовет ошибку:
# (?:(?<=hi!)|(?<=long_text)) или (?:(?<![abcdef])|(?<=\d{4})) или (?:(?<=\w\s)|(?<=\W)) не вызовут ошибку.
# В lookahead можно спокойно ставить условия с шаблонами разной длины, ошибок не будет.
# Положение lookahead (lookbehind) в регулярном выражении важно,
# проверка идёт после (или перед) шаблона, после которого стоит lookahead (lookbehind):
reg = r'\[(?:\d+(?!\s*\d+)\s*,?\s*)+\]|' \
      r'\[\]'
string = '[1, 23, ][2]лдл [][ [  ] [402030, 404040] ][ [1 2 3 4]'  # найти перечисления в квадратных скобках
print(re.findall(reg, string))  # ['[1, 23, ]', '[2]', '[]', '[402030, 404040]']

# флаги (flags)
print(re.findall(r'привет', 'привет ПРИВЕТ пРиВеТ', flags=re.I))  # ['привет', 'ПРИВЕТ', 'пРиВеТ']
print(re.findall(r'привет', 'привет ПРИВЕТ пРиВеТ', flags=re.IGNORECASE))  # аналогично предыдущему
print(re.findall(r'(?i)привет', 'привет ПРИВЕТ пРиВеТ'))  # аналогично предыдущему
# re.MULTILINE - при использовании флага спецсимволы ^ и $ будут совпадать
# не с началом и концом всего текста, а с началом и концом строк
string = """
I like flags
I like flags
I like flags
"""
print(re.findall(r'^I like flags$', string))  # []
print(re.findall(r'^I like flags$', string, flags=re.M))  # ['I like flags', 'I like flags', 'I like flags']
# re.DOTALL - точка теперь будет соответствовать любому символу
# Если флаг не используется - точка соответствует любому символу, кроме символа новой строки.
# Флаги можно складывать:
test1 = re.findall('f+', '\nf\nF\nf\nF\n', flags=re.MULTILINE + re.IGNORECASE + re.DOTALL)
test2 = re.findall('f+', '\nf\nF\nf\nF\n', flags=re.MULTILINE | re.IGNORECASE | re.DOTALL)  # аналогично предыдущему
print(test1, test2)  # ['f', 'F', 'f', 'F'] ['f', 'F', 'f', 'F']
'''

'''
# КОРТЕЖИ (TUPLE)
# Основное отличие кортежей от списков - невозможность изменять элементы кортежа.
a = 4, 2, 6, 3, 1, 10, 54
# a[1] = 2 выдаёт ошибку, т. к. в отличие от списка в кортеже нельзя менять элементы
print(sorted(a))  # [1, 2, 3, 4, 6, 10, 54] (конвертация в список)
print(tuple(reversed(a)))  # (54, 10, 1, 3, 6, 2, 4)
print(min(a, default=None))  # 1
print(max(a, default='Error'))  # 54
print(sum(a))  # 80
print(sum(tuple(range(1, 101, 1))))  # 5050 (вместо 'tuple' можно использовать 'list' и т. д.)
print(sum(range(1, 101, 1)))  # 5050

a = ([], "а", "п", "б", ('a', 'd', 'f',), 'r', '1', 'aaa', 'aa')
print(a[4][2])  # f (для вывода кортежа в кортеже)
a[0].append(2)  # если внутри кортежа есть изменяемые элементы, то их можно менять
# однако a[0] += [1] вызовет ошибку (TypeError: 'tuple' object does not support item assignment)
print(a + (1, 2))  # ([2], 'а', 'п', 'б', ('a', 'd', 'f'), 'r', '1', 'aaa', 'aa', 1, 2)
print(1, 2, 3)  # 3 числа
print((1, 2, 3))  # кортеж
c = ('ooo',)  # задание кортежа из одного элемента (по PEP 8 пробел между конечной запятой и скобкой не ставится)
print(a + c)  # ([2], 'а', 'п', 'б', ('a', 'd', 'f'), 'r', '1', 'aaa', 'aa', 'ooo')
'''

'''
# СПИСКИ (LIST)
a = [1, 2, 'g', 4, True, 0, False]
a.append([3, 1])  # принимает один аргумент и добавляет его в конец списка
print('append:', a)  # append: [1, 2, 'g', 4, True, 0, False, [3, 1]]
a.insert(2, 'd')  # вставляет элемент в указанный индекс
print('insert:', a)  # insert: [1, 2, 'd', 'g', 4, True, 0, False, [3, 1]]
a.extend([6, 'd'])  # итерирует один объект, затем добавляет элементы по одному в конец списка
print('extend:', a)  # extend: [1, 2, 'd', 'g', 4, True, 0, False, [3, 1], 6, 'd']
popped_item = a.pop(1)  # удаляет элемент указанного индекса
print('popped_item is', popped_item)  # popped_item is 2
# если аргумент не передан, то удаляется последний элемент (a.pop())
print(a)  # [1, 'd', 'g', 4, True, 0, False, [3, 1], 6, 'd']
del a[1]
print(a)  # [1, 'g', 4, True, 0, False, [3, 1], 6, 'd']
a.remove('g')  # удаляет первое вхождение элемента, если элемента нет, то ошибка
print(a)  # [1, 4, True, 0, False, [3, 1], 6, 'd']
a.remove(True)  # True приводится к 1, поэтому удаляются 1 и True
print(a)  # [4, True, 0, False, [3, 1], 6, 'd']
a.remove(True)
print(a)  # [4, 0, False, [3, 1], 6, 'd']
a.remove(False)  # False приводится к 1, поэтому удаляются 0 и False
print(a)  # [4, False, [3, 1], 6, 'd']
a.remove(False)
print(a)  # [4, [3, 1], 6, 'd']
a.reverse()  # разворачивает список задом наперёд, либо print(list(reversed(a)))
print(a)  # ['d', 6, [3, 1], 4]
a = [3, 6, 2, 8, 9]
a.sort()  # сортирует список в порядке возрастания, в порядке убывания a.sort(reverse=True)
print(a)  # [2, 3, 6, 8, 9]
print(sum(a), max(a), min(a))  # 28 9 2
b = a[:]  # или b = a.copy() (поверхностное копирование списка, b = a список не копирует, а делает на него ссылку)
del a[0:2]  # при удалении элементов в "а" элементы в "b" не удаляются
print(a)  # [6, 8, 9]
print(b)  # [2, 3, 6, 8, 9]
b[1:4:2] = ['f', 'f']  # можно изменять срезы в списках
print(b)  # [2, 'f', 6, 'f', 9]
print(9 in a)  # True
print(a + [4] * 2)  # [6, 8, 9, 4, 4]
a.clear()
print(a, type(a))  # [] <class 'list'>

words = ['xyz', 'zara', 'beegeek', 'Zara', 'zar']
print(max(words))  # zara (сравнение строк происходит посимвольно по коду ASCII (функция ord()))

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[rainbow.index('Green')] = 'Зеленый'  # замена элемента, зная только сам элемент без индекса
rainbow[rainbow.index('Violet')] = 'Фиолетовый'
print(rainbow)  # ['Red', 'Orange', 'Yellow', 'Зеленый', 'Blue', 'Indigo', 'Фиолетовый']

words1 = ['iq option', 'stepik', 'beegeek']
words2 = ['iq option', 'stepik', 'beegeek']
words1.append('python')  # объект добавляется в конец списка
words2.extend('python')  # объект итерируется, затем элементы добавляются по одному в конец списка
print(words1)  # ['iq option', 'stepik', 'beegeek', 'python']
print(words2)  # ['iq option', 'stepik', 'beegeek', 'p', 'y', 't', 'h', 'o', 'n']

numbers = ['sdf', 0, '5775', 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*numbers, sep='')  # sdf0577511112345678910
print(numbers.index(4))  # 9 (индекс первого вхождения значения)
print(numbers.count(1))  # 4

my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
f = sum(my_list, [])  # преобразование в одномерный список
print(f)  # [1, 9, 8, 7, 4, 7, 3, 4, 2, 1]

d = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
days = [(i, d[i % len(d)]) for i in range(1, 78)]  # бесконечный проход по списку
for i in days:
    print(i)
'''

'''
# ГЕНЕРАТОРЫ СПИСКОВ (LIST COMPREHENSION)
# работают быстрее, чем цикл for с использованием метода append(), но медленнее, чем функция list(iterable)
result = [i ** 3 for i in range(1, 100)]
# отобразим последние 5 значений с помощью слайсинга (среза):
print(result[-5:])  # [857375, 884736, 912673, 941192, 970299]

# создание матрицы
n, m = 3, 4  # n - строки, m - столбцы
my_list = [[0] * m for _ in range(n)]  # создание вложенного списка
print(*my_list, sep='\n')
a = [[0] * m] * n  # Неправильное создание вложенного списка,
a[0][0] = 5  # так как при изменении одного элемента, меняются все элементы столбца.
print(*a)  # [5, 0, 0, 0] [5, 0, 0, 0] [5, 0, 0, 0]

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
d = sum([a[i] * b[i] for i in range(len(a))]) if len(a) == len(b) else "error"
print(d)  # 30

if len(a) == len(b):  # аналогично предыдущему
    d = sum([i * j for i, j in zip(a, b)])
    print(d)
else:
    print('error')

print(*[i if i % 2 == 0 else 'NO' for i in range(10)])  # если есть else, то if ставится до for
print(*[i for i in range(10) if i % 2 == 0])  # если нет else, то if ставится после for
print('F' if len(a) == 1 else 'G' if len(a) == 2 else 'H')  # альтернативная запись elif
a = [i * j for i in [2, 3, 4, 5] for j in [1, 2, 3] if i * j >= 10]
print(a)  # [12, 10, 15]
a, b = 1, 5
print([i ** 2 for i in range(a, b + 1)] if a <= b else [i ** 3 for i in range(a, b - 1, -1)])
print([i ** 2 for i in range(a, b + 1)] or [i ** 3 for i in range(a, b - 1, -1)])  # аналогично предыдущему
matrix = [[j for j in range(6)] for i in range(4)]
print(matrix)  # [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]]
squares = [number ** 2 for row in matrix for number in row]
print(squares)  # [0, 1, 4, 9, 16, 25, 0, 1, 4, 9, 16, 25, 0, 1, 4, 9, 16, 25, 0, 1, 4, 9, 16, 25]
'''

'''
# МНОЖЕСТВА (SET)
# Элементом множества не может быть неизменяемый тип данных (список, другое множество, словарь).
# Так как элементы множества не индексируются, то они не поддерживают никаких операций
# среза и индексирования, однако множество можно обойти по элементам через цикл for.
s = set([1, 3, 2, 'rr'])  # аналогично s = {1, 3, 2, 'rr'}
print(s, type(s))  # {1, 2, 3, 'rr'} <class 'set'>
print(1 in s)  # True
print(3 not in s)  # False
print({1, 2, 3}.isdisjoint({6, 7, 8}))  # True (проверка на пустоту пересечения)
print({1, 2}.issubset({1, 2, 3, 4}))  # True (является ли подмножеством)
print({1, 2, 3, 4, 5}.issuperset({1, 2, 3, 4}))  # True (обратное)
print({1, 2, 3, 10} >= {10})  # True (является ли подмножеством, аналогично предыдущему)

# операции, возвращающие новые множества
print({1, 2, 3, 4} | {1, 2, 6, 7})  # {1, 2, 3, 4, 6, 7} (объединение множеств)
print({1, 2, 3, 4}.union({1, 2, 6, 7}))  # аналогично предыдущему
print({1, 2, 3, 4, 5} & {1, 2, 3} & {2, 3, 4})  # пересечение множеств (оставить общие элементы)
print({1, 2, 3, 4, 5}.intersection({1, 2, 3}).intersection({2, 3, 4}))  # аналогично предыдущему
print({2, 3, 4, 4, 5, 6, 7, 8} - {2, 3, 4, 100})  # {8, 5, 6, 7} (разность множеств)
print({2, 3, 4, 4, 5, 6, 7, 8}.difference({2, 3, 4, 100}))  # аналогично предыдущему
print({1, 3} ^ {2, 3, 6})  # {1, 2, 6} (выводятся не пересекающиеся элементы; пересекающиеся удаляются)
print({1, 3}.symmetric_difference({2, 3, 6}))  # аналогично предыдущему 

# операции, изменяющие текущие множества
a = set([1, 2, 3])
a.update({4, 5, 6})  # добавление множества к множеству
print(a)  # {1, 2, 3, 4, 5, 6}
a |= {6, 7, 8}  # аналогично предыдущему
print(a)  # {1, 2, 3, 4, 5, 6, 7, 8}
a.intersection_update({2, 3})  # оставить в множестве элементы, содержащиеся в обоих множествах
print(a)  # {2, 3}
a &= {3}  # та же операция, другой синтаксис (оставить общие элементы)
print(a)
a = {1, 2, 3}
a -= {2}
print(a)  # {1, 3}
a.difference_update({3})  # та же операция, другой синтаксис
print(a)  # {1}
a = {1, 2, 3}
b = {2, 3, 4}
a ^= b  # оставить в множестве элементы, присутствующие в одном из двух, но не обоих (уникальные)
# a.symmetric_difference_update(b) аналогично предыдущему
print(a)  # {1, 4}

a = {100, 2}
a.add(6)
print(a)  # {2, 100, 6}
a.add(None)
print(a)  # {2, 100, 6, None}
a.discard(12)  # если элемента нет, то ошибка не выводится
print(a)  # {2, 100, 6, None}
a.remove(100)  # если элемента нет, то выводится ошибка
print(a)  # {2, 6, None}
a.clear()  # удаление всех элементов
print(a)  # set()
a = {1, 2, 3, 4}
returned = a.pop()  # удаляет случайный элемент множества
print(returned)  # выводит удалённый элемент
a.pop()
print(a)

myset = {'python'}
myset2 = set('python')
print(myset)   # {'python'}
print(myset2)  # {'p', 'o', 'h', 't', 'y', 'n'}

a = {1, 2, 3, 4}
b = 'bcd'
# a |= b  TypeError: unsupported operand type(s) for |=: 'set' and 'str'
c = a.union(b)
print(c)  # {1, 2, 3, 4, 'b', 'd', 'c'}
a.update(b)  # аналогично c = a.union(b) и c = a | set(b)
print(a)  # {1, 2, 3, 4, 'b', 'd', 'c'}

# удаление дубликатов и вывод уникальных элементов по порядку
s = 'hello_world!'
print(*sorted(set(s), key=s.index), sep='')  # helo_wrd!
print(''.join(sorted(set(s), key=s.index)))  # helo_wrd!
'''

'''
# СЛОВАРИ (DICTIONARY)
d = dict()  # либо d={}
key = 'b'  # ключ - неизменяемый тип данных (не может быть список, множество, словарь)
value = 100  # значение - любой тип данных (изменяемый или неизменяемый)
d[key] = value
print(d)  # {'b': 100}
# Способ создания словаря только если ключ является строковым типом
# (использование чисел или иных типов данных приведёт к ошибке):
r = dict(msk=495, spb=812, nsk=383)  
print(r)  # {'msk': 495, 'spb': 812, 'nsk': 383}
d = {
    'зарплаты': {'Петя': 100000, 'Аня': 100000},
    'проекты': ['разработка нормальной БД'],
    's': 334
    }
print(d)
print(d.get('про', 'NO INFO'))  # если ключа нет, вернёт None, либо 2-ой аргумент (если указан)
del d['проекты']  # если ключа нет, выведет ошибку
print(d)  # {'зарплаты': {'Петя': 100000, 'Аня': 100000}, 's': 334}
p = d.pop('s', None)  # если удаляемого ключа нет, выводится 2-ой аргумент, если его нет, то выводится ошибка
print(p)  # 334 (выводит только значение, однако удаляются ключ и значение)
print(d)  # {'зарплаты': {'Петя': 100000, 'Аня': 100000}}
d.update({'f': 1})  # либо d['f'] = 1
print(d)  # {'зарплаты': {'Петя': 100000, 'Аня': 100000}, 'f': 1}
print(d.keys(), type(d.keys()))  # dict_keys(['зарплаты', 'f']) <class 'dict_keys'>
print(list(d.keys()))  # ['зарплаты', 'f']
print(d.values(), type(d.values()))  # dict_values([{'Петя': 100000, 'Аня': 100000}, 1]) <class 'dict_values'>
print(tuple(d.values()))  # ({'Петя': 100000, 'Аня': 100000}, 1)
print(d.items())  # dict_items([('зарплаты', {'Петя': 100000, 'Аня': 100000}), ('f', 1)]) (кортежи ключ-значение)
print(list(d.items()))  # [('зарплаты', {'Петя': 100000, 'Аня': 100000}), ('f', 1)]
d = {a: a ** 2 for a in range(7, 0, -1)}  # dict comprehension
print(d)  # {7: 49, 6: 36, 5: 25, 4: 16, 3: 9, 2: 4, 1: 1}
d_copy = d.copy()  # создание копии словаря
popped_item = d.popitem()  # удаляет последний добавленный ключ со значением
print(popped_item)  # (1, 1) (кортеж ключ-значение)
print(d)  # {7: 49, 6: 36, 5: 25, 4: 16, 3: 9, 2: 4}
d.clear()
print(d)  # {}
print(d_copy)  # {7: 49, 6: 36, 5: 25, 4: 16, 3: 9, 2: 4, 1: 1}
# Метод setdefault позволяет получить значение из словаря по заданному ключу,
# автоматически добавляя элемент в словарь, если он отсутствует:
print(d_copy.setdefault(7, 1000))  # вернёт 49, т. к. значение для ключа 7 существует
print(d_copy.setdefault(8, 64))  # 64 (создаётся новая пара ключ-значение)
print(d_copy.setdefault(9))  # значение будет None, т. к. оно не передано
print(d_copy)  # {7: 49, 6: 36, 5: 25, 4: 16, 3: 9, 2: 4, 1: 1, 8: 64, 9: None}
d_copy[777] = d_copy.pop(7)  # замена ключа, значение остаётся прежним, ключ добавляется в конец словаря
print(d_copy)  # {6: 36, 5: 25, 4: 16, 3: 9, 2: 4, 1: 1, 8: 64, 9: None, 777: 49}

dict_1 = {'John': 15, 'Rick': 10, 'Misa': 12}
dict_2 = {'Bonnie': 18, 'Rick': 20}
dict_3 = dict_1 | dict_2  # объединение словарей, аналогично {**dict_1, **dict_2}
# Если в словарях присутствуют одинаковые ключи, то значение берётся из последнего словаря:
print(dict_3)  # {'John': 15, 'Rick': 20, 'Misa': 12, 'Bonnie': 18}
print(*dict_3)  # John Rick Misa Bonnie
print({*dict_3}, type({*dict_3}))  # {'John', 'Rick', 'Misa', 'Bonnie'} <class 'set'>
print({**dict_1, **dict_2})  # {'John': 15, 'Rick': 20, 'Misa': 12, 'Bonnie': 18} (распаковка словаря)

a, b, c = 'qwert', 'zz', 'wthgrttt'
d = {len(a): a, len(b): b, len(c): c}
print(d)  # {5: 'qwert', 2: 'zz', 8: 'wthgrttt'}
print(d[min(d)], d[max(d)], sep=' & ')  # zz & wthgrttt
print(min(d), len(a), a)  # 2 5 qwert

# При сравнении словарей порядок элементов не важен:
print({'one': 1, 'two': 2} == {'two': 2, 'one': 1})  # True (сравниваются и ключи и значения)

# создание словарей
print(dict.fromkeys([1, 2, 3]))  # {1: None, 2: None, 3: None}
dict1 = dict.fromkeys(['name', 'age', 'job'], 'Missed info')  # создание словаря с одним и тем же значением
print(dict1)  # {'name': 'Missed info', 'age': 'Missed info', 'job': 'Missed info'}
info_tuple = (['name', 'Timur'], ['age', 28], ['job', 'Teacher'])  # кортеж списков
info_dict = dict(info_tuple)  # создание словаря на основе кортежа списков (или списка кортежей и т. д.)
print(info_dict)  # {'name': 'Timur', 'age': 28, 'job': 'Teacher'}
print(info_dict['name'])  # Timur

# создание словарей с помощью функции zip
keys = ['name', 'age', 'gender']
values = ['Timur', 28, 'male']
info = dict(zip(keys, values))
print(info)  # {'name': 'Timur', 'age': 28, 'gender': 'male'}

# поменять местами ключ и значение в словаре
new_info = {v: k for k, v in info.items()}
print(new_info)  # {'Timur': 'name', 28: 'age', 'male': 'gender'}

a = ['S1', 'S2', 'S3', 'S4']
b = ['Cami', 'Juan', 'Dan', 'Sam', 'Bati']
c = [86, 98, 89, 92]
result = [{i: {k: j}} for i, k, j in zip(a, b, c)]
print(result)  # [{'S1': {'Cami': 86}}, {'S2': {'Juan': 98}} и т. д.]

# подсчёт количества элементов в объекте с помощью словаря
text = 'footballcyberpunkextraterritorialityconversationalistblockterdependencemamauserfff'
result = {}
for c in text:
    result[c] = result.get(c, 0) + 1
print(result)  # {'f': 4, 'o': 6, 't': 8, 'b': 3, 'a': 7, 'l': 5, ...}
print(sorted(result.items()))  # [('a', 7), ('b', 3), ('c', 4), ('d', 2), ...]
result_2 = {k: v for k, v in sorted(result.items())}  # сортировка по ключам в алфавитном порядке
print(result_2)  # {'a': 7, 'b': 3, 'c': 4, 'd': 2, 'e': 10, 'f': 4, ...}
result_3 = {x: y for x, y in sorted(result.items(), key=lambda x: -x[1])}  # сортировка по убыванию значений словаря
print(result_3)  # {'e': 10, 't': 8, 'r': 8, 'a': 7, 'o': 6, 'l': 5, 'n': 5, ...}

res = {}
for letter in text:
    res.setdefault(letter, {}).setdefault(text.count(letter), []).append(letter)  # создание вложенных словарей
print(res)  # {'f': {4: ['f', 'f', 'f', 'f']}, 'o': {6: ['o', 'o', 'o', 'o', 'o', 'o']}, ...}
'''

'''
# МОДУЛЬ COLLECTIONS
from collections import namedtuple  # именованные кортежи (занимают меньше памяти и работают быстрее, чем словари)
# namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
# В качестве field_names можно использовать: список, словарь, кортеж,
# множество (не рекомендуется, т. к. неупорядоченно), любой итерируемый объект.
Person = namedtuple('Person', ['name', 'age', 'marks'])
timur = Person('Тимур', 29, [5, 5])
timur.marks.append(4)
name, age, marks = timur  # распаковка кортежа
print(timur, type(timur))  # Person(name='Тимур', age=29, height=170) <class '__main__.Person'>
print(name, timur.marks)  # Тимур [5, 5, 4]
print(timur.age, timur[1])  # 29 29 (timur.age аналогично timur[1])
print(timur._fields)  # ('name', 'age', 'marks') (кортеж строк с именами полей)
tom = Person._make(['Tom', 15, [4, 4]])  # либо tom = Person.(*['Tom', 15, [4, 4]])
print(tom)  # Person(name='Tom', age=15, marks=[4, 4])
print(tom._asdict())  # {'name': 'Tom', 'age': 15, 'marks': [4, 4]} (преобразование именованного кортежа в словарь)
tom_2 = tom._replace(age=14)
print(tom_2)  # Person(name='Tom', age=14, marks=[4, 4])

# Параметр rename (меняет название полей если это зарезервированные ключевые слова):
headers = ('name', 'surname', 'age', 'class')
Student = namedtuple('Student', headers, rename=True)
stud = Student('Роман', 'Белых', 26, 10)
print(stud)  # Student(name='Роман', surname='Белых', age=26, _3=10)

# Параметр default (устанавливает значения по умолчанию):
Point = namedtuple('Point', ('x', 'y'), defaults=(0, 0))
point1 = Point()
point2 = Point(1, 9)
print(point1)  # Point(x=0, y=0)
print(point2)  # Point(x=1, y=9)
print(Point._field_defaults)  # {'x': 0, 'y': 0}

from collections import defaultdict
# В отличие от обычных словарей если нет ключа, то создаёт ключ со значением по умолчанию (для int равен 0).
# Создание новых пар ключ-значение, используя defaultdict быстрее, чем методы setdeafult() и get() для словарей.
info = defaultdict(int, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
print(info['name'])  # Timur
print(info['salary'])  # 0
print(info)  # defaultdict(<class 'int'>, {'name': 'Timur', 'age': 29, 'job': 'Teacher', 'salary': 0})

# подсчёт элементов
numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
result = defaultdict(int)
for num in numbers:
    result[num] += 1
print(result)  # defaultdict(<class 'int'>, {9: 1, 8: 1, 32: 2, 1: 5, 10: 4, 23: 3, 4: 2, 2: 6})

result = defaultdict(list)
for num in numbers:
    result[num].append(num)
print(result)  # defaultdict(<class 'list'>, {9: [9], 8: [8], 32: [32, 32], 1: [1, 1, 1, 1, 1], ...})

# Значение по умолчанию можно задать функцией двумя способами:
# 1-ый способ (используя lambda-выражение):
info = defaultdict(lambda: '1000000$', {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
print(info['name'])  # Timur
print(info['salary'])  # 1000000$


# 2-ой способ (используя стандартную функцию):
def get_default():
    return 69000


info = defaultdict(get_default, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
print(info['name'])  # Timur
print(info['salary'])  # 69000

from collections import Counter  # написан на языке С, поэтому работает быстро
# наследуют все методы словарей, кроме fromkeys()
letters = Counter('mississippi')
print(letters)  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
letters.update('missouri')
print(letters)  # Counter({'i': 6, 's': 6, 'm': 2, 'p': 2, 'o': 1, 'u': 1, 'r': 1})
counter = Counter(i=2, m=1)
print(counter)  # Counter({'i': 2, 'm': 1})
letters.update(counter)
print(letters)  # Counter({'i': 8, 's': 6, 'm': 3, 'p': 2, 'o': 1, 'u': 1, 'r': 1})
print(letters.most_common())  # [('i', 8), ('s', 6), ...] (возвращает список, отсортированный по убыванию значений)
print(letters.most_common(3))  # [('i', 8), ('s', 6), ('m', 3)] (выводит количество самых повторяемых элементов)
print(letters.most_common()[-3:])  # [('o', 1), ('u', 1), ('r', 1)] (самые редко повторяемые)
print(list(letters.elements()))  # ['m', 'm', 'm', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', ...]
print(letters.total())  # 22 (вычисляет сумму всех значений)
letters.subtract('i' * 100)  # вычитание словарей (принимает любой итерируемый объект)
print(letters)  # Counter({'s': 6, 'm': 3, 'p': 2, 'o': 1, 'u': 1, 'r': 1, 'i': -92})

# операторы &, |, +, -
counter1 = Counter(i=10, s=40, p=10, m=1)
counter2 = Counter(i=2, s=8, p=10, m=3)
print(counter1 & counter2)  # Counter({'p': 10, 's': 8, 'i': 2, 'm': 1})  (возвращает минимумы значений)
print(counter1 | counter2)  # Counter({'s': 40, 'i': 10, 'p': 10, 'm': 3})  (возвращает максимумы значений)
print(counter1 + counter2)  # Counter({'s': 48, 'p': 20, 'i': 12, 'm': 4})
print(counter1 - counter2)  # Counter({'s': 32, 'i': 8}) (нулевые и отрицательные элементы исключаются)

# использование унарных операторов + и -
counter = Counter(a=5, b=-9, c=0)
print(counter)  # Counter({'a': 5, 'c': 0, 'b': -9})
print(+counter)  # Counter({'a': 5}) (выводит положительные элементы)
print(-counter)  # Counter({'b': 9}) (выводит отрицательные элементы)

# Сравнение рассматривает нулевые значения как отсутствующие:
counter1 = Counter(i=4)
counter2 = Counter(s=0, i=4)
print(counter1 == counter2)  # True

# Допускается складывание строк и других объектов:
counter1 = Counter(i=4, s='4')
counter2 = Counter(i=5, s='5')
counter1.update(counter2)
print(counter1)  # Counter({'i': 9, 's': '54'}) (складывает строки в обратном порядке)
'''

'''
# RANGE ОБЪКТЫ, ИТЕРИРУЕМЫЕ ОБЪЕКТЫ, ИТЕРАТОРЫ, ГЕНЕРАТОРЫ
# Объект типа range не хранит весь набор чисел, он создает новое число "на лету" только тогда, когда оно потребуется,
# при этом старые значения не хранятся. Размер объектов range не зависит от количества чисел, которые предполагается
# перебрать, нужно помнить только начальное и конечное значения последовательности, шаг и текущее значение.
import copy
x = range(10 ** 10)  # range объекты занимают меньше места в памяти (всегда 48 байт), чем списки
print(x[4])  # 4 (объекты range поддерживают индексацию и срезы)
print(x == range(10 ** 10))  # True
print(x.index(0), x.count(3))  # 0 1
print(x, len(x), type(x))  # range(0, 10000000000) 10000000000 <class 'range'>

# Итерируемый объект - объект, который можно итерировать, то есть 
# проходиться по нему, перебирая каждый элемент раз за разом.
# У всех итерируемых объектов есть магический метод __iter__(), который преобразует итерируемый 
# объект в итератор. Встроенная функция iter() вызывает за кулисами именно этот магический метод.
# Итератор - это любой объект, реализующий метод __next__() (map, filter, zip, enumerate, reversed).
# Использование итераторов приводит к выигрышу с точки зрения потребляемой памяти,
# однако при этом замедляется скорость программы.
# Элементы итератора можно обойти только один раз. Нельзя найти длину или обратиться к индексу итератора.
# Списки, словари, кортежи, множества, строки, range объекты являются итерируемыми объектами, однако
# не являются итераторами, для их преобразования в итератор используется встроенная функция iter():
sp = iter([1, 2, 3, 4, 5])  # преобразование списка и итератор
sp2 = copy.copy(sp)
print(sp, type(sp))  # <list_iterator object at 0x0000024DF5CEFF10> <class 'list_iterator'>
print(sum(sp))  # 15
# При повторном выводе получим 0, т. к. по элементам итератора sp уже проитерировалась первая функция sum:
print(sum(sp))  # 0
print(4 in sp2)  # True (на этом моменте в итераторе остался только последний элемент "5")
print(next(sp2))  # 5
print(1 in sp2)  # False (на этом моменте итератор пуст)
from_10_to_20 = iter(range(10, 21))
copy1 = from_10_to_20  # ссылка на итератор
copy2 = copy.copy(from_10_to_20)  # копия итератора
print(from_10_to_20, type(from_10_to_20))  # <range_iterator object at 0x000001F31ED8DF50> <class 'range_iterator'>
print(next(from_10_to_20))  # 10
print(next(from_10_to_20))  # 11
print(next(from_10_to_20))  # 12
for value in from_10_to_20:  # проход оставшихся элементов с 13 по 20
    print(value)
# Можно передать второй аргумент, который будет возвращен вместо возбуждения исключения
# StopIteration, если в итераторе больше не осталось элементов:
print(next(from_10_to_20, 'end'))  # end
print(next(copy1, 'there is no elements'))  # there is no elements (т. к. все элементы проитерированы в from_10_to_20)
print(next(copy2, 'there is no elements'))  # 10

# Генератор - это итератор, но не наоборот. Не любой итератор является генератором.
# Генератор - частный случай итератора.
# Существует 2 способа создания генератора:
# (1) генераторное выражение, например, (i ** 2 for i in range(1, 6))
# (2) генераторные функции - это функции, где есть хотя бы одно ключевое слово yield
b = (i ** 2 for i in range(1, 6))  # generator comprehension (создание генератора)
print(b, type(b))  # <generator object <genexpr> at 0x00000194BDFD1E70> <class 'generator'>


# Функция-генератор (экономит память) - это функция, которая может возвращать по
# одному значению, при этом «замораживая» своё выполнение.
# При новом вызове функции она будет выполняться с того места, на котором остановилась.
def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
        yield i  # метод next() замораживает функцию на этом месте (все локальные переменные сохраняются)
        yield pr  # функция начнёт выполняться с этого места при следующем вызове метода next()
        # return 13  # StopIteration: 13 (прерывает работу генератора, при этом само значение 13 не выводится)


for j in fact(5):
    print(j, end=' | ')  # 1 | 1 | 2 | 2 | 3 | 6 | 4 | 24 | 5 | 120 |
print()
result = fact(5)
for j in range(5):
    print(next(result), end=' | ')  # 1 | 1 | 2 | 2 | 3 |
print()
print(list(fact(5)))  # [1, 1, 2, 2, 3, 6, 4, 24, 5, 120]

f = fact(2)
print(f.__next__())  # 1
print(next(f))  # 1
# print(next(f)) # StopIteration


def get_data():
    yield from range(5)  # аналогично: for i in range(5): yield i
    yield from fact(4)  # позволяет вкладывать один генератор в другой, таким образом создавая вложенные генераторы
    yield from 'ABC'


print(list(get_data()))  # [0, 1, 2, 3, 4, 1, 2, 6, 24, 'A', 'B', 'C']
'''

'''
# МОДУЛЬ ITERTOOLS (порождает итераторы)
import itertools

# Итератор, циклично генерирующий бесконечную последовательность элементов:
cycle_iter = itertools.cycle(['a', 'b', 'c'])
for i in range(10):
    print(next(cycle_iter))
numbers = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]

# Функция dropwhile возвращает итератор, который генерирует элементы из входного итерируемого
# объекта сразу же после того, как для заданного условия будет получено ложное значение:
new_numbers = list(itertools.dropwhile(lambda num: num <= 5, numbers))
print(new_numbers)  # [6, 7, 8, 9, 10, 1, 2, 3]

# Функция takewhile возвращает итератор, который генерирует элементы из входного итерируемого
# объекта до тех пор, пока для заданного условия не будет получено ложное значение:
new_numbers = list(itertools.takewhile(lambda num: num <= 5, numbers))
print(new_numbers)

# Функция filterfalse противоположна встроенной функции filter:
new_numbers = itertools.filterfalse(lambda num: num <= 5, numbers)
print(*new_numbers)  # 6 7 8 9 10

# Функция compress фильтрует итерируемый объект с использованием другого итерируемого объекта для выборки значений:
data = 'ABCDEF'
selectors = [True, False, True, False, True, False]  # значения, какие следует брать, а какие игнорировать
result = itertools.compress(data, selectors)  # останавливается, когда исчерпан любой из итерируемых объектов
print(list(result))  # ['A', 'C', 'E']

# Итератор, последовательно генерирующий элементы всех переданных итерируемых объектов:
chain_iter = itertools.chain('ABC', 'DEF')
print(*chain_iter)  # A B C D E F
chain_iter = itertools.chain.from_iterable(['ABC', 'DEF'])  # для вложенных итерируемых объектов
print(*chain_iter)  # A B C D E F

# функция zip_longest
zip_iter = itertools.zip_longest([1, 2, 3], ['a', 'b', 'c', 'd', 'e'], fillvalue='*')
print(*zip_iter)  # (1, 'a') (2, 'b') (3, 'c') ('*', 'd') ('*', 'e')

# Итератор, возвращающий последовательные перекрывающиеся пары в виде кортежей:
print(*itertools.pairwise('ABCDE'))  # ('A', 'B') ('B', 'C') ('C', 'D') ('D', 'E')

# перебор комбинаций
print(itertools.permutations('123'))  # <itertools.permutations object at 0x000001E9AD4FA110>
print(list(itertools.permutations('123')))  # [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ...]; n!
print(list(itertools.permutations('123', r=2)))  # [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ...]; n!/(n-r)!
print(list(itertools.combinations('123', r=2)))  # [('1', '2'), ('1', '3'), ('2', '3')]; n!/(r!(n-r)!)
print(*(itertools.combinations_with_replacement('123', r=2)))  # ('1', '1') ('1', '2') ...; (r+n-1)!/(r!(n-1)!)
sp = list(map(lambda x: ''.join(x), itertools.permutations('123')))
print(sp)  # ['123', '132', '213', '231', '312', '321']

# декартово произведение множеств
prod_iter = list(''.join(str(e) for e in i) for i in itertools.product(['a', 'b', 'c'], range(5), repeat=1))
print(prod_iter)  # ['a0', 'a1', 'a2', 'a3', 'a4', 'b0', 'b1', 'b2', 'b3', 'b4', 'c0', 'c1', 'c2', 'c3', 'c4']
'''

'''
# ПЕРЕМЕННЫЕ
# Переменные бывают изменяемые (mutable) и неизменяемые (immutable).
# В Python сами переменные не хранят значения, а в них сохраняется лишь ссылка на объект.
a, b, c = '123'  # множественное присвоение (более предпочтительный вариант, чем массовое присвоение)
print(a, b, c)  # 1 2 3
q = w = [1, 2, 3]  # массовое (каскадное) присвоение (для изменяемых объектов так не делать)
q[1] = 'h'  # при массовом присвоении изменение списка "q" повлечёт за собой изменение списка "w"
print(q, id(q))  # [1, 'h', 3] 2814321676736 (значения id меняются при каждом запуске программы)
print(w, id(w))  # [1, 'h', 3] 2814321676736 (значения id меняются при каждом запуске программы)
# Оператор is проверяет идентичность объектов в памяти (значения id()), а "==" проверяет поэлементно равенство значений.
# Согласно PEP 8 сравнение объектов с None должно выполняться оператором is, а не "==".
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("list1 == list2: " + str(list1 == list2))  # list1 == list2: True
print("list1 is list2: " + str(list1 is list2))  # list1 is list2: False
print("list1 == list3: " + str(list1 == list3))  # list1 == list3: True
print("list1 is list3: " + str(list1 is list3))  # list1 is list3: True
list3[1] = 'n'  # при изменении list1 меняется и list3, и наоборот, т. к. они ссылаются на один и тот же объект в памяти
print(list1)  # [1, 'n', 3]
print(list3)  # [1, 'n', 3]

# поверхностное и глубокое копирование
import copy
x = [1, [2]]
# Поверхностная копия создаёт объект и затем вставляет в него ссылки на объекты, находящиеся в оригинале.
y = copy.copy(x)
z = copy.deepcopy(x)  # глубокая копия создаёт объект и рекурсивно копирует все внутренние объекты
# Разница между поверхностным и глубоким копированием существенна только для составных объектов,
# содержащих изменяемые объекты (например, вложенные списки, или словарь, значения которого списки или словари).
y.append(3)  # исходный список не изменится
y[1].append(4)  # в исходном списке изменится внутренний список
print(x)  # [1, [2, 4]]
print(y)  # [1, [2, 4], 3]
print(z)  # [1, [2]]

# особенности работы операторов + и +=
nums1 = [1, 2, 3]
nums2 = nums1
nums1 = nums1 + [4, 5]  # в данном случае оператор + создал новый список
print(nums1)  # [1, 2, 3, 4, 5]
print(nums2)  # [1, 2, 3]
nums1 = [1, 2, 3]
nums2 = nums1
nums1 += [4, 5]  # в данном случае оператор += изменил текущий список
print(nums1)  # [1, 2, 3, 4, 5]
print(nums2)  # [1, 2, 3, 4, 5]

# Интернирование - это процесс хранения в памяти только одной копии объекта.
num1 = 10 ** 10
num2 = 10 ** 10
print(num1 is num2, num1 == num2)  # True True
num1 = 10 ** 100
num2 = 10 ** 100
print(num1 is num2, num1 == num2)  # False True (для больших значений интернирования не происходит)
s1 = 'beegeek!' * 100
s2 = 'beegeek!' * 100
s3 = ('bee' + 'geek!') * 100
print(id(s1))  # 2170009721648
print(id(s2))  # 2170009721648
print(id(s3))  # 2170009721648

a, b = 4, 5
a, b = b, a  # перестановка переменных "a" и "b"
print(a, b)  # 5 4
b = b + 2  # Сначала вычисляется то, что стоит справа от знака равно, затем новое значение
print(b)  # присваивается переменной (старое значение заменяется на новое).

nums = [1, 2, 3]
nums.append(nums)
print(nums)  # [1, 2, 3, [...]] (отображении объектов, содержащих циклические ссылки)

x = 6
print(x)
del x  # можно удалить переменную
# print(x) # NameError: name 'x' is not defined

# моржовой оператор
print(see_walrus := 'Look at my walrus, my walrus is amazing')
print('w' in (s := 'sdfsw'))  # переменную и значение необходимо поместить в скобки (из-за низкого приоритета оператора)
'''

'''
# БИТОВЫЕ ОПЕРАЦИИ
print(7 << 1)  # 14 (сдвиг каждого бита вправо; аналогично умножению на 2; работает быстрее, чем умножение)
print(7 >> 1)  # 3 (сдвиг каждого бита влево; аналогично целочисленному делению на 2; работает быстрее, чем деление)

# Для выполнения битовых операций, числа переводятся в двоичную систему,
# а затем производятся операции с каждой парой битов:
print(bin(3))       # 0b11   (1) перевод первого числа в двоичную систему
print(bin(58))  # 0b111010   (2) перевод второго числа в двоичную систему
print((int(0b000010)))  # 2  (3) результат выполнение побитовой операции сложения
print(3 & 58)  # 2           (4) проверка
print(37 & 58)  # 32 (И)
print(37 | 58)  # 63 (ИЛИ)
print(37 ^ 58)  # 31 (исключающее ИЛИ, XOR)
print(~37)  # -38 (инверсия, НЕ)
'''

'''
# БУЛЕВЫ ЗНАЧЕНИЯ (BOOL), ЛОГИЧЕСКИЕ ОПЕРАТОРЫ NOT, AND, OR
# Приоритет логических операторов: not, and, or.
# Для and: если логическое выражение вернуло ложь, то последующие не проверяются, результат выражения будет False.
# Для or: если логическое выражение вернуло истину, то последующие не проверяются, результат выражения будет True.
print(bool(0))  # False
print(bool('0'))  # нулевое значение или None - "False", ненулевое - "True"
print(bool(''))  # пустая строка (список и т. д.) - "False", непустая - "True"
# Согласно PEP 8 предпочтительнее использовать isinstance чем type(...) == ...,
# однако необходимо помнить, что isinstance принимает True и False за int.
print(isinstance([1, 2, 3], list))  # True
print(isinstance(True, int))  # True (True & False относятся к int)
print(isinstance(True, float))  # False
print(isinstance(10.5, (int, float)))  # True (можно передать кортеж из типов)
print(int(True), int(False))  # 1 0
print(float(True), float(False))  # 1.0 0.0

print(not [])  # not возвращает булево значение
print(1 and [] and 3)  # возвращает 1-ый ложный операнд, либо последний, если все истинные
print([] or 1 or 2)  # возвращает 1-ый истинный операнд, либо последний, если все ложные

print(1 + True)  # 2 (True принимается за 1)
print(1 + False)  # 1 (False принимается за 0)

# исключение нулевых значений
# 1-ый способ:
result_1 = 1
for i in [1, 3, 5, 0]:
    result_1 *= i or 1
print('result_1 =', result_1)  # result_1 = 15

# 2-ой способ:
result_2 = 1
for i in [1, 3, 5, 0]:
    result_2 *= i + (i == 0)
print('result_2 =', result_2)  # result_2 = 15
'''

'''
# ОПЕРАТОР ASSERT (нужен для того, чтобы указать, что нечто является истиной)
mylist = ['item']
assert len(mylist) >= 1
mylist.pop()
print(mylist)
assert len(mylist) >= 1, 'list length equals 0'  # AssertionError: list length equals 0
'''

'''
# ОБРАБОТКА ИСКЛЮЧЕНИЙ (TRY-EXCEPT-ELSE-FINALLY)
# Блок else в конструкции try-except подобен блоку else в конструкциях for/while,
# он срабатывает если в контролируемом коде не произошло ошибок,
# если тело цикла завершилось штатным способом, без break.
# Блок finally выполняется в любом случае, независимо от того,
# возникла ошибка (исключение) при выполнении кода try блока или нет.
"""
try:
    # контролируемый код
except тип_ошибки_1:
    # код обработки ошибки (исключения)
except тип_ошибки_2:
    # код обработки ошибки (исключения)
...
except тип_ошибки_n:
    # код обработки ошибки (исключения)
else:
    # код для случая, если ошибки не было
finally:
    # код, который выполняется всегда"""

try:
    nums = [10, 5, 20, 25]
    print(nums[100])
except (KeyError, IndexError) as error:
    print(error)  # list index out of range
    print(type(error))  # <class 'IndexError'>
    print(type(error).__name__)  # IndexError

# Инструкции внутри блока finally будут выполнены, даже если блок try содержит break, continue, return.
def try_func():
    print('start')
    try:
        print('Выполняется блок try!')
        x = 'try'
        # print(x / 0)
        return x
    except:
        print('Выполняется блок except!')
        x = 'except'
        return x
    else:  # в отличие от finally блок else не выполняется всегда (т. к. в try есть return)
        print('Выполняется блок else!')
        x = 'else'
        return x
    finally:
        print('Выполняется блок finally!')
        x = 'finally'
        # return x


print(try_func())


def beegeek():
    numbers = [1, 2, 3, 4]
    try:
        numbers.append(numbers[4])
        return numbers
    except IndexError:
        numbers.append(numbers[3])
        return numbers
    finally:
        numbers.append(numbers[2])


print(beegeek())  # [1, 2, 3, 4, 4, 3]

# возбуждение исключений с помощью оператора raise (прекращает работу функции как и return)
try:
    raise IndexError('ошибочка')
except Exception as err:
    print(err)  # ошибочка
    print(type(err))  # <class 'IndexError'>
    print(type(err).__name__)  # IndexError


# создание пользовательских исключений
class NegativeAgeError(Exception):  # необходимо наследовать от Exception, а не от BaseException
    pass


age = -10
try:
    if age < 0:
        raise NegativeAgeError('Возраст не может быть отрицательным')
    print('Ваш возраст равен', age)
except TypeError:
    print('Возраст должен быть числом')
except NegativeAgeError as e:
    print(e)  # Возраст не может быть отрицательным
    print(type(e))  # <class '__main__.NegativeAgeError'>
    print(type(e).__name__)  # NegativeAgeError


class PrimaryKeyError(Exception):
    """Создание пользовательских исключений с аргументами."""
    def __init__(self, **kwargs):
        if not kwargs:
            self.message = f'Первичный ключ должен быть целым неотрицательным числом'
        elif kwargs.get('id') is not None:
            self.message = f"Значение первичного ключа id = {kwargs.get('id')} недопустимо"
        elif kwargs.get('pk') is not None:
            self.message = f"Значение первичного ключа pk = {kwargs.get('pk')} недопустимо"

    def __str__(self):
        return self.message


try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as error:
    print(error)  # Значение первичного ключа id = -10.5 недопустимо
    print(error.__class__)  # <class '__main__.PrimaryKeyError'>
    print(type(error).__name__)  # PrimaryKeyError
'''

'''
# УСЛОВНЫЙ ОПЕРАТОР IF
# Из всех указанных блоков выполнится только один, тот чье условие выполниться первым, как только
# тело if или какого-нибудь elif выполняется, все нижеследующие elif, а также else пропускаются.
if 1 == 1:
    print(1)
elif 1 == 1:
    print(2)
else:
    print(3)

# Тернарный оператор - условное выражение, записанное в одну строку.
number = -7
number = number if number >= 0 else -number
print(number)  # 7
'''

'''
# КОНСТРУКЦИЯ MATCH/CASE
json_data = {'id': 2, 'access': True, 'info': ['01.01.2023', {'login': '123', 'email': 'email@m.ru'}, True, 1000]}
match json_data:  # в данном случае [] - это группирующие скобки, а не указатель списка, либо можно использовать ()
    case {'access': bool(access), 'info': list([str(), {'email': str() as email}, _, _, *_]) as info}:
        print(f"JSON: access: {access}, email: {email}, {info}")  # Для списков/кортежей проверяется наличие всех
    case _:              # элементов, а также их порядок, для словарей/множеств только вхождение конкретного элемента.
        print("неверный запрос")

primary_keys = {1, 2, 3}
match primary_keys:
    case set() as keys if len(keys) == 3:
        print(f"Primary Keys: {keys}")
    case _:
        print("неверный запрос")
'''

'''
# ЦИКЛЫ FOR & WHILE
# Цикл for за кулисами вызывает один раз магический метод __iter__() у итерируемого объекта для получения итератора, 
# а затем метод __next__() до тех пор, пока не будет возбуждено исключение StopIteration.
# Изменение любой коллекции (списка, словаря, множества) во время итерации по ней - плохая идея, так как словари
# и множества во время изменения могут быть перестроены, что скорее всего приведёт к изменению порядка элементов в них.
# Цикл for: для повторения кода определённое (известное) количество раз.
# Цикл while: для повторения кода неизвестное количество раз.
# Внутри цикла значение переменной можно изменять на любое, 
# но это изменение не повлияет на следующее значение переменной (в отличие от VBA).
for i in range(4):
    print(i)
    i = "hello"
    print(i)

number = 10
running = True
while running:
    guess = int(input('Введите целое число: '))
    if guess == number:
        print('Вы угадали!!!')
        running = False  # прерывает цикл (либо можно написать "break", тогда else не выполнятся)
    elif guess > number:
        print('Заданное число меньше указанного')
    else:
        print('Заданное число больше указанного')
else:
    print('конец')
'''
'''
while True:  # можно написать "while 1:"
    s = input('Введите что-нибудь: ')
    if s == 'exit':
        break
    if len(s) < 3:
        print('not  enough')
        continue  # continue пропускает остальные действия в блоке ('Введённая строка слишком длинная' не выведется)
    print('Введённая строка слишком длинная')
'''
'''
for i in range(-10, 5, 1):  # range может содержать 1 переменную (это будет конечное значение)
    print(i)
    if i >= 0:
        print('right now')
        break
    else:
        print('not now')
else:  # из-за того, что есть "break" else не выполняется
    print('9999')

s = 1, 2, 3, 4, 5, 'gg', (1, 3), [1, 2]
for i in s:
    print(i, type(i), type(s))

mas = ['stroka1', 'null', 'stroka3', 'stop', 'null']
for s in mas:
    if s == 'null':
        continue  # continue пропускает текущую итерацию, break прерывает текущий цикл (for/while)
    print(s)

# Аналогично предыдущей записи, не используя continue:
for s in mas:
    if s != 'null':
        print(s)

models = ['decision tree', 'linear model', 'svm', 'ensemble']
for i in range(len(models)):
    models[i] += ' - алгоритм машинного обучения'
    print(models[i])
print(models)  # список изменился

# Перебор элементов каждого с каждым без повторений:
a = 1, 2, 3, 4, 5
for i in range(len(a) - 1):
    print('i =', i)
    for j in range(i + 1, len(a)):
        print('j =', j)


def chunked(s: str, n: int) -> list:
    """Функция разбивает строку s на списки длиной n символов."""
    result = []
    s = s.split()
    for i in range(0, len(s), n):
        print(i)
        result.append(s[i : i+n])  # отступы в срезе согласно PEP 8
    return result


print(chunked('a b c d e f r g b', 5))  # [['a', 'b', 'c', 'd', 'e'], ['f', 'r', 'g', 'b']]


# алгоритм Евклида
def evklid(a: int, b: int) -> int:
    """Функция находит НОД (наибольший общий делитель).
    a * b = НОД * НОК"""
    while b > 0:
        a, b = b, a % b
    return a


print(evklid(75, 120))


def euler_76(num=100):
    """Функция считает сколькими различными способами можно записать число в
    виде суммы натуральных чисел (пример динамического программирования)."""
    integers = list(range(1, num + 1))
    ways = [1] + [0] * num
    for option in integers:
        for i in range(len(ways) - option):
            ways[i + option] += ways[i]
    return ways


print(euler_76(100))
'''

'''
# ВСТРОЕННЫЕ ФУНКЦИИ ALL & ANY
# Функция all проверяет каждый элемент последовательности на истинность.
print(all(i.isdigit() for i in '12354635'))  # True (функции all и any работают с итераторами)
print(all([1, 2, 3]))  # True
print(all([1, 2, 3, 0, 5]))  # False
print(all([False, 4, 1]))  # False
print(all(('', 'red', 'green')))  # False
print(all({0: 'Zero', 1: 'One', 2: 'Two'}))  # False (проверяет ключи, но не значения)
print(all({'Zero': 0, 'One': 1, 'Two': 2}))  # True
# Функция any возвращает True если хотя бы один элемент последовательности является истинным.
print(any([0, 1, 0]))  # True
print(any([False, 0, 1]))  # True
print(any(['', [], 'green']))  # True
print(any([]))  # False
print(all([]))  # True
'''

'''
# ВСТРОЕННЫЕ ФУНКЦИИ ZIP & ENUMERATE (являются итераторами)
# Количество кортежей, получаемых в ходе функции zip определяется
# по минимальной длине среди всех коллекций, участвующих в функции.
first = 'a b c d e f g'.split(' ')  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
second = '1 2 3 4 5 6 7'.split(' ')  # ['1', '2', '3', '4', '5', '6', '7']
# При strict=True вызывает ошибку ValueError, если длины объектов не совпадают:
x_zip = zip(first, second, first, strict=True)
print(x_zip, type(x_zip))  # <zip object at 0x000001E40C5D47C0> <class 'zip'>
print(list(x_zip))  # [('a', '1', 'a'), ('b', '2', 'b'), ('c', '3', 'c'), ('d', '4', 'd'), ('e', '5', 'e'), ...]

matrix = [[7, 2, 9], [4, 5, 6], [1, 8, 3]]
print(list(zip(*matrix)))  # [(7, 4, 1), (2, 5, 8), (9, 6, 3)] (транспонирование матрицы)

colors = ['red', 'green', 'blue']
pairs = enumerate(colors, 5)
print(pairs, type(pairs))  # <enumerate object at 0x000001AB393D4780> <class 'enumerate'>
print(list(pairs))  # [(5, 'red'), (6, 'green'), (7, 'blue')]
for pair in enumerate(colors, 10):
    print(pair)  # (10, 'red') и т. д.

models = ['decision tree', 'linear model', 'svm', 'ensemble']
# Функция zip возвращает пару элементов, которые можно записать в 2 разные переменные в цикле for.
# Записываем первый элемент пары в num, второй - в model:
for num, model in zip(range(len(models)), models):
    print(num + 1, 'model is:', model)  # 1 model is: decision tree и т. д.

for num, model in enumerate(models):  # аналогично предыдущей записи
    print(num + 1, 'model is:', model)

# ZIP & UNZIP
a = [1, 2, 3]
b = [4, 5, 6]
f = list(zip(a, b))
print(f, type(f))  # [(1, 4), (2, 5), (3, 6)] <class 'list'>
c, d = zip(*f)
print(c, type(c))  # (1, 2, 3) <class 'tuple'>
print(list(d))  # [4, 5, 6]
'''

'''
# РАСПАКОВКА (ДЕСТРУКТУРИЗАЦИЯ, UNPACKING) И УПАКОВКА (ОПЕРАТОР *)
a, *b, c = (1, 2, 3, 4, 5)
print(a, type(a), c)  # 1 <class 'int'> 5
print(*b, b, type(b))  # 2 3 4 [2, 3, 4] <class 'list'>
a, *b, c = 1, 2
print(a, b, c)  # 1 [] 2
num_1, num_2, num_3 = 10, 20, 30
*numbers, = num_1, num_2, num_3
print(numbers)  # [10, 20, 30]

first, _, third, *_, last = [1, 2, 3, 4, 5, 6, 7, 8]  # для получения определённых элементов коллекции
print(first)  # 1
print(third)  # 3
print(_)  # [4, 5, 6, 7]
print(last)  # 8

dictionary_1 = {"red": "красный", "blue": "синий"}
dictionary_2 = {"green": "зеленый", "yellow": "желтый"}
dictionary_3 = {**dictionary_1, **dictionary_2}  # упаковка словарей (либо dictionary_3 = dictionary_1 | dictionary_2)
print(dictionary_3)  # {'red': 'красный', 'blue': 'синий', 'green': 'зеленый', 'yellow': 'желтый'}

s = 'Python'
print(*s, sep='^', end='*')  # P^y^t^h^o^n*
print()
print(*sorted([]) or [5, 7, 4], (0, 1))  # 5 7 4 (0, 1) (* применяется ко всему выражению одного аргумента)
print(*[1, 2, 3] + [5, 6, 7], [8, 9])  # 1 2 3 5 6 7 [8, 9]
'''

'''
# ФУНКЦИИ (FUNCTION)
# Параметр - это значение, которое принимает функция (переменная внутри определения функции).
# Аргумент - это значение, которое передается в функцию при ее вызове в программе,
# фактическое значение, переданное функции.
pechat = print  # функции можно переназначать (как встроенные, так и самописные)
pechat('hello')

# ВСТРОЕННЫЕ ФУНКЦИИ (BUILT-IN FUNCTION, BUILTINS)
# Значения аргументов по умолчанию встроенной функции print:
# sep = ' ' - пробел
# end = '\n' - перевод на новую строку
print('1', '2', '3', sep='\n')
print('1', '2', '3', end='t')
print('g')
print(type(print))  # <class 'builtin_function_or_method'>
print('td' + 'r', 'e')  # tdr e (с "+" не ставится пробел, с "," ставится)

print(hash(100.89))  # 2052200278200189028 (хеш-значение переданного объекта)
# print(hash((1, 4, 'fg', [1, 2, 3]))) # TypeError: unhashable type: 'list'
list_data = eval("['Python', 'C#']")  # будет ошибка при использовании while, for, if, def, import, class, raise и т. д.
print(list_data, type(list_data), len(list_data))  # ['Python', 'C#'] <class 'list'> 2
code = """for i in range(10):
    if i % 2 == 0:
        print(i)"""
exec(code)

numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]
print(max(numbers, key=abs))  # -210 (также можно использовать: key=len, key=numbers.index)
print(min(numbers, key=abs))  # -7
print(sorted(numbers, key=abs, reverse=True))  # [-210, 117, -100, 87, -50, 32, 10, 8, -7]
print((sum([1, 2], 10)))  # 13 (второй аргумент - это значение по умолчанию)

points = [(1, -1), (29, 9), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
points.sort()  # либо print(sorted(points))
# Сортировка пройдет по первым значениям пар кортежа, а в случае их равенства, по вторым:
print(points)  # [(-10, 15), (1, -1), (1, 5), (2, -4), (2, 3), (7, 18), (10, 9)]


def compare_by_second(point):
    return point[1], point[0]  # кортеж условий сравнения
# Сначала сортировка идёт по point[1] (2-му элементу), если они равны, то по point[0] (1-му элементу).
# Можно задать кортеж с любым количеством условий сравнения.


def compare_by_sum(point): return point[0] + point[1]  # способ записи функции в одну строку


# Функция, используемая в аргументе key должна обязательно иметь какой-либо параметр (при определении функции).
print(sorted(points, key=compare_by_second))   # сортируем по второму значению кортежа
print(sorted(points, key=lambda point: (point[1], point[0])))  # аналогично предыдущему
print(sorted(points, key=compare_by_sum))      # сортируем по сумме кортежа


def sort_priority(numbers, group):
    """Приоритетная сортировка, если в сортируемом списке numbers содержится число из group."""
    numbers.sort(key=lambda x: (x not in group, x))


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)
print(numbers)  # [2, 3, 5, 7, 1, 4, 6, 8]
print(sorted([(True, 4), (False, 4)]))  # функция sort_priority работает аналогично этому примеру (False = 0, True = 1)
print(sorted(numbers, key=lambda x: (x % 2 == 1, x)))  # сначала выводятся чётные числа по возрастанию, затем нечётные


# В функции сначала указываются обязательные параметры (message),
# а потом параметры по умолчанию (times=1), иначе будет ошибка.
def say(message, times=1):  # значение times по умолчанию 1, но его можно поменять
    print(message * times)


# say(message=1, times) # ошибка т. к. именованный аргумент стоит до позиционного
# say(times, message=1) # сначала должны идти позиционные аргументы (times), затем именованные (message=1)
say('44', 2)  # 4444
say('33')  # 33
say(message='33')  # значение аналогично предыдущему
say(message='44', times=3)  # использование именованных аргументов
say(times=3, message='44')  # аналогично предыдущему
print(say('44', 2))  # None (если return не указан, то по умолчанию возвращается значение None)


# ОПЕРАТОР RETURN
def maximum(x, y):
    if x > y:
        return x  # return используется для прекращения работы функции и выхода из неё (аналогично break в циклах)
    elif x == y:
        return 'числа равны', f'{x = }, {y=}'  # можно возвратить несколько значений (кортеж)
    else:
        return y


print(maximum(1, 1))  # ('числа равны', 'x = 1, y=1')


def print_person(name, age):
    if age > 120 or age < 1:
        print("Invalid age")
        return  # используется для выхода из функции (возвращает значение None)
    print(f"Name: {name}  Age: {age}")


print_person("Tom", 22)  # Name: Tom  Age: 22
print_person("Bob", -102)  # Invalid age


# Не рекомендуется использовать изменяемые объекты в качестве значений по умолчанию (списки, словари, множества),
# так как изменение списка повлияет на каждый следующий вызов функции:
def append_func(element, seq=[]):
    seq.append(element)
    return seq


print(append_func(10))  # [10]
print(append_func(5))  # [10, 5]


# Для решения вышеописанной проблемы можно использовать константу None:
def append_func(element, seq=None):
    if seq is None:
        seq = []
    seq.append(element)
    return seq


print(append_func(10))  # [10]
print(append_func(5))  # [5]


def matrix(n=1, m=0, value=0):
    """Функция создаёт матрицу."""
    if not m:
        m = n
    print(locals())  # список имен, находящихся в локальном пространстве
    return [[value] * m for _ in range(n)]


print(matrix())  # [[0]]
print(matrix(3))  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]] (n = m если указано только n)
print(matrix(2, 3, 5))  # [[5, 5, 5], [5, 5, 5]]


# вызов функции через словарь
def start():
    print("Let's start")


def stop():
    print("Let's stop")


def pause():
    print("Let's pause")


commands = {'start': start, 'stop': stop, 'pause': pause}  # словарь соответствия команда-функция
# Сначала необходимо задать функции, чтобы сохранить их в словарь, либо в переменную.
for command in commands:  # в словаре в качестве значений пишется функция без скобок
    commands[command]()  # вызываем нужную функцию через словарь по ключу со скобками в конце


# *args позволяет передавать функции произвольное число неименованных аргументов (кортеж)
# **kwargs позволяет передавать функции произвольное число именованных аргументов (словарь)
def func(*args):
    return '|'.join(args)


args = ['a', 'b', 'c', 'd', 'e']
print(*args)  # a b c d e
print(func(*args))  # a|b|c|d|e (в функцию можно передавать распакованный аргумент)


def total(aaa=1, bbb=2, ccc=3, initial=5, *numbers, **keywords):  # если есть * или **, то параметр необязательный
    count = initial  # * - кортеж, ** - словарь
    for number in numbers:
        count += number
        print(count, number, numbers)
    for key in keywords:
        count += keywords[key]
        print(count, key, keywords[key], keywords)
    print(locals())  # список имен, находящихся в локальном пространстве
    return count, {'aaa': aaa, 'bbb': bbb, 'ccc': ccc, **keywords}  # распаковка словаря


print(total(1, 2, 3, 5, 1, 2, 4, a=4, b=6))  # (22, {'aaa': 1, 'bbb': 2, 'ccc': 3, 'a': 4, 'b': 6})


# подсчёт количества вызовов функции, используя пользовательские атрибуты функций
def remove_marks(text, marks):
    remove_marks.count += 1
    return ''.join(c for c in text if c not in marks)


remove_marks.count = 0
marks = '.,!?'
text = 'Are you listening? Meet my family! There are my parents, my brother and me.'
for mark in marks:
    print(remove_marks(text, mark))
print(remove_marks.__dict__)  # {'count': 4}
print(remove_marks.count)  # 4

# АНОНИМНЫЕ ФУНКЦИИ - обычные функции, но записанные в одну строку.
# Обозначается lambda, её необязательно присваивать переменной (как с def).
func = lambda a, b: a ** b  # возведение "а" в степень "b"
print(func(2, 3))  # 8
func = lambda *args: args[0] * args[1]
print(func(2, 3, 4))  # 6
print((lambda x, y: x + y)(5, 10))  # 15

# ФУНКЦИИ ВЫСШЕГО ПОРЯДКА – функции, которые принимают или/и возвращают другие функции (map, filter, min, max, sorted).
# ФУНКЦИЯ ВЫСШЕГО ПОРЯДКА MAP (является итератором)
# Применяет указанную функцию к каждому элементу указанной последовательности/последовательностей.
# Функция, используемая в map или filter должна обязательно принимать аргумент.
x = [1.0, -2.0, 3.0]
l1_norm = lambda x: sum(map(abs, x))
print(l1_norm(x))  # 6.0


def l1_norm(x):  # аналогично предыдущей функции с использованием lambda
    return sum(map(abs, x))


print(l1_norm(x))  # 6.0

numbers = ['-1', '20', '3', '-94', '65', '6', '-970', '8']
new_numbers = list(map(abs, map(int, numbers)))  # можно строить бесконечные цепочки преобразований
print(new_numbers)  # [1, 20, 3, 94, 65, 6, 970, 8]


def a_na_b(a, b):
    return a * b


list1 = [1, 2, 3, 4]
list2 = [4, 3, 2, 1]
# Функция, которую следует применить к элементам последовательности или последовательностей,
# должна принимать количество элементов равное количеству последовательностей.
print(list(map(a_na_b, list1, list2)))  # [4, 6, 6, 4]
print(list(map(lambda a, b: a * b, list1, list2)))  # [4, 6, 6, 4] (аналогично предыдущему)

# ФУНКЦИЯ ВЫСШЕГО ПОРЯДКА FILTER (является итератором)
# В отличие от map фильтрующая функция не изменяет элементы последовательности,
# а исключает элементы, не удовлетворяющие условиям функции.
def is_greater10(num):
    return num > 10


numbers = [12, 2, -30, 48, 51, -60, 19, 10, 13]
large_numbers = list(filter(is_greater10, numbers))
print(large_numbers)  # [12, 48, 51, 19, 13]
large_numbers = list(filter(lambda x: x > 50, numbers))
print(large_numbers)  # [51]


def search_for_rus_phones(number):
    if number[:2] == '+7' or number[:2] == '+8' or number[0] == '8':
        return number


data = ['+7123456789', '+1123456789', '8123456789']
filter_res = filter(search_for_rus_phones, data)
print(list(filter_res))  # ['+7123456789', '8123456789']

values = [1, 0, 10, '', None, [], [1, 2, 3], ()]
true_values = filter(None, values)
print(list(true_values))  # [1, 10, [1, 2, 3]]
numbers = list(filter(int, ['1', '2', '3', '4', '5', 6, 7, 2.5]))
print(numbers)  # ['1', '2', '3', '4', '5', 6, 7, 2.5]

pets = ['alfred', 'tabitha', 'william', 'arla']
chars = ['x', 'y', '2', '3', 'a']
uppered_pets = list(map(str.upper, pets))
capitalized_pets = list(map(str.capitalize, pets))
only_letters = list(filter(str.isalpha, chars))
print(uppered_pets)  # ['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']
print(capitalized_pets)  # ['Alfred', 'Tabitha', 'William', 'Arla']
print(only_letters)  # ['x', 'y', 'a']


# ВЛОЖЕННЫЕ ФУНКЦИИ
# 1-ый способ:
def generator_square_polynom(a, b, c):
    def square_polynom(x):
        print(f'inner_function: {locals()}')
        return a * x ** 2 + b * x + c
    print(f'outer_function: {locals()}')
    return square_polynom


# 2-ой способ:
def generator_square_polynom_2(a, b, c):
    return lambda x: a * x**2 + b * x + c


# 3-ий способ:
generator_square_polynom_3 = lambda a, b, c: lambda x: a * x**2 + b * x + c

print(generator_square_polynom(a=-3, b=-10, c=50)(x=-1))  # 57
equation = generator_square_polynom(1, 2, 4)
print(equation(2), equation(7))  # 12 67


def add_3(x):
    return x + 3


def mul_7(x):
    return x * 7


def compose(f, g):
    return lambda x: f(g(x))


print(mul_7(mul_7(mul_7(mul_7(2)))))  # 4802
print(compose(mul_7, add_3)(1))  # 28
print(compose(add_3, mul_7)(2))  # 17
print(compose(mul_7, str)(3))   # 3333333
print(compose(str, mul_7)(5))   # 35

# КЛЮЧЕВЫЕ СЛОВА GLOBAL & NONLOCAL
x = 60


def aa():
    x = 2
    print(x)

    def bb():
        # global x
        # nonlocal x
        x = 5
        print(x)
        print(f'bb_function: {locals()}')

    bb()
    print(x)
    print(f'aa_function: {locals()}')


aa()
print(x)


# ЗАМЫКАНИЕ (CLOSURE) - функция, которая находится внутри другой функции
# и ссылается на переменные, объявленные в теле внешней функции.
def average_numbers():
    numbers = []
    count = 0

    def inner(number):
        nonlocal count  # Вложенная функция inner не просто обращается (получает значение)
        count += 1      # к переменной count, но и пытается его изменить! Внутренняя функция
        numbers.append(number)  # inner видит переменные во внешней функции average_numbers,
        print(f'{numbers = }')  # но, если она хочет такую переменную изменить, должна объявить ее nonlocal.
        return sum(numbers) / len(numbers), count
    return inner


r1 = average_numbers()  # списки для переменных r1 и r2 получаются разные
print(r1(1))
print(r1(2))
print(r1(3))
print(r1(4))
r2 = average_numbers()
print(r2(10))
print(r2(100))
print(r2(1000))
print(r1(10000))


# ДЕКОРАТОРЫ - это, по сути, "обёртки", которые дают нам возможность изменить поведение функции, не изменяя её код.
# Аргументы в функции могут меняться и при изменении в такой конструкции будут возникать ошибки,
# поэтому лучше принять себе за правило: при описании декоратора, все принимаемые параметры,
# (вне зависимости от их наличия), лучше добавлять через *args и **kwargs (в функциях inner и func).
# Параметры в функциях inner и func должны быть одинаковыми, иначе будет ошибка.
from functools import wraps
def header(func):
    @wraps(func)  # для сохранения исходных имени функции и строки документации
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')
    return inner


def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
    inner.__name__ = func.__name__  # Чтобы после декорирования не пропадали
    inner.__doc__ = func.__doc__    # имя функции и строка документации внутренней функции.
    return inner


# Синтаксический сахар (англ. syntactic sugar) в языке программирования - это синтаксические возможности,
# применение которых не влияет на поведение программы, но делает использование языка более удобным для человека.
@header
@table  # является синтаксическим сахаром для записи say = header(table(say))
def say(name, surname, age):
    """Способы сохранения строки документации функции say:
    1) inner.__doc__ = func.__doc__
    2) from functools import wraps, @wraps(func) (сохраняет ещё и имя функции)
    """
    print('hello', name, surname, age)


say('Ivan', 'Ivanov', 30)
print(say.__name__)
print(say.__doc__)


# Чтобы декоратор не поглощал возвращаемое значение из функции greet() нужно, чтобы
# вложенная функция wrapper() явно возвращала какое-либо значения (return f'{dash}\n{result}\n{dash}'):
def talk(func):
    def wrapper(*args, **kwargs):
        dash = '-' * 15
        result = func(*args, **kwargs)
        return f'{dash}\n{result}\n{dash}'
    return wrapper


@talk
def greet(name):
    return f'Hello {name}!'


print(greet('Timur'))


# декоратор, который подсчитывает время выполнения функции
import time
def timer(iters=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            for i in range(iters):
                value = func(*args, **kwargs)
            end = time.perf_counter()
            total = end - start
            print(f'Среднее время выполнения {func.__name__}: {round(total/iters, 4)} сек.')
            return value
        return wrapper
    return decorator


@timer(iters=1000)  # Аналогично result = timer(1000)(test)(10000) либо test = timer(1000)(test)(10000),
def test(n):  # чтобы не создавать лишнюю переменную "result".
    return sum([(i/99) ** 2 for i in range(n)])


result = test(10000)  # Среднее время выполнения test: 0.0009 сек.
print(f'Результат функции test = {result}')  # Результат функции test = 34005033.67003357


# декоратор, который вызывает функцию переданное количество раз
def repeater(repeat=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, repeat + 1):
                print(f'{i}-й запуск функции:')
                value = func(*args, **kwargs)
                print()
            return value
        return wrapper
    return decorator


@repeater(repeat=5)  # аналогично repeater(repeat=5)(beegeek)()
def beegeek():
    print('beegeek')


beegeek()
'''

"""
# СТРОКА ДОКУМЕНТАЦИИ (DOCSTRING)
def printMax(x, y):
    '''Выводит максимальное.
    Оба значения должны быть целыми числами.'''
    x = int(x)
    y = int(y)
    '''Это уже не относится к строке документации.'''
    if x > y:
        print(x, type(x), 'наибольшее')
    else:
        print(y, type(y), 'наибольшее')


print(printMax.__doc__)  # выводит то, что в тройных кавычках (курсивом, первый раз)
printMax(3, 5)  # 5 <class 'int'> наибольшее
print(printMax.__name__)  # printMax (выводит название функции)

help(sorted)
print(sorted.__doc__)
import math  # чтобы открыть сам модуль math, кликнуть на него мышкой, зажав ctrl
help(math)
"""

'''
# АННОТАЦИИ ТИПОВ
# list[int, float] - означает, что первый элемент целое число, второй вещественное число
# list[int | float] - означает, что элементы могут быть как целыми так и вещественными
def add_numbers(a: list[int | float], b: int = 3) -> dict[str, int | float]:  # для словаря: [ключ, значение]
    a.append(b)
    return {str(i): j for i, j in enumerate(a, 1)}


print(add_numbers([4.2, 3, 5], 5.6))  # второй аргумент подсвечивается, т. к. передан не тот тип данных
print(add_numbers.__annotations__)  # {'a': list[int | float], 'b': <class 'int'>, 'return': dict[str, int | float]}

# Также можно добавить аннотации типов к переменным в любом месте кода:
name: str = 'Kirill'
age: int = 10

# Можно также аннотировать переменные, не назначая им сразу значения:
surname: str



# РЕКУРСИЯ
import sys
print(sys.getrecursionlimit())  # 1000
sys.setrecursionlimit(1000)  # установка максимальной глубины рекурсии


def fact(x):
    """Вычисление факториала с помощью рекурсии."""
    if x == 0:  # факториал 0 равен 1 (0! = 1)
        return 1
    else:
        return x * fact(x - 1)


print(fact(10))  # 3628800

fact = lambda n: 1 if n == 0 else n * fact(n - 1)  # использование рекурсии в лямбда-функциях
print(*map(fact, range(1, 11)))  # 1 2 6 24 120 720 5040 40320 362880 3628800


def reverse(times):
    """Разворачивает числа задом наперёд."""
    if times > 0:
        print('Это рекурсивная функция.')
        reverse(times - 1)
        print(times)


reverse(5)


def quicksort(array):
    """Быстрая сортировка с помощью рекурсии."""
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))  # [2, 3, 5, 10]


def rec(spisok, level=1):
    """Обход всех вложенных элементов (например, файлов в папках)."""
    print(*spisok, 'level =', level)
    for i in spisok:
        if type(i) == list:
            rec(i, level + 1)


a = [1, [3, 5, 7], [[[[[[3, 4]]]]], 4, 6, 7, [4, 5]]]
rec(a)


def dict_travel(data, parent_key=''):
    for key, value in sorted(data.items()):
        key = f'{parent_key}.{key}' if parent_key else key
        if isinstance(value, dict):
            dict_travel(value, key)
        else:
            print(f'{key}: {value}')


data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
dict_travel(data)


def recursive_sum(nested_lists):
    """Подсчёт всех элементов коллекции."""
    total = 0
    for elem in nested_lists:
        if isinstance(elem, list):
            total += recursive_sum(elem)
        else:
            total += elem
    return total


print(recursive_sum(a))  # 49


# Мемоизация – это способ оптимизации, при котором сохраняется результат выполнения функции,
# и этот результат используется при следующем вызове.
# 1-ый способ:
def fib_1(x):
    cache = {1: 1, 2: 1}

    def fib_rec(n):  # использование вложенной функции, чтобы не делать переменную cache глобальной
        result = cache.get(n)
        if result is None:
            result = fib_rec(n - 2) + fib_rec(n - 1)
            cache[n] = result
        return result
    return fib_rec(x)


# 2-ой способ (используя пользовательские атрибуты функции):
def fib_2(num):
    if num < 2:
        return num
    if num not in fib_2.__dict__:
        fib_2.__dict__[num] = fib_2(num - 1) + fib_2(num - 2)
    return fib_2.__dict__[num]
    

# 3-ий способ (используя декоратор):
# Кэшировать следует только чистые функции (является детерминированной и не обладает побочными эффектами).
from functools import lru_cache  # least recently used (lru) (работает только с хэшируемыми объектами)
@lru_cache(maxsize=80, typed=False)  # при typed=False f(3) и f(3.0) будут кэшироваться одинаково
def fib_3(n):  # maxsize по умолчанию равен 128
    if n <= 2:
        return 1  # для реализации кэширования функция должна возвращать какой-либо результат
    else:
        return fib_3(n - 1) + fib_3(n - 2)


print(fib_1(100))  # 354224848179261915075
print(fib_2(100))  # 354224848179261915075
print(fib_2.__dict__)  # {2: 1, 3: 2, 4: 3, 5: 5, 6: 8, ...}
print(fib_3(100))  # 354224848179261915075
print(fib_3.cache_info())  # CacheInfo(hits=97, misses=100, maxsize=80, currsize=80)
# hits - количество значений, которые lru_cache вернул непосредственно из памяти, поскольку они присутствовали в кэше
# misses - количество значений, которые были вычислены, а не взяты из памяти
# maxsize - размер кэша, который мы определили, передав его декоратору
# currsize - текущий размер кэша


@lru_cache
def ways(n):
    """Функция считает количество способов записи числа n, используя числа 1, 2, 4."""
    if n > 4:
        return ways(n - 1) + ways(n - 3) + ways(n - 4)
    elif n > 3:
        return ways(n - 1) + ways(n - 3)
    elif n > 1:
        return ways(n - 1)
    if n == 1:
        return 1


print(ways(100), ways.cache_info())  # 256319508074468182850 CacheInfo(hits=193, misses=100, maxsize=128, currsize=100)
'''

'''
# ОБЪЕКТНО-ОРИЕНТИРОВАННОЕ ПРОГРАММИРОВАНИЕ (ООП) - методология программирования, основанная
# на представлении программы в виде совокупности объектов, каждый из которых является
# экземпляром определённого класса, а классы образуют иерархию наследования.
# Класс - модель для создания объектов определённого типа, описывающая их структуру и поведение.
class ElectricCar:  # Согласно PEP 8 классы обозначаются с большой буквы (в стиле UpperCamelCase)
    """Электромобиль."""
    engine_type = 'electric motor'  # атрибуты класса представляют собой переменные класса


car = ElectricCar()
car2 = ElectricCar()
car.color = 'black'
car.owner = 'Elon'
setattr(car, 'mileage', 250)  # установить атрибут
delattr(car, 'mileage')  # удалить атрибут (если объект не имеет атрибута, возбуждается исключение AttributeError)
# delattr(car, 'engine_type') # AttributeError: engine_type, т. к. нельзя удалить атрибут класса через объект
print(hasattr(car, 'mileage'))  # False
# При добавлении атрибута в сам класс, атрибут добавляется и к экземплярам класса, которые были созданы раньше:
ElectricCar.fuel = 'electricity'
print(car2.fuel)  # electricity
print(ElectricCar.__dict__)  # {'__module__': '__main__', '__doc__': 'Электромобиль.', ...}
print(car.__dict__)  # выводит атрибуты только экземпляра класса, но не атрибуты самого класса
print(getattr(car, 'color'))  # black
print(getattr(car, 'engine_type', 'no attr'))  # electric motor
print(getattr(car, 'volume', 'no attr'))  # no attr
print(type(car), type(car).__name__)  # <class '__main__.ElectricCar'> ElectricCar
print(car.__class__, car.__class__.__name__)  # <class '__main__.ElectricCar'> ElectricCar


# Методы класса фактически представляют собой функции, которые
# определены внутри класса и которые определяют его поведение.
# Атрибуты класса представляют собой переменные класса.
class SchoolMember:
    """Представляет любого человека в школе."""
    def __init__(self, name, age):  # name, age - атрибуты класса (задаются в методе __init__());
        self.name = name  # self (контекстный объект) - специальный параметр, представляющий собой
        self.age = age    # ссылку на конкретный экземпляр (объект) класса;
        self.example = 7  # задание константы в качестве атрибута
        print('(Создан SchoolMember: {0})'.format(self.name))
        # метод __init__ должен возвращать None иначе будет ошибка

    def __del__(self):  # магический метод __del__ называется финализатор
        print(f'Удаление экземпляра: {self.name} - {self}')

    def tell(self):
        """Вывести информацию."""
        print('Имя: "{0}" Возраст "{1}"'.format(self.name, self.age))


class Teacher(SchoolMember):
    """Представляет преподавателя."""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)  # выполняет метод __init__ в классе SchoolMember
        self.salary = salary
        print('(Создан Teacher {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))


class Student(SchoolMember):
    """Представляет студента."""
    def __init__(self, name, age, marks):
        super().__init__(name, age)  # аналогично SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценка: "{0:d}"'.format(self.marks))


# Метод __init__() инициализирует атрибуты объекта.
# Сразу после создания объекта исполняется метод __init__() (метод инициализации или инициализатор):
shriva = Teacher('Mrs. Shriva', 40, 30000)  # объект (экземпляр) класса
swar = Student('Swar', 25, 75)  # объект (экземпляр) класса
kirill = Student('Kirill', 17, 100)  # объект (экземпляр) класса
members = [shriva, swar]
for member in members:
    member.tell()
SchoolMember.tell(kirill)  # выполняет метод tell() только для SchoolMember
kirill.tell()  # аналогично Student.tell(kirill)
print(SchoolMember, type(SchoolMember))  # <class '__main__.SchoolMember'> <class 'type'>
print(SchoolMember.__doc__)  # Представляет любого человека в школе.
print(shriva)  # <__main__.Teacher object at 0x0000022EC15DFE80>
print(shriva.name, shriva.age, shriva.salary)  # Mrs. Shriva 40 30000
print(shriva.__doc__)  # Представляет преподавателя.
print(shriva.__dict__)  # {'name': 'Mrs. Shriva', 'age': 40, 'example': 7, 'salary': 30000} (все атрибуты объекта)
shriva.salary = 70000  # атрибут объекта можно изменять
print(shriva.name, shriva.age, shriva.salary)  # Mrs. Shriva 40 70000
shriva.company = 'Microsoft'  # необязательно определять атрибуты внутри класса (можно сделать это динамически вне кода)
print(shriva.company)  # Microsoft
ann = SchoolMember('Ann', 23)
ann.tell()  # аналогично Student.tell(ann)


# геттеры, сеттеры, статические методы и методы класса
# Геттеры и сеттеры, позволяют избегать прямого доступа к атрибутам,
# а также добавлять дополнительную логику при изменении их значений.
# Cтатические методы и методы класса могут вызываться как из самого класса, так и экземпляра этого класса.
# Методы класса предназначены для работы с атрибутами класса и переданными аргументами,
# а статические - только с переданными им аргументами.
class ElectricCar:
    cars = []

    def __init__(self, owner):
        print(f'вызов метода __init__() для {owner}')  # В методе __init__() идет обращение к свойству,
        self.owner = owner  # в котором есть проверка на корректность передаваемого аргумента.
        # self._owner = owner # обращения к свойству уже нет (использовать если не определён сеттер)
        type(self).cars.append(self)  # добавление в список всех созданных экземпляров класса
        # ElectricCar.cars.append(self) # аналогично предыдущему
        # self.__class__.cars.append(self) # аналогично предыдущему

    @property
    def owner(self):  # геттер
        print(f'вызов свойства owner (геттер) для {self._owner}')
        return self._owner  # если имя атрибута начинается с одного нижнего подчеркивания, то он считается защищенным

    @owner.setter  # сеттер
    def owner(self, owner):  # имена методов сеттера, геттера и делитера должны совпадать
        print(f'вызов свойства owner (сеттер) для {owner}')
        if isinstance(owner, str) and owner.isalpha():
            self._owner = owner
        else:
            raise ValueError('Передано некорректное значение.')

    @owner.deleter  # делитер
    def owner(self):
        print(f'вызов свойства owner (делитер) для {self._owner}')  # self.owner вызовет ещё и геттер
        del self._owner

    @classmethod  # метод класса
    def defined_owner(cls):
        print('вызов метода класса defined_owner()')
        return cls('Noah')

    @classmethod  # метод класса
    def first_car(cls):  # вывод первого созданного экземпляра класса
        print('вызов метода класса first_car()')
        return cls.cars[0] if cls.cars else None

    @classmethod  # метод класса
    def last_car(cls):  # вывод последнего созданного экземпляра класса
        print('вызов метода класса last_car()')
        return cls.cars[-1] if cls.cars else None

    @classmethod  # метод класса
    def num_of_cars(cls):  # нахождение количества созданных объектов класса
        print('вызов метода класса num_of_cars()')
        return len(cls.cars)

    @staticmethod
    def fuel_consumption(distance):
        """Статические методы в Python - это методы, которые принадлежат классу, а не его
        экземпляру и работают только с передаваемыми аргументами. Они полезны, когда вам
        нужно выполнить какую-то операцию, которая не зависит от состояния объекта."""
        print(f'вызов статического метода fuel_consumption() для {distance}')
        return f'{20 * distance / 100} liters of gasoline'


car = ElectricCar('Elon')
print(car.owner)
# car.owner = ['Gvido', 'Elon'] # ValueError: Передано некорректное значение.
car1 = ElectricCar('Mike')
car2 = ElectricCar('Jack')
print(hasattr(car2, '_owner'))  # True
del car2.owner
print(hasattr(car2, '_owner'))  # False
car3 = ElectricCar('Henry')
print(ElectricCar.first_car().owner)  # Elon
print(ElectricCar.last_car().owner)  # Henry
print(ElectricCar.num_of_cars())  # 4
print(ElectricCar.fuel_consumption(1000))  # 200.0 liters of gasoline
car4 = ElectricCar.defined_owner()
print(car4.owner)  # Noah
# Если в классе задан атрибут как объект-свойство, то в первую очередь выбирается оно,
# даже если в экземпляре класса есть локальное свойство с таким же именем:
car4.__dict__['owner'] = 'Kirill'
print(car4.__dict__, car4.owner)  # {'_owner': 'Noah', 'owner': 'Kirill'} Noah


# протокол дескрипторов
# магические метода __get__(), __set__(), __delete__(), __set_name__()
# Дескриптор - объект, чьё поведение при доступе к нему как к атрибуту переопределяется методами протокола дескрипторов.
class NonNegativeInteger:
    def __init__(self, default=None):
        self.default = default

    def __set_name__(self, cls, name):               # Позволяет неявно использовать имя переменной
        print(f'вызов метода __set_name__ для: {cls = }, {name = }')   # в качестве имени атрибута,
        self.name = name                                   # за которым будет закреплён дескриптор.

    def __get__(self, obj, cls):
        print(f'вызов метода __get__ для: {obj = }, {cls = }')
        if obj is None:  # нужно, чтобы не было ошибки при обращении к дескриптору через сам класс
            return self
        if self.name in obj.__dict__:
            return obj.__dict__[self.name]
        elif self.default is None:
            raise AttributeError('Атрибут не найден')
        else:
            return self.default

    def __set__(self, obj, value):  # Если метод __set__() не определён, то дескриптор является дескриптором не-данных
        print(f'вызов метода __set__ для: {obj = }, {value = }')  # (non-data descriptor) и строка student.score будет
        if isinstance(value, int) and value >= 0:  # обращаться к атрибуту score, а не к дескриптору, аналогично
            obj.__dict__[self.name] = value  # и self.score = score приведёт к установке объекту self атрибута score.
        else:
            raise ValueError('Некорректное значение')

    def __delete__(self, obj):
        print(f'вызов метода __delete__ для: {obj = }')
        del obj.__dict__[self.name]


class Student:
    score = NonNegativeInteger(50)
    score2 = 37


student = Student()
print(student.score)  # 50
print(student.score2)  # 37
student.score = 100
print(student.score)  # 100
print(student.__dict__)  # {'score': 100}
print(Student.score)  # <__main__.NonNegativeInteger object at 0x0000022EFFE2BFD0>
print(Student.score.__class__)  # <class '__main__.NonNegativeInteger'>
del student.score
print(student.__dict__)  # {}


# строковое представление объектов класса
# Если в классе определён метод __repr__(), но не определён метод __str__(),
# то по умолчанию при вызове __str__ используется __repr__.
class AnyClass:
    def __init__(self, **kwargs):
        print(f'вызов метода __init__() для {kwargs}')
        self.__dict__.update(kwargs)  # установка передаваемых аргументов в качестве атрибутов

    def __str__(self):  # неформальное строковое представление
        print(f'вызов метода __str__()')
        return f'AnyClass: {", ".join(self._attrs())}'

    def __repr__(self):  # формальное строковое представление
        print(f'вызов метода __repr__()')
        return f'AnyClass({", ".join(self._attrs())})'

    def _attrs(self):
        print(f'вызов метода _attrs()')
        return [f'{k}={repr(v)}' for (k, v) in self.__dict__.items()]


attrs = {'name': 'Guido van Rossum',
         'birth_date': '31.01.1956',
         'age': 67,
         'career': 'Python guru'}
obj = AnyClass(**attrs)
print(obj.name)  # Guido van Rossum
print(obj.birth_date)  # 31.01.1956
print(obj.age)  # 67
print(obj.career)  # Python guru
print(obj)  # за кулисами вызывается obj.__str__()
print(str(obj))  # AnyClass: name='Guido van Rossum', birth_date='31.01.1956', age=67, career='Python guru'
print(repr(obj))  # AnyClass(name='Guido van Rossum', birth_date='31.01.1956', age=67, career='Python guru')
print(hasattr(obj, '__iter__'))  # False
print(dir(obj))


# сравнение объектов класса и магический метод __hash__()
from functools import total_ordering
# Декоратор total_ordering нужен для того, чтобы определить метод __eq__
# и один из методов: lt, le, gt, ge. Остальные определятся автоматически.
# Если декоратор не реализован, то достаточно объявить eq, lt, le, остальные методы будут работать инверсионно:
# - для obj1 != obj2 будет выполнено not (obj1 == obj2)
# - для obj1 > obj2 будет выполнено obj2 < obj1 (операнды меняются местами)
@total_ordering
class ElectricCar:
    def __init__(self, power_reserve):
        print(f'вызов метода __init__() для {power_reserve}')
        self.power_reserve = power_reserve

    def __eq__(self, other):  # если метод не определён, то по умолчанию сравниваются id экземпляров класса
        print('вызов метода __eq__()')
        if isinstance(other, ElectricCar):  # аналогично isinstance(other, type(self))
            return self.power_reserve == other.power_reserve
        return NotImplemented  # рекомендуется возвращать константу NotImplemented при сравнении объектов

    def __lt__(self, other):
        print('вызов метода __lt__()')
        if isinstance(other, ElectricCar):  # аналогично isinstance(other, type(self))
            return self.power_reserve < other.power_reserve
        return NotImplemented

    def __hash__(self):
        print('вызов метода __hash__()')
        return hash(self.power_reserve)


car1 = ElectricCar(400.5)
car2 = ElectricCar(330.4)
print(car1 >= car2)  # True
print(car1 <= car2)  # False
print(car1.__eq__(500))  # NotImplemented
print(hash(car1), hash(car2))  # 1152921504606847376 922337203685425482
print(hasattr(car1, '__hash__'))  # True
print(dir(car1))


# унарные операторы
class Matrix:
    def __init__(self, rows, cols, value=0):
        print(f'вызов метода __init__()')
        self.rows = rows
        self.cols = cols
        self.value = value
        self._matrix = [[value] * cols for _ in range(rows)]

    def get_value(self, row, col):
        print('вызов метода get_value()')
        return self._matrix[row][col]  # нижнее подчёркивание означает, что атрибут защищённый

    def set_value(self, row, col, value):
        print('вызов метода set_value()')
        self._matrix[row][col] = value

    def __str__(self):
        string_matrix = [[str(ele) for ele in row] for row in self._matrix]
        return '\n'.join(' '.join(row) for row in string_matrix)

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __pos__(self):
        print('вызов метода __pos__()')
        matrix = Matrix(self.rows, self.cols)  # создаётся новый объект
        for row in range(matrix.rows):
            for col in range(matrix.cols):
                matrix.set_value(row, col, self.get_value(row, col))
        return matrix

    def __neg__(self):
        print('вызов метода __neg__()')
        matrix = Matrix(self.rows, self.cols)  # создаётся новый объект
        for row in range(matrix.rows):
            for col in range(matrix.cols):
                matrix.set_value(row, col, -self.get_value(row, col))
        return matrix

    def __round__(self, n):
        print('вызов метода __round__()')
        matrix = Matrix(self.rows, self.cols)  # создаётся новый объект
        for row in range(matrix.rows):
            for col in range(matrix.cols):
                matrix.set_value(row, col, round(self.get_value(row, col), n))
        return matrix

    def __invert__(self):
        print('вызов метода __invert__()')
        matrix = Matrix(self.cols, self.rows)  # создаётся новый объект
        for row in range(self.cols):
            for col in range(self.rows):
                matrix.set_value(row, col, self.get_value(col, row))
        return matrix


matrix = Matrix(2, 3, 1)
matrix.set_value(1, 2, 8)
print(matrix)
print([matrix, matrix])  # [Matrix(2, 3), Matrix(2, 3)] (для объектов коллекций по умолчанию вызывается метод __repr__)
print(repr(matrix))
print(-matrix)
print(~matrix)
print(hasattr(matrix, '__pos__'))  # True
print(dir(matrix))
methods = {k: v for k, v in Matrix.__dict__.items() if callable(v)}  # методы класса Matrix
print(methods)
print(Matrix.__dict__)


# арифметические операции
class Vector:
    def __init__(self, x, y):
        print(f'вызов метода __init__()')
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):  # если __iadd__ не реализован, то используется __add__
        print('вызов метода __add__()')
        if isinstance(other, Vector):  # аналогично isinstance(other, type(self))
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __iadd__(self, other):  # в отличие от метода __add__, метод __iadd__ изменяет текущий объект
        """i означает inplace (на месте)"""
        print('вызов метода __iadd__()')
        if isinstance(other, Vector):  # аналогично isinstance(other, type(self))
            self.x += other.x
            self.y += other.y
            return self
        return NotImplemented

    def __sub__(self, other):  # если __isub__ не реализован, то используется __sub__
        print('вызов метода __sub__()')
        if isinstance(other, Vector):  # аналогично isinstance(other, type(self))
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other):  # если __imul__ не реализован, то используется __mul__
        print('вызов метода __mul__()')
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):  # реализация умножения, не учитывающего порядок операндов
        print('вызов метода __rmul__()')
        return self.__mul__(other)

    def __truediv__(self, other):  # если __itruediv__ не реализован, то используется __truediv__
        print('вызов метода __truediv__()')
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other)
        return NotImplemented


a = Vector(1, 2)
b = Vector(3, 4)
print(a + b)  # Vector(4, 6)
print(a - b)  # Vector(-2, -2)
print(b + a)  # Vector(4, 6)
print(b - a)  # Vector(2, 2)
print(a * 2)  # Vector(2, 4)
print(2 * a)  # Vector(2, 4)
print(a / 2)  # Vector(0.5, 1.0)
a += b
print(a)  # Vector(4, 6) (изменение текущего объекта)
print(hasattr(a, '__add__'))  # True
print(dir(a))
methods = {k: v for k, v in Vector.__dict__.items() if callable(v)}  # методы класса Vector
print(methods)
print(Vector.__dict__)


# вызываемые объекты, магический метод __call__() (альтернатива замыканию)
class QuadraticPolynomial:
    def __init__(self, a, b, c):
        print(f'вызов метода __init__()')
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        print('вызов метода __call__()')
        return self.a * x ** 2 + self.b * x + self.c

    def __abs__(self):
        print(self.__dict__)
        return sum(i ** 2 for i in self.__dict__.values()) ** 0.5


func = QuadraticPolynomial(1, 2, 1)
print(func(1))  # 4
print(func(2))  # 9
print(hasattr(func, '__call__'))  # True
print(dir(func))
print(abs(func))  # 2.449489742783178


# магические методы __getattribute__(), __setattr__(), __delattr__()
# Разница между __getattribute__() и __getattr__() в том, что __getattribute__() вызывается первым и вызывается всегда,
# а метод __getattr__() вызывается только в том случае, если атрибута, к которому происходит обращение, не существует.
class ProtectedObject:
    """Класс запрещает получение, изменение и удаление защищенных атрибутов своих экземпляров."""
    def __init__(self, **kwargs):
        print(f'вызов метода __init__()')
        for name, value in kwargs.items():
            object.__setattr__(self, name, value)
            # setattr(self, name, value)  # приведёт к ошибке, т. к. вызовется метод __setattr__

    def __getattribute__(self, name):
        print('вызов метода __getattribute__()')
        if name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        print('вызов метода __setattr__()')
        if name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        print('вызов метода __delattr__()')
        if name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__delattr__(self, name)


user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')
user.login = 'new_login'
print(user.login)
del user.login
# print(user._password) # AttributeError: Доступ к защищенному атрибуту невозможен


# протокол итерируемых объектов и итераторов
# магические методы __iter__() и __next__()
# Протокол - это набор методов, который должен быть реализован классом.
class Square:
    def __init__(self, n):  # конструктор класса, вызывается единожды при создании объекта
        self.n = n

    def __iter__(self):  # Метод, который преобразует итерируемый объект в итератор (для итерируемых объектов),
        self.zero = 0  # либо возвращает сам итератор (сам себя).
        return self

    def __next__(self):  # метод, который возвращает следующий элемент или возбуждает исключение StopIteration
        if self.zero == self.n:
            raise StopIteration  # без "raise StopIteration" получим бесконечный итератор
        self.zero += 1
        return self.zero ** 2


squares = Square(10)
print(list(squares))  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


class SkipIterator:
    def __init__(self, iterable, n):
        print(f'вызов метода __init__()')
        self.obj = iter(list(iterable)[:: n + 1])  # отступы в срезе согласно PEP 8

    def __iter__(self):
        print('вызов метода __iter__()')
        return self
        # yield from self.obj  # если передаваемый объект не является итератором

    def __next__(self):
        print('вызов метода __next__()')
        return next(self.obj)


skip_iterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)  # пропускаем по два элемента
print(next(skip_iterator))  # 1
print(*skip_iterator)  # 4 7 10
print(hasattr(skip_iterator, '__next__'))  # True
print(dir(skip_iterator))


# протокол последовательностей
# магические методы: __getitem__(), __setitem__(), __delitem__(), __contains__()
class Order:
    def __init__(self, cart, customer):
        print(f'вызов метода __init__()')
        self.cart = list(cart)
        self.customer = customer

    def check_key(self, key):  # отдельный метод для проверки индекса на корректность
        print('вызов метода check_key()')
        if not isinstance(key, (int, slice)):
            raise TypeError('Индекс должен быть целым числом или срезом')
        if isinstance(key, int):
            if key < 0 or key >= len(self.cart):
                raise IndexError('Неверный индекс')
        return key

    def __len__(self):  # Если в классе определен магический метод __len__(), но не определен
        print('вызов метода __len__()')  # магический метод __bool__(), то именно __len__() будет
        return len(self.cart)  # использоваться для всех логических приведений.

    def __getitem__(self, key):  # определяет поведение при доступе к элементу, используя синтаксис self[key]
        print('вызов метода __getitem__()')
        key = self.check_key(key)
        if isinstance(key, slice):
            return Order(self.cart[key], self.customer)  # key аналогично slice(key.start, key.stop, key.step)
        return self.cart[key]

    def __contains__(self, item):  # определяет поведение при проверке на принадлежность с помощью оператора in (not in)
        print('вызов метода __contains__()')
        return item in self.cart

    def __iter__(self):  # метод __iter__() позволяет обойти экземпляр класса через цикл
        print('вызов метода __iter__()')
        yield from self.cart

    def __setitem__(self, key, value):  # Определяет поведение при присваивании значения элементу,
        print('вызов метода __setitem__()')  # используя синтаксис self[key] = value.
        key = self.check_key(key)
        self.cart[key] = value

    def __delitem__(self, key):  # определяет поведение при удалении элемента с помощью оператора del
        print('вызов метода __delitem__()')
        key = self.check_key(key)
        del self.cart[key]

    def __reversed__(self):
        print('вызов метода __reversed__()')
        return reversed(self.cart)


order = Order(['банан', 'яблоко', 'лимон'], 'Кемаль')
print(*order, sep=', ')  # банан, яблоко, лимон
order[1] = 'ананас'
del order[2:]
print(*order, sep=', ')  # банан, ананас
print(*order[2:])  # банан, ананас
for i in order:
    print(i)
print(hasattr(order, '__getitem__'))  # True
print(dir(order))
print(bool(order))  # вызывается функция __len__, так как __bool__ не определён


# Срезы в Python реализуются с помощью slice объектов. Именно они автоматически создаются
# и указываются в качестве индексов, когда мы используем синтаксис срезов.
nums = [1, 2, 3, 4, 5]
print(nums[slice(1, None, None)])  # равнозначно nums[1:]
print(nums[slice(3)])              # равнозначно nums[:3]
print(nums[slice(1, 3)])           # равнозначно nums[1:3]
print(nums[slice(1, 4, 2)])        # равнозначно nums[1:4:2]

slice1 = slice(10)
print(slice1, type(slice1))  # slice(None, 10, None) <class 'slice'>
print(slice1.start, slice1.stop, slice1.step)  # None 10 None


# протокол контекстных менеджеров, магические методы: __enter__(), __exit__()
import sys
class UpperPrint:
    def __enter__(self):
        print('вход в контекстный менеджер')
        self.original_write = sys.stdout.write
        sys.stdout.write = self.upper_write
        return self

    def upper_write(self, text):
        self.original_write(text.upper())

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write
        print('выход из контекстного менеджера')


with UpperPrint():
    print('Проверка функции UpperPrint')  # ПРОВЕРКА ФУНКЦИИ UPPERPRINT


import copy
class Atomic:
    """Возврат к исходной коллекции при ошибке (способ 1)."""
    def __init__(self, data, deep=False):
        self.data = data
        self.deep = deep
        self.copy = copy.deepcopy(self.data) if deep else copy.copy(self.data)

    def __enter__(self):
        return self.copy

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is None:
            self.data.clear()
            if isinstance(self.data, list):
                self.data.extend(self.copy)
            else:
                self.data.update(self.copy)
        return True  # обработка всех типов исключений


numbers = [1, 2, 3, 4, 5]
with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[1]
print(numbers)  # [1, 0, 4, 5, 6]
numbers = [1, 2, 3, 4, 5]
with Atomic(numbers) as atomic:
    del atomic[100]
print(numbers)  # print(numbers)


class DefenderVector:
    """Возврат к исходной коллекции при ошибке (способ 2)."""
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]  # делаем копию вектора v
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp
        return False


v1 = [1, 2, 3]
v2 = [1, 2]
try:
    with DefenderVector(v1) as dv:
        for i, _ in enumerate(dv):
            dv[i] += v2[i]
except Exception as error:
    print(error)
print(v1)  # [1, 2, 3]
try:
    with DefenderVector(v1) as dv:
        for i, _ in enumerate(dv):
            dv[i] += v1[i]
except Exception as error:
    print(error)
print(v1)  # [2, 4, 6]


# реентерабельный контекстный менеджер
class TreeBuilder:
    """Построение дерева, используя принцип стека.
    При входе в контекстный менеджер в стек добавляется список, при выходе - удаляется.
    Последний элемент стека считается текущим, именно в него происходит добавление значения при вызове метода add()."""
    def __init__(self):
        self.knots = [[]]

    def __enter__(self):
        self.knots.append([])

    def __exit__(self, *args, **kwargs):
        if self.knots[-1]:
            self.knots[-2].append(self.knots[-1])
        self.knots.pop()

    def add(self, value):
        self.knots[-1].append(value)

    def structure(self):
        return self.knots[-1]


tree = TreeBuilder()
with tree:
    tree.add(1)
    tree.add(2)
    with tree:
        tree.add(3)
        with tree:
            tree.add(4)
    with tree:
        tree.add(5)
print(tree.structure())  # [[1, 2, [3, [4]], [5]]]


# магический метод __new__()
TYPE_OS = 1  # 1 - Windows; 2 - Linux
class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        obj = DialogWindows() if TYPE_OS == 1 else DialogLinux()
        setattr(obj, 'name', args[0])
        return obj


dlg1 = Dialog('windows')
TYPE_OS = 2
dlg2 = Dialog('linux')
TYPE_OS = 1
print(dlg1, dlg1.name_class)  # <__main__.DialogWindows object at 0x0000028C09183EB0> DialogWindows
print(dlg2, dlg2.name_class)  # <__main__.DialogLinux object at 0x0000028C09183E50> DialogLinux


# наследование и магический метод __new__()
# cls ссылается на класс, self ссылается на экземпляр класса
class Animal:
    def __new__(cls, *args, **kwargs):  # Произвольное количество позиционных и именованных аргументов в методе
        print('1. Вызов метода __new__()')  # __new__() необходимо для того чтобы не ограничивать сигнатуру метода
        print(cls)  # __init__(), так как аргументы, передаваемые классу при создании его экземпляра
        print(args, kwargs)  # попадают как в метод __new__(), так и в метод __init__().
        return super().__new__(cls)  # равнозначен object.__new__(Cat)

    def __init__(self, name, age):
        print('2. Вызов метода __init__()')
        print(self)
        self.name = name
        self.age = age


class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # неявное обращение к методу __init__() родительского класса
        # super(Cat, self).__init__(name, age) # аналогично предыдущему
        # Animal.__init__(self, name, age) # аналогично предыдущему
        self.breed = breed


cat = Cat('Кемаль', 1, breed='манчкин')
print(cat.name, cat.age, cat.breed)
print(hasattr(cat, '__new__'))
print(dir(cat))  # True
# Порядок, в котором просматриваются классы во время поиска конкретного
# метода или атрибута называется Method Resolution Order (MRO):
print(Cat.mro())  # [<class '__main__.Cat'>, <class '__main__.Animal'>, <class 'object'>]


# наследование от неизменяемых типов данных
class Distance(float):  # При наследовании от неизменяемых типов данных их значение определяется при создании, то есть
    def __new__(cls, value, unit):  # в методе __new__(), и менять его в инициализаторе уже поздно. Кроме того,
        instance = super().__new__(cls, value)  # выражение Distance(1, 'Meters') сперва вызывает метод __new__()
        instance.unit = unit  # класса float, который принимает лишь один аргумент - числовое или строковое значение,
        return instance  # на основе которого будет создано число, а в нашем случае их передается два.


distance = Distance(1, 'Meters')
print(distance)  # 1.0
print(distance.unit)  # Meters
print(issubclass(Distance, float))  # True (функция работает только с классами)
print(isinstance(Distance, float))  # False (функция работает как с классами, так и с объектами классов)
print(isinstance(distance, float))  # True
print(type(Distance))  # <class 'type'>
print(Distance)  # <class '__main__.Distance'>
print(type(distance))  # <class '__main__.Distance'>


# наследование и атрибуты protected (одно нижнее подчёркивание) и private (два нижних подчёркивания)
class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    @staticmethod
    def __verify_coord(coord):
        return 0 <= coord <= 100


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self.__fill = fill

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def _check(self, coord):
        return super().__verify_coord(coord)  # запрещено переопределять приватные методы базового класса в дочернем


r = Rect(0, 0, 10, 20)
print(r.__dict__)  # {'_Geom__x1': 0, '_Geom__y1': 0, '_Geom__x2': 10, '_Geom__y2': 20, '_Rect__fill': 'red'}
# Приватные атрибуты жестко привязываются к текущему классу, поэтому
# нельзя обращаться к приватным свойствам-координатам в дочернем классе Rect:
# print(r.get_coords())  # AttributeError
# Если нужно определить закрытые атрибуты, доступные в текущем классе и во всех его дочерних классах,
# то для этого следует использовать метод определения protected – одно нижнее подчеркивание.
# print(r._check(50))  # AttributeError


# абстрактные классы
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod  # все абстрактные методы дочерних классов должны быть переопределены, иначе будет ошибка TypeError
    def sound(self):
        """В абстрактном методе можно оставлять только комментарий."""

    @abstractmethod
    def move(self):
        print('Животное движется')


class Cat(Animal):
    def sound(self):
        print('мяу')

    def move(self):
        super().move()
        print('Кот движется')


cat = Cat()
cat.move()  # Кот движется
cat.sound()  # мяу
print(isinstance(Cat, Animal))  # False (функция работает как с классами, так и с объектами классов)
print(isinstance(cat, Animal))  # True
print(issubclass(Cat, Animal))  # True (функция работает только с классами)


# множественное наследование
from abc import ABC, abstractmethod
class Family(ABC):
    def __init__(self, mood='neutral'):
        self.mood = mood

    @abstractmethod
    def greet(self):
        pass


class Father(Family):
    def greet(self):
        return 'Hello!'

    def be_strict(self):
        self.mood = 'strict'


class Mother(Family):
    def greet(self):
        return 'Hi, honey!'

    def be_kind(self):
        self.mood = 'kind'


class Daughter(Mother, Father):
    pass


class Son(Father, Mother):
    pass


son = Son()
daughter = Daughter()
print(son.greet())
print(daughter.greet())
print(son.mood)
son.be_kind()
print(son.mood)
print(Son.mro())
print(Daughter.mro())


# слоты, атрибут __slots__ (более быстрый доступ к атрибутам экземпляров классов и экономия памяти)
# Слоты следует использовать когда экземпляры класса имеют фиксированный набор аргументов.
class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point2D):
    __slots__ = ('z',)

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


point = Point3D(1, 2, 3)
print(Point2D.__slots__)  # ('x', 'y')
print(Point3D.__slots__)  # ('z',)
print(point.__slots__)  # ('z',)
print(point.x, point.y, point.z)  # 1 2 3
point.x = 10
print(point.x)
# print(point.__dict__) # AttributeError: 'Point3D' object has no attribute '__dict__'. Did you mean: '__dir__'?
# point.d = 3 # AttributeError: 'Point3D' object has no attribute 'd'


# классы декораторы
# Использование классов декораторов может быть выгодно тем, что они избавляют от тройной
# последовательной вложенности функций и делают код более простым для понимания.
import functools
class do_twice:
    def __init__(self, func):
        functools.update_wrapper(self, func)  # сохранение информации о декорируемой функции
        self.func = func  # декорируемая функция

    def __call__(self, *args, **kwargs):
        for _ in range(2):
            value = self.func(*args, **kwargs)  # вызов декорируемой функции
        return value


@do_twice
def greet(name):
    print(f'Привет, {name}!')


greet('Кемаль')


class do_n_times:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):  # передача декорируемой функции
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(self.n):
                value = func(*args, **kwargs)  # вызов декорируемой функции
            return value
        return wrapper


def greet(name):
    print(f'Привет, {name}!')


decorator = do_n_times(4)  # создание экземпляра класса do_n_times
greet = decorator(greet)  # вызов экземпляра класса do_n_times
greet('Рождер')


# декорирование классов
import functools
def count_instances(cls):
    old_init = cls.__init__  # сохранение исходного инициализатора
    cls.count = 0  # счетчик созданных экземпляров декорируемого класса

    @functools.wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)  # вызов исходного инициализатора
        cls.count += 1  # увеличение счетчика на единицу

    cls.__init__ = new_init  # замена исходного инициализатора новым
    return cls


@count_instances
class MyClass:
    pass


print(MyClass.count)  # 0
for _ in range(10):
    obj = MyClass()
print(MyClass.count)  # 10


def add_attr_to_instances(**attrs):
    def decorator(cls):
        old_init = cls.__init__

        @functools.wraps(old_init)
        def new_init(self, *args, **kwargs):
            old_init(self, *args, **kwargs)
            self.__dict__.update(attrs)  # добавление атрибута экземпляру декорируемого класса

        cls.__init__ = new_init
        return cls

    return decorator


@add_attr_to_instances(first_attr=1, second_attr=2)
class MyClass:
    pass


obj = MyClass()
print(obj.first_attr)  # 1
print(obj.second_attr)  # 2


def class_log(log_descriptor):
    """Функцию-декоратор для класса, которая создаёт логирование вызовов методов
    класса (добавляет в список log_descriptor все вызванные методы)."""
    def decorator(method):
        def wrapper(*args, **kwargs):
            log_descriptor.append(method.__name__)
            return method(*args, **kwargs)

        return wrapper

    def class_decorator(cls):
        for k, v in cls.__dict__.items():
            if callable(v):
                setattr(cls, k, decorator(v))
        return cls

    return class_decorator


vector_log = []


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
v[1]
print(vector_log)  # ['__init__', '__setitem__', '__getitem__']


# модуль dataclasses (автоматически реализуют: __init__(), __repr__() и __eq__())
from dataclasses import dataclass, field, astuple, asdict
# (frozen=False) атрибуты класса можно менять; (order=True) можно сравнить экземпляры класса >, <, <=, >= 
@dataclass(frozen=False, order=True)
class Point:
    x: float = 0.0
    y: float = 0.0
    coordinates: list = field(default_factory=list, repr=False)  # пустой список в качестве значения по умолчанию
    quadrant: int = field(init=False, compare=False, default=0)

    def __post_init__(self):  # второй инициализатор, который зависит от значений атрибутов
        if self.x > 0 and self.y > 0:
            self.quadrant = 1
        elif self.x < 0 < self.y:
            self.quadrant = 2
        elif self.x < 0 and self.y < 0:
            self.quadrant = 3
        elif self.x > 0 > self.y:
            self.quadrant = 4
        else:
            self.quadrant = 0

    def symmetric_x(self):
        return Point(self.x, -self.y)

    def symmetric_y(self):
        return Point(-self.x, self.y)


point = Point(1, 2)
print(point == Point(1, 2))  # True
print(point <= Point(2, 2))  # True (последовательное сравнение значений всех атрибутов для которых compare=True)
print(point > Point(1, 3))  # False
print(point)  # Point(x=1, y=2, quadrant=1)
print(point.quadrant)  # 1
print(point.symmetric_x())  # Point(x=1, y=-2, quadrant=4)
print(point.symmetric_y())  # Point(x=-1, y=2, quadrant=2)
point.coordinates.extend([(1, 2), (1, 1)])
print(point.coordinates)  # [(1, 2), (1, 1)]
print(asdict(point))  # {'x': 1, 'y': 2, 'coordinates': [(1, 2), (1, 1)], 'quadrant': 1}
print(astuple(point))  # (1, 2, [(1, 2), (1, 1)], 1)
'''

'''
# ДАТА И ВРЕМЯ
# МОДУЛЬ DATETIME
from datetime import datetime, date, time, timedelta
import locale
print(datetime.min, datetime.max)  # 0001-01-01 00:00:00 9999-12-31 23:59:59.999999
my_date = date(2014, 7, 21)
print(my_date)  # 2014-07-21 (год-месяц-число)
my_time = time(10, 45, 17)  # 10:45:17
# Строковое представление объекта в неформальном виде (понятному человеку):
print(str(my_time), my_time)  # 10:45:17 10:45:17
# Строковое представление объекта в формальном виде (понятному интерпретатору Python):
print(repr(my_time))  # datetime.time(10, 45, 17)
my_datetime = datetime.combine(my_date, my_time)  # объединение даты и времени
print(my_datetime)  # 2014-07-21 10:45:17
print(datetime(1961, 4, 12, 14, 47, 45, 123456))  # 2023-07-10 10:35:04.296997
now = datetime.now()
print(now, type(now))  # 2023-07-16 08:42:15.291273 <class 'datetime.datetime'>
print(now.date(), type(now.date()))  # 2023-07-20 <class 'datetime.date'>
print(now.time(), type(now.time()))  # 21:01:05.839087 <class 'datetime.time'>
print(now.day)  # 15 (число месяца)
print(now > my_datetime)  # True (дату можно сортировать и сравнивать) (только одинаковые классы, например date с date)
# Преобразование объектов datetime, date, time в строку:
print(now.strftime('%H:%M:%S (%j, %W)'))  # 10:04:13 (197, 28) (%j - номер дня от начала года, %W - номер недели)
print(now.strftime('%A %d, %B %Y'))  # Sunday 16, July 2023
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
print(now.strftime('%A %d, %B %Y'))  # воскресенье 16, Июль 2023
# Преобразование строки ТОЛЬКО в объект datetime:
my_datetime = datetime.strptime('time = 10/08/2034 13-55-59', 'time = %d/%m/%Y %H-%M-%S')
print(my_datetime)  # 2034-08-10 13:55:59
print(now.weekday())     # 5 (день недели: 0 - пн, 1 - вт и т. д.)
print(now.isoweekday())  # 6 (день недели: 1 - пн, 2 - вт и т. д.)
datetime1 = datetime(1992, 10, 6, 10, 12, 45)
datetime2 = datetime1.replace(year=2995, month=12, day=17, hour=14, minute=37)  # replace не изменяет старый объект
print(datetime1)  # 1992-10-06 10:12:45
print(datetime2)  # 2995-12-17 14:37:45
print(date.toordinal(now))  # 738717 (преобразование объекта типа date в номер дня, начиная с 0001-01-01)
print(date.fromordinal(777777))  # 2130-06-25 (метод, позволяющий создать объект типа date из номера дня)

# МОДУЛЬ TIMEDELTA (значение может быть как положительным, так и отрицательным)
# С timedelta можно проводить операции сложения, вычитания, деления и умножения.
# С объектами datetime, date можно проводить операции сложения и вычитания,
# однако нельзя складывать и вычитать datetime с date и наоборот (класс должен совпадать).
delta = timedelta(weeks=-1, days=3, hours=10, minutes=15, seconds=50, milliseconds=9, microseconds=2)
print(delta, type(delta))  # -4 days, 10:15:50.009002 <class 'datetime.timedelta'>
print(delta.total_seconds())  # -308649.990998 (перевод в секунды)
span = now - delta  # однако (delta - now) вызовет ошибку, т. к. нельзя вычитать datetime.timedelta от datetime.datetime
print(span, type(span))  # 2023-08-02 06:14:43.392332 <class 'datetime.datetime'>
print(datetime(2021, 1, 1, 12, 15, 20) - datetime(2020, 5, 1, 10, 5, 10))  # 245 days, 2:10:10
print(7 * timedelta(weeks=1, hours=2))  # 49 days, 14:00:00
print(timedelta(weeks=1, seconds=42) / 7)  # 1 day, 0:00:06 (7 / timedelta(weeks=1, seconds=42) вызовет ошибку)
print(timedelta(weeks=1) / timedelta(hours=5))  # 33.6 (единица измерения делимого, т. е. часы)
# Вычисление времени до указанного:
print(timedelta(hours=21, minutes=0) - timedelta(hours=now.hour, minutes=now.minute))  # 0:21:00
'''

'''
# МОДУЛЬ TIME (ВЫЧИСЛЕНИЕ СКОРОСТИ РАБОТЫ ПРОГРАММЫ)
import time
time.sleep(3.24)  # задержка выполнения программы на заданное количество секунд
print(time.time())  # 1691323930.4258037 (количество секунд, прошедших с момента начала эпохи (1 января 1970))
# Очередной вызов функции time() может вернуть значение меньше, чем значение, полученное при предыдущем вызове.

# вычисление скорости работы программы
start = time.perf_counter()  # методы по убыванию точности: perf_counter(), monotonic(), time()
# код, скорость которого проверяется
end = time.perf_counter()
print(end - start)  # 6.00004568696022e-07
'''

'''
# МОДУЛЬ TIMEIT (ВЫЧИСЛЕНИЕ СКОРОСТИ РАБОТЫ ПРОГРАММЫ)
import timeit
code_to_test = """
x = 5  # код, скорость которого проверяется
for i in range(10000):
    x += i
"""
elapsed_time = timeit.timeit(code_to_test, number=1000) / 1
print(elapsed_time)
'''

'''
# МОДУЛЬ CALENDAR
import calendar
import locale
print(list(calendar.day_name))  # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(list(calendar.day_abbr))  # ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(list(calendar.month_name))  # ['', 'January', 'February' и т. д.] (0-ой элемент пустой т. к. январь - 1-ый месяц)
print(list(calendar.month_abbr))  # ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct' и т. д.]
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
print(list(calendar.day_name))  # ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
print(list(calendar.day_abbr))  # ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
print(list(calendar.month_name))  # ['', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август' и т. д.]
print(list(calendar.month_abbr))  # ['', 'янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт' и т. д.]
print(calendar.isleap(2020))  # True (проверка года на високосность)
print(calendar.leapdays(2020, 2025))  # 2 (количество високосных лет в диапазоне, не включая правую границу)
print(calendar.weekday(2021, 9, 2))  # 3 (четверг; функция возвращает день недели)
print(calendar.monthrange(2022, 1))  # (5, 31) (день недели первого дня месяца, количество дней в месяце)
print(*calendar.monthcalendar(2021, 9), sep='\n')  # матрица, представляющая собой календарь на месяц
print(calendar.month(2021, 9, w=1, l=1))  # возвращает календарь на месяц (w - ширина столбца, l - ширина строки)
print(calendar.calendar(2021, w=1, l=1, c=10, m=12))  # календарь на весь год (m - количество столбцов)
'''

'''
# ИМПОРТ СОБСТВЕННОГО МОДУЛЯ (другого файла, написанного в python и не только)
import heat  # при импорте модуля, выполняется код этого модуля только один раз
import pprint  # pretty print
pprint.pprint(dir(heat))  # получим список атрибутов модуля, в том числе все переменные
print(heat)  # <module 'heat' from 'C:\\Users\\Валерий\\PycharmProjects\\untitled1\\heat.py'> (путь модуля)
'''
'''
# from heat import * # звёздочка импортирует все переменные
# не рекомендуется вызывать все переменные модуля через звёздочку, т. к. может случиться конфликт имён с текущим модулем
from heat import m, h  # можно импортировать конкретную переменную
print('m equals', m)  # m equals 20
print('h equals', h)  # h equals 0.02
print(globals())  # в словарь включаются импортированные переменные m и h
print(locals())  # в словарь включаются импортированные переменные m и h
'''
'''
from function import pri as pr  # при импортировании функции скобки с переменными не нужны
pr(6)
'''
'''
import function as fun  # импортируемый файл имеют имя названия модуля (function)
fun.pri(5)
print(__name__)  # основной файл имеет имя __main__
print(fun.math.pi)  # При таком вызове в модуле function должен быть импортирован модуль math,
однако лучше напрямую импортировать модуль math в текущем модуле.
'''

'''
# МОДУЛЬ SYS
import sys
# Поток ввода (sys.stdin) - это специальный объект в программе, куда попадает весь текст, который ввёл пользователь.
data = sys.stdin.readlines()  # метод readlines() конвертирует итератор sys.stdin в список
print(data)  # для завершения работы программы нажать ctrl + D
sys.stdout.write('Hello ')  # поток вывода (в отличие от print нет перехода на новую строку)
sys.stdout.write('world!')  # Hello world!
# sys.stdout.write(17) (выведет ошибку, т. к. необходимо преобразовать данные к строковому типу данных)

# вычисление объёма занимаемой памяти
from pympler import asizeof
# __sizeof__() метод, позволяющий узнать сколько байтов памяти занимает объект
# getsizeof() вызывает метод объекта __sizeof__ и добавляет размер дополнительной информации,
# которая хранится для сборщика мусора, если он используется
# asizeof в отличие от sys.getsizeof измеряет объекты рекурсивно
a = 3
print(a.__sizeof__(), sys.getsizeof(a), asizeof.asizeof(a))  # 28 28 32

a = range(10)
print(a.__sizeof__(), sys.getsizeof(a), asizeof.asizeof(a))  # 48 48 48

a = (i for i in a)
print(a.__sizeof__(), sys.getsizeof(a), asizeof.asizeof(a))  # 88 104 424

a = tuple(a)
print(a.__sizeof__(), sys.getsizeof(a), asizeof.asizeof(a))  # 104 120 432

a = list(a)
print(a.__sizeof__(), sys.getsizeof(a), asizeof.asizeof(a))  # 120 136 448

a = set(a)
print(a.__sizeof__(), sys.getsizeof(a), asizeof.asizeof(a))  # 712 728 1040

a = dict(zip(a, a))
print(a.__sizeof__(), sys.getsizeof(a), asizeof.asizeof(a))  # 344 360 672

obj = [1, 2, (3, 4), 'text']
print(obj.__sizeof__(), sys.getsizeof(obj), asizeof.asizeof(obj))  # 72 88 328
print(asizeof.asized(obj, detail=2).format())  # [1, 2, (3, 4), 'text'] size=328 flat=88
'''

'''
# СОХРАНЕНИЕ И ЧТЕНИЕ ФАЙЛОВ (БЛОКНОТ)
# 'r' открытие на чтение (является значением по умолчанию)
# 'w' открытие на запись, содержимое файла удаляется; если файла не существует, то создается новый
# 'x' открытие на запись, если файла не существует; если файл существует, выводится ошибка (FileExistsError)
# 'a' открытие на дозапись, информация добавляется в конец файла; если файла не существует, создается новый
# 'b' открытие в двоичном режиме; работа с бинарными файлами (картинки, аудио, видео и т. д.)
# 't' открытие в текстовом режиме (является значением по умолчанию)
# 'r+' открытие на чтение и запись, запись происходит в начало файла, записанные строки заменяют исходные строки в файле

file = open('C:/Users/gurin/Downloads/Python/languages.txt', 'r', encoding='utf-8')
line1 = file.readline()
print(file.tell())  # 8 (курсор смещён вправо на 8 байт)
# По байту на каждый из символов 'P', 'y', 't', 'h', 'o', 'n'
# и два байта на символ перевода строки '\n'.
file.seek(0)  # перевод курсора в начало документа
line2 = file.readline()
print(line1, line2, sep='')
file.close()  # после работы с файлом, его необходимо закрыть, чтобы освободить память от файла

f = open('C:/Users/gurin/Downloads/Python/test.txt', 'w')
for i in range(5):
    f.write(str(i)+'\n')  # запись информации в файл
f.close()

poem = """\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
используй Python!
"""
f = open('C:/Users/gurin/Downloads/Python/poem.txt', 'w')  # открытие файла для записи (writing)
f.write(poem)  # запись текста в файл
f.close()  # закрытие файла
# Если режим не указан, то по умолчанию установлен режим чтения 'r' (reading):
f = open('C:/Users/gurin/Downloads/Python/poem.txt')
while True:
    line = f.readline()  # считываем файл построчно
    if len(line) == 0:  # нулевая длина означает конец файла
        break
    print(line, end='')  # end убирает пустые строки между текстом
f.close()

# Менеджер контекста, контекстный менеджер, contex manager - это объекты,
# которые позволяют управлять контекстом выполнения блока кода.
# Контекст - это то, с чем мы работаем в данный момент.
# Позволяет выделять и освобождать ресурсы строго по необходимости.
# После окончания блока with файл будет закрыт автоматически.
with open('C:\\Users\\gurin\\Downloads\\Python\\pi_digits.txt') as file_object:
    contents = file_object.read(10)  # можно задать количество считываемых символов
    print(contents)  # 3.14159265

# можно использовать '\\', либо r'\\', либо '/' либо r'/', либо r'\' (raw strings - сырые строки)
# list(file_object) аналогично file_object.readlines() (выводит список строк)

with open('C:\\Users\\gurin\\Downloads\\Python\\pi_digits.txt') as file_object:
    print(file_object)
    # <_io.TextIOWrapper name='C:\\Users\\gurin\\Downloads\\Python\\pi_digits.txt' mode='r' encoding='cp1251'>
    for line in file_object:  # аналогично for line in file_object.readlines():
        print(line)
print(file_object.closed)  # True (проверка на то, закрыт файл или нет)

# Примеры работы с несколькими файлами, используя контекстный менеджер:
# Способ 1:
# with A() as a, B() as b:
#     SUITE
# Способ 2:
# with A() as a:
#     with B() as b:
#         SUITE
# Способ 3:
# with (
#     A() as a,
#     B() as b,
#       ):
#     SUITE

with open('C:/Users/gurin/Downloads/Python/test2.txt', 'w') as file:
    file.write('привет!')  # write записывает одну переменную!
with open('C:/Users/gurin/Downloads/Python/test2.txt', 'a') as file:
    file.write('\nДобавим (a - append) пару фраз для теста.')

with open('C:/Users/gurin/Downloads/Python/phi.txt', 'w', encoding='utf-8') as output:
    print('Джoн Локк', 'Дэвид Хьюм', 'Эдмyнд Берк', sep='***', end='!!!', file=output)

philosophers = ['Джoн Локк\n', 'Дэвид Хьюм\n', 'Эдмyнд Берк\n']
with open('C:/Users/gurin/Downloads/Python/philosophers.txt', 'w', encoding='utf-8') as file:
    file.writelines(philosophers)  # запись списка строк

with open('C:/Users/gurin/Downloads/Python/philosophers2.txt', 'w', encoding='utf-8') as file:
    print(philosophers, file=file)  # запись списка строк
'''

'''
# МОДУЛЬ OS
# mkdir() - создает новую папку
# rmdir() - удаляет папку
# rename() - переименовывает файл/папку
# remove() - удаляет файл
# listdir() - список файлов в папке

import os
given_path = 'C:\\Users\\gurin\\Downloads\\Книги'
print(*os.listdir(given_path), sep='\n', end='\n\n')  # вывод всех файлов в папке


def file_obhod(given_path, level=1):  # обход всех файлов в папках с помощью рекурсии
    print(f'level = {level}, content = {os.listdir(given_path)}')
    for i in os.listdir(given_path):
        if os.path.isdir(given_path + '\\' + i):
            print('спускаемся в', given_path + '\\' + i)
            file_obhod(given_path + '\\' + i, level+1)
            print('возвращаемся в', given_path)


file_obhod(given_path)
'''

'''
# МОДУЛЬ JSON
# JSON (JavaScript Object Notation) - текстовый формат обмена данными, основанный на языке программирования JavaScript.
# Парсинг - это автоматизированный сбор и структурирование информации с сайтов при помощи программы или сервиса.
# Сериализация - это процесс сохранения объекта в виде последовательности байт,
# чтобы в будущем по этой последовательности можно было бы восстановить исходный объект.
# Десериализация - это обратный процесс, это «раскодирование» строки 
# определённого формата обратно в питоновский словарь.
import json  # совместим с другими языками программирования в отличие от pickle
# Строковые объекты в формате JSON всегда заключаются в двойные кавычки:
str_json = '{"name": "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB"}'

# Функция loads() в качестве аргумента принимает строку с данными в формате json:
data = json.loads(str_json)  # десериализация
print(data, type(data))  # {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'} <class 'dict'>

# Функция dump() записывает переданный Python объект в файл:
with open(r'C:/Users/gurin/Downloads/Python/countries.json', 'w') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

# Функция dumps() сериализует Python объект в json строку:
new_json = json.dumps(data, indent=2)  # сериализация (все ключи преобразуются в строковый тип данных)
print(new_json, type(new_json))  # <class 'str'>
print(json.dumps(data, indent='---', sort_keys=True, separators=(';', ' = ')))

# Функция load() принимает файловый объект и возвращает его десериализованное содержимое:
with open(r'C:/Users/gurin/Downloads/Python/countries.json') as file:
    countries = json.load(file)  # десериализация
print(countries, type(countries))

# Ключи в JSON-объекте могут быть только строками, заключенными в двойные кавычки.
# В формат JSON нельзя записать словарь, у которого ключи - кортежи.
# С помощью необязательного аргумента skipkeys можно игнорировать подобные ключи:
data = {
        'beegeek': 2018,
        ('Timur', 'Guev'): 29,
        ('Arthur', 'Kharisov'): 20,
        'stepik': 2013,
        'BEEGEEK': ('Arthur', 'Kharisov')
       }
json_data = json.dumps(data, skipkeys=True)  # преобразуем dict в json (кортежи преобразуется в списки)
print(json_data)  # {"beegeek": 2018, "stepik": 2013, "BEEGEEK": ["Arthur", "Kharisov"]}
'''

'''
# МОДУЛЬ PICKLE
import pickle  # бинарная сериализация (сериализация в байты) (работает быстрее, чем json и требует меньше памяти)
# pickle не может сериализовать лямбда-функции и генераторы
data = [1, 2]
pickle_data = pickle.dumps(data)
print(pickle_data, type(pickle_data))  # b'\x80\x04\x95\t\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02e.' <class 'bytes'>
with open(r"C:/Users/gurin/Downloads/Python/pickle_file.json", 'wb') as file:
    pickle.dump(data, file)  # можно сериализовать только в бинарный формат
with open(r"C:/Users/gurin/Downloads/Python/pickle_file.json", 'rb') as file:
    new_data = pickle.load(file)  # десериализуется только бинарный формат
print(new_data)  # [1, 2]
print(pickle.loads(pickle_data))  # [1, 2]
'''

'''
# МОДУЛЬ URLLIB (скачать страницу из интернета)
from urllib.request import urlopen
html = urlopen(r"https://www.python.org/").read().decode('utf-8')
print(html)
'''
'''
# МОДУЛЬ REQUESTS
import requests
resp = requests.get("https://www.python.org/")
print(resp)  # <Response [200]> (код ответа)
print(resp.status_code)  # 200
print(resp.text)  # вывод html-кода
print(resp.url)  # вывод адреса страницы
'''

'''
# МОДУЛЬ CSV (от англ. Comma-Separated Values - значения, разделённые запятыми)
import csv
# метод reader()
with open(r"C:/Users/gurin/Downloads/Python/data.csv", encoding='utf-8') as file:
    data = csv.reader(file)  # csv.reader(file) - итератор, каждая строка которого является списком
    heads = next(data)  # заголовки
    print(heads)
    data = list(data)
    print(data)

# метод writer()
with open(r"C:/Users/gurin/Downloads/Python/domain_usage_list.csv", 'w', encoding='utf-8', newline='') as file:
    wr = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    # quoting=csv.QUOTE_NONNUMERIC - означает заключать все нечисловые поля в кавычки
    wr.writerow(heads)  # запись заголовков
    wr.writerows(data)  # запись строк (либо используя метод writerow() через цикл for)

# метод DictReader()
columns = ['first_name', 'surname', 'email']  # заголовки
with open(r"C:/Users/gurin/Downloads/Python/data.csv", encoding='utf-8') as file:
    data = list(csv.DictReader(file))  # csv.DictReader(file) - итератор, каждая строка которого является словарём
    print(data)

# метод DictWriter()
with open(r"C:/Users/gurin/Downloads/Python/domain_usage_dict.csv", 'w', encoding='utf-8', newline='') as file:
    wr = csv.DictWriter(file, fieldnames=columns, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    wr.writeheader()  # запись заголовков
    for row in data:  # запись строк (либо используя метод writerows())
        wr.writerow(row)
'''

'''
# МОДУЛЬ PANDAS (DATA SCIENCE, АНАЛИЗ ДАННЫХ, МАШИННОЕ ОБУЧЕНИЕ)
import matplotlib.pyplot as plt
import pandas as pd
import phik
import seaborn as sns
import shap
from catboost import CatBoostClassifier, CatBoostRegressor, cv, Pool
from phik import report
from phik.report import plot_correlation_matrix
from sklearn import preprocessing
from sklearn import tree
from sklearn.cluster import KMeans
from sklearn.ensemble import ExtraTreesClassifier, GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LinearRegression, SGDClassifier
from sklearn.metrics import accuracy_score, auc, average_precision_score, classification_report, confusion_matrix, \
    f1_score, log_loss, mean_absolute_error, mean_absolute_percentage_error, precision_recall_fscore_support, \
    precision_score, recall_score, roc_auc_score, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
pd.set_option('display.width', None)  # показывать таблицу во всю ширину экрана
pd.set_option('display.max_columns', None)  # показать все столбцы таблицы
df = pd.read_csv(r"C:/Users/gurin/Downloads/Python/students.csv")  # df - dataframe
df_2 = pd.read_csv(r"C:/Users/gurin/Downloads/Python/aug_train.csv")
df_3 = pd.read_csv(r"C:/Users/gurin/Downloads/Python/uk-used-cars/bmw.csv")
df_4 = pd.read_csv(r"C:/Users/gurin/Downloads/Python/Churn_Modelling.csv")

print(df.columns, end='\n\n')  # список всех столбцов (список фичей)
print(df.info(), end='\n\n')
print(df.describe(), end='\n\n')  # описание всех столбцов таблицы
print(df.head(), end='\n\n')  # первые 5 строк таблицы
print(df.tail(), end='\n\n')  # последние 5 строк таблицы
print(df.dtypes, end='\n\n')  # типы данных столбцов (dtypes = data types)
print(df['Age'].describe(), end='\n\n')  # описание столбца для числовых данных
print(df['Chocolate'].value_counts(), end='\n\n')  # описание столбца для нечисловых (категориальных) данных
print(df['Sex'].value_counts(normalize=True), end='\n\n')  # вывод данных в долях
print(df['Glasses'].value_counts(dropna=False), end='\n\n')  # dropna=False отображает пропуски
print(df['Growth'].mean, end='\n\n')  # происходит автоматическое округление
print(df[['Growth', 'Weight', 'Age']], end='\n\n')  # для выбора нескольких столбцов нужны двойные квадратные скобки
print(df[df['Growth'] < df['Growth'].mean()], end='\n\n')  # выбор людей, у которых рост меньше среднего
df_cut = df[['Age', 'Growth', 'Weight']].copy()  # .copy() нужно, чтобы не было SettingWithCopyWarning
print(df_cut.rename({'Age': 'col1', 'Weight': 'col3'}, axis=1))  # переименование столбцов, не сохраняя названия
print(df_cut.sort_values(by=['Age', 'Growth'], ascending=[True, True]), end='\n\n')  # сортировка по нескольким столбцам
print(df_cut.iloc[0], end='\n\n')  # вывод первой строки
print(df_4.select_dtypes(include='object'))  # выбор категориальных признаков

# визуализация данных
plt.hist(df_3['price'])
plt.grid(True)
plt.show()
print(df_3.groupby('year')['price'].agg(['count', 'mean', 'median']))  # сводная таблица
df_3.groupby('year')['price'].median().plot()
plt.show()
sns.displot(data=df, x='Growth')
sns.displot(data=df, x='Growth', kind='kde')
plt.show()
sns.countplot(data=df, x='Sex', hue='Animal')
plt.show()

# заполнение и удаление незаполненных ячеек
print(df.isna().mean().sort_values(ascending=False), end='\n\n')  # доля незаполненных данных по каждому столбцу
print(df[df['Children number'].isna()])  # просмотр строк, где незаполненны данные
df1 = df.dropna()  # удалить строки, где заполнены не все ячейки
print(df1, end='\n\n')
df2 = df.fillna(0)  # заполнить пустые ячейки нулями
print(df2, end='\n\n')
df3 = df.copy()
df3['Weight'] = df['Weight'].fillna(df['Weight'].mean())  # заполнение пустых ячеек в столбце средними значениями
print(df['Weight'].describe(), end='\n\n')
print(df3['Weight'].describe(), end='\n\n')

# добавление нового столбца
df_cut['Mass index'] = 10000 * df_cut['Weight'] / df_cut['Growth'] ** 2
print(df_cut, end='\n\n')


def new_training_hours(row):
    if row['education_level'] == 'Phd':
        return row['training_hours'] + 1000
    return row['training_hours']


df_2['new_training_hours'] = df_2.apply(new_training_hours, axis=1)
print(df_2[df_2['education_level'] == 'Phd'])

age = df_2[['enrollee_id']].copy()
age['age'] = 30
print(age)
df_2 = df_2.merge(age, how='left', on='enrollee_id', validate='1:1')  # validate, чтобы не было дубликатов
print(df_2)
print(len(df_2))  # проверка на появление дубликатов после join
df_2 = df_2.drop('age', axis=1)

# корреляция
# Метод corr() использовать тогда, когда знаем, что корреляция есть и нужно выяснить между какими признаками сильнее.
print(df_cut.corr(), end='\n\n')  # коэффициент корреляции
sns.heatmap(df_cut.corr())  # зависимость между столбцами присутствует, если значение больше 0.5
plt.show()  # если значение меньше 0, то зависимость обратная

# Для выявления корреляции использовать phik (результат нужно проверить с помощью сводной таблицы):
phik_overview = df_2.phik_matrix()
print(phik_overview)
sns.heatmap(phik_overview)
plt.show()
print(phik_overview['target'].sort_values(ascending=False))  # target - хочет ли уволиться сотрудник

# группировка значений
print(df.groupby('Sex')[['Growth', 'Weight']].mean(), end='\n\n')
group = df.groupby('Sex', dropna=False)['Weight'].agg(['count', 'mean'])  # группировка с добавлением 'count'
print(group)  # сводная таблица
print(group['count'].sum())  # проверка совпадает ли результат (157) с общим количеством строк (186)
print(df.groupby(['Sex', 'Glasses'])[['Growth', 'Weight']].mean(), end='\n\n')  # группировка по нескольким признакам

# Разбиение категории на 5 равных интервалов по значению 'Weight':
df['Weight_group'] = pd.cut(df['Weight'], 5)
weight_group = df.groupby('Weight_group', dropna=False)['Growth'].agg(['count', 'mean'])
print(weight_group)  # сводная таблица
print(weight_group['count'].sum())  # проверка совпадает ли результат (186) с общим количеством строк (186)

# Разбиение категории на 5 равных интервалов по количеству людей (строк):
df['Weight_group_q'] = pd.qcut(df['Weight'], 5, duplicates='drop')
weight_group_q = df.groupby('Weight_group_q', dropna=False)['Growth'].agg(['count', 'mean'])  # группировка
print(weight_group_q)  # сводная таблица ('count' получились неравные из-за наличия одинаковых значений 'Weight')
print(weight_group_q['count'].sum())  # проверка совпадает ли результат (186) с общим количеством строк (186)

# Разбиение категории на произвольное количество интервалов любых значений:
df['Weight_group_custom'] = pd.cut(df['Weight'], [-float('inf'), 50, 75, 90, float('inf')])
weight_group_custom = df.groupby('Weight_group_custom', dropna=False)['Growth'].agg(['count', 'mean'])
print(weight_group_custom)  # сводная таблица
print(weight_group_custom['count'].sum())  # проверка совпадает ли результат (186) с общим количеством строк (186)
df = df.drop(['Weight_group', 'Weight_group_q', 'Weight_group_custom'], axis=1)  # удалить столбцы


# перегруппировка данных (объединение нескольких столбцов в один)
def education_group(x):
    if x in ['High School', 'Primary School']:
        return 'School'
    if x in ['Masters', 'Phd']:
        return 'Masters_and_phd'
    return x


print(df_2.groupby('education_level', dropna=False)['target'].agg(['count', 'mean']))
df_2['new_education_level'] = df_2['education_level'].apply(education_group)
print(df_2.groupby('new_education_level', dropna=False)['target'].agg(['count', 'mean']), end='\n\n')

# игрушечные данные - маленький DataFrame, чтобы проверить на них какую-то функцию или идею
t = pd.DataFrame({'col1': [1, 2, 3, float('nan')],
                  'col2': ['a', 'b', 'c', 'd'],
                  'col3': [0]*3 + [1]*1,
                  'col4': [0, 0, 0, 1]})
print(t)
print(t['col1'].sum(), t['col1'].mean(), t['col1'].count())
'''
'''
# поиск и удаление аномальных данных
# 1-ая процедура поиска выбросов (1-ый способ)
m = df['Weight'].mean()
s = df['Weight'].std()
df = df[(df['Weight'] < m + 3 * s) & (df['Weight'] > m - 3 * s)]
sns.boxplot(x=df['Weight'])  # построение ящика с усами
plt.show()

# 2-ая процедура поиска выбросов (2-ой способ)
a = df['Age'].quantile(0.25)
b = df['Age'].quantile(0.75)
df = df[(df['Age'] < b + 1.5 * (b - a)) & (df['Age'] > a - 1.5 * (b - a))]
sns.boxplot(x=df['Age'])  # построение ящика с усами
plt.show()
'''
'''
# человеческое обучение (задача регрессии)
train, test = train_test_split(df_3, random_state=42)
print(df_3.isna().mean())
phik_overview = df_3.phik_matrix()
print(phik_overview['price'].sort_values(ascending=False))
sns.heatmap(phik_overview)
plt.show()


def engine_group(x):
    if x <= 1.5:
        return '<=1.5'
    if x <= 2:
        return '<=2'
    return '>2'


train['engine_group'] = train['engineSize'].apply(engine_group)  # группировка (способ №1)
train['year_group'] = pd.cut(train['year'], [0, 2010, 2012, 2014, 2016, 2018, float('inf')])  # группировка (способ №2)
model_year_engine_trn_group_median = (train.groupby(['year_group',
                                                     'engine_group',
                                                     'transmission'])['price'].median().reset_index())
model_year_engine_trn_group_median = model_year_engine_trn_group_median.rename(
    {'price': 'price_pred_year_engine_trn_median'}, axis=1)
print(model_year_engine_trn_group_median)
train = train.merge(model_year_engine_trn_group_median, how='left', on=['year_group', 'engine_group', 'transmission'])
print(train)
print(mean_absolute_error(train['price'], train['price_pred_year_engine_trn_median']))
print(mean_absolute_percentage_error(train['price'], train['price_pred_year_engine_trn_median']))

# предсказание на тестовых данных
test['engine_group'] = test['engineSize'].apply(engine_group)
test['year_group'] = pd.cut(test['year'], [0, 2010, 2012, 2014, 2016, 2018, float('inf')])
test = test.merge(model_year_engine_trn_group_median, how='left', on=['year_group', 'engine_group', 'transmission'])
print(test.isna().mean())
print(test[test['price_pred_year_engine_trn_median'].isna()])
test_no_na = test.dropna().copy()
print(mean_absolute_error(test_no_na['price'], test_no_na['price_pred_year_engine_trn_median']))
print(mean_absolute_percentage_error(test_no_na['price'], test_no_na['price_pred_year_engine_trn_median']))
'''
'''
# кластеризация (распределение данных на несколько групп)
df_cut = df[['Weight', 'Growth', 'Sex']]
df_cut = df_cut.dropna()
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(df_cut[['Weight', 'Growth']])
df_cut['Label'] = kmeans.labels_
sns.scatterplot(data=df_cut, x='Weight', y='Growth', hue='Label')  # предположение (распределение на 2 пола)
plt.show()
print(df_cut)
sns.scatterplot(data=df_cut, x='Weight', y='Growth', hue='Sex')  # реальные данные
plt.show()
print(sum((df_cut['Sex'] == 'мужской') & (df_cut['Label'] == 1)) / df_cut.shape[0])  # доля угаданных мужчин
print(sum((df_cut['Sex'] == 'женский') & (df_cut['Label'] == 0)) / df_cut.shape[0])  # доля угаданных женщин
print(sum((df_cut['Sex'] == 'мужской') & (df_cut['Label'] == 0)) / df_cut.shape[0])  # доля не угаданных мужчин
print(sum((df_cut['Sex'] == 'женский') & (df_cut['Label'] == 1)) / df_cut.shape[0])  # доля не угаданных жунщин
'''
'''
# линейная регрессия
# предсказание целевого признака (Growth) по одному нецелевому признаку (Shoe size)
df_cut = df[['Growth', 'Shoe size']]
df_cut = df_cut.dropna()
sns.scatterplot(data=df_cut, x='Shoe size', y='Growth')
plt.show()
linear_regression = LinearRegression()
results = linear_regression.fit(df_cut['Shoe size'].values.reshape(-1, 1), y=df_cut['Growth'].values)
print(results.coef_, results.intercept_)
df_cut['Predicted growth'] = results.predict(df_cut['Shoe size'].values.reshape(-1, 1))
print(df_cut)
print(mean_absolute_error(df_cut['Growth'], df_cut['Predicted growth']))  # погрешность предсказаний
print(mean_absolute_percentage_error(df_cut['Growth'], df_cut['Predicted growth']))  # погрешность предсказаний
'''
'''
# линейная регрессия
# предсказание целевого признака по двум нецелевым признакам: 'Middle and ring finger', 'Middle and little finger'
df_cut = df[['MIddle and index finger', 'Middle and ring finger', 'Middle and little finger']].copy()
linear_regression = LinearRegression()
results = linear_regression.fit(df_cut[['Middle and ring finger', 'Middle and little finger']].values.reshape(-1, 2),
                                y=df_cut['MIddle and index finger'].values)
print(results.intercept_, results.coef_)  # 7.436145518798954 [0.10731496 0.04389948]
df_cut['Predicted'] = results.predict(df_cut[['Middle and ring finger',
                                              'Middle and little finger']].values.reshape(-1, 2))
print(df_cut[['MIddle and index finger', 'Predicted']])
print(mean_absolute_error(df_cut['Predicted'], df_cut['MIddle and index finger']))  # 3.094567105647603
print(mean_absolute_percentage_error(df_cut['Predicted'], df_cut['MIddle and index finger']))  # 0.3192124845366315
'''
'''
# метод k ближайших соседей; предсказание категориального признака (классификация) 
# калибровка
df_cut = df[['Growth', 'Weight', 'Sex']]
df_cut = df_cut.dropna()
sns.scatterplot(data=df_cut, x='Weight', y='Growth', hue='Sex')
plt.show()
scaler = StandardScaler()
scaler.fit(df_cut[['Weight', 'Growth']].values.reshape(-1, 2))
arr = scaler.transform(df_cut[['Weight', 'Growth']].values.reshape(-1, 2))
model = KNeighborsClassifier(n_neighbors=3)
model.fit(arr, y=df_cut['Sex'].values)

# работа с тестовыми данными
df_test = pd.read_csv(r"C:/Users/gurin/Downloads/Python/students_test.csv")
df_test_cut = df_test[['Growth', 'Weight', 'Sex']]
df_test_cut = df_test_cut.dropna()
arr_test = scaler.transform(df_test_cut[['Weight', 'Growth']].values.reshape(-1, 2))
df_test_cut['Predicted'] = model.predict(arr_test)
print(df_test_cut)
print(pd.crosstab(df_test_cut['Predicted'], df_test_cut['Sex']))  # матрица ошибок

# построение наглядной диаграммы, которая показывает ошибочные результаты
df_test_cut['Code'] = '0'
df_test_cut.loc[(df_test_cut['Sex'] == 'мужской') & (df_test_cut['Predicted'] == 'женский'), 'Code'] = '1'
df_test_cut.loc[(df_test_cut['Sex'] == 'женский') & (df_test_cut['Predicted'] == 'мужской'), 'Code'] = '2'
sns.scatterplot(data=df_test_cut, x='Weight', y='Growth', hue='Code')
plt.show()
'''
'''
# линейный классификатор; предсказание категориального признака (классификация)
# калибровка
df_cut = df[['Growth', 'Weight', 'Sex']]
df_cut = df_cut.dropna()
sns.scatterplot(data=df_cut, x='Weight', y='Growth', hue='Sex')
plt.show()
scaler = StandardScaler()
scaler.fit(df_cut[['Weight', 'Growth']].values.reshape(-1, 2))
arr = scaler.transform(df_cut[['Weight', 'Growth']].values.reshape(-1, 2))
model = SGDClassifier()
model.fit(arr, y=df_cut['Sex'].values)

# работа с тестовыми данными
df_test = pd.read_csv(r"C:/Users/gurin/Downloads/Python/students_test.csv")
df_test_cut = df_test[['Growth', 'Weight', 'Sex']]
df_test_cut = df_test_cut.dropna()
arr_test = scaler.transform(df_test_cut[['Weight', 'Growth']].values.reshape(-1, 2))
df_test_cut['Predicted'] = model.predict(arr_test)
print(df_test_cut)
print(pd.crosstab(df_test_cut['Predicted'], df_test_cut['Sex']))  # матрица ошибок

# построение наглядной диаграммы, которая показывает ошибочные результаты
df_test_cut['Code'] = '0'
df_test_cut.loc[(df_test_cut['Sex'] == 'мужской') & (df_test_cut['Predicted'] == 'женский'), 'Code'] = '1'
df_test_cut.loc[(df_test_cut['Sex'] == 'женский') & (df_test_cut['Predicted'] == 'мужской'), 'Code'] = '2'
sns.scatterplot(data=df_test_cut, x='Weight', y='Growth', hue='Code')
plt.show()
'''
'''
# decision tree (дерево решений); предсказание категориального признака
df_cut = df[['Growth', 'Weight', 'Sex', 'Hair length', 'Children number']]
df_cut = df_cut.dropna()
sns.pairplot(df_cut, hue='Sex')
plt.show()
model = tree.DecisionTreeClassifier(max_depth=5)
model.fit(df_cut[['Growth', 'Weight', 'Hair length', 'Children number']].values.reshape(-1, 4),
          y=df_cut['Sex'].values)

# построение блок-схемы
plt.figure(figsize=(20, 10))
tree.plot_tree(model, feature_names=['Growth', 'Weight', 'Hair length', 'Children number'],
               class_names=['мужской', 'женский'], filled=True)
plt.show()

# работа с тестовыми данными
df_test = pd.read_csv(r"C:/Users/gurin/Downloads/Python/students_test.csv")
df_test_cut = df_test[['Growth', 'Weight', 'Sex', 'Hair length', 'Children number']]
df_test_cut = df_test_cut.dropna()
df_test_cut['Predicted'] = model.predict(df_test_cut[['Growth', 'Weight',
                                                      'Hair length', 'Children number']].values.reshape(-1, 4))
print(pd.crosstab(df_test_cut['Predicted'], df_test_cut['Sex']))  # матрица ошибок
# Вычисление величин precision (доля истинных мужчин/женщин, отнесённых ИИ к мужчинам/женщинам) и
# recall (доля правильно предсказанных мужчин/женщин среди всех мужчин/женщин):
print(precision_recall_fscore_support(df_test_cut['Sex'], df_test_cut['Predicted']))

# построение наглядной диаграммы, которая показывает ошибочные результаты
df_test_cut['Code'] = '0'
df_test_cut.loc[(df_test_cut['Sex'] == 'мужской') & (df_test_cut['Predicted'] == 'женский'), 'Code'] = '1'
df_test_cut.loc[(df_test_cut['Sex'] == 'женский') & (df_test_cut['Predicted'] == 'мужской'), 'Code'] = '2'
sns.scatterplot(data=df_test_cut, x='Weight', y='Growth', hue='Code')
plt.show()
'''
'''
# преобразование категориальных признаков в bool
df1 = pd.get_dummies(df, drop_first=True)  # drop_first удаление 1-ой колонки, чтобы избежать избыточности информации
print(df1.info())

# замена категориальных признаков на числовые (оцифровка категориальных признаков)
coder = preprocessing.LabelEncoder()
for name in df.select_dtypes(include=['object']).columns:  # все категориальные признаки
    coder.fit(df[name])
    df[name] = coder.transform(df[name])
df = df.dropna()

# важность признаков для определения пола человека
selector = ExtraTreesClassifier()
result = selector.fit(df[df.columns], df['Sex'])
print(result.feature_importances_)
features_table = pd.DataFrame(result.feature_importances_, index=df.columns, columns=['Importance'])
print(features_table.sort_values(by='Importance', ascending=False))

df_cut = df[['Growth', 'Weight', 'Sex', 'Hair length', 'Children number', 'Coin', 'Animal', 'Army']]
df_cut = df_cut.dropna()
model = tree.DecisionTreeClassifier(max_depth=4)
model.fit(df_cut[['Growth', 'Weight', 'Hair length', 'Children number', 'Coin', 'Animal',
                  'Army']].values.reshape(-1, 7), y=df_cut['Sex'].values)

# построение блок-схемы
plt.figure(figsize=(20, 10))
tree.plot_tree(model, feature_names=['Growth', 'Weight', 'Hair length', 'Children number', 'Coin', 'Animal', 'Army'],
               class_names=['мужской', 'женский'], filled=True)
plt.show()

# работа с тестовыми данными
df_test = pd.read_csv(r"C:/Users/gurin/Downloads/Python/students_test.csv")
df_test_cut = df_test[['Growth', 'Weight', 'Sex', 'Hair length', 'Children number', 'Coin', 'Animal', 'Army']]
df_test_cut = df_test_cut.dropna()

# замена категориальных признаков на числовые
for name in df_test_cut.select_dtypes(include=['object']).columns:  # все категориальные признаки
    coder.fit(df_test_cut[name])
    df_test_cut[name] = coder.transform(df_test_cut[name])
df_test_cut = df_test_cut.dropna()

df_test_cut['Predicted'] = model.predict(df_test_cut[['Growth', 'Weight', 'Hair length', 'Children number',
                                                      'Coin', 'Animal', 'Army']].values.reshape(-1, 7))
print(pd.crosstab(df_test_cut['Predicted'], df_test_cut['Sex']))  # матрица ошибок
'''
'''
# decision tree (дерево решений); задача регрессии (предсказание числового признака)
df_cut = df[['Growth', 'Weight', 'Hair length', 'Shoe size']]
df_cut = df_cut.dropna()
sns.pairplot(df_cut)
plt.show()
model = tree.DecisionTreeRegressor(max_depth=2)
model.fit(df_cut[['Weight', 'Hair length', 'Shoe size']].values.reshape(-1, 3), y=df_cut['Growth'].values)

# построение блок-схемы
plt.figure(figsize=(20, 10))
tree.plot_tree(model, feature_names=['Weight', 'Hair length', 'Shoe size'], class_names=['Growth'], filled=True)
plt.show()

# работа с тестовыми данными
df_test = pd.read_csv(r"C:/Users/gurin/Downloads/Python/students_test.csv")
df_test_cut = df_test[['Growth', 'Weight', 'Hair length', 'Shoe size']]
df_test_cut = df_test_cut.dropna()
df_test_cut['Predicted'] = model.predict(df_test_cut[['Weight', 'Hair length', 'Shoe size']].values.reshape(-1, 3))
print(df_test_cut[['Growth', 'Predicted']])
print(mean_absolute_error(df_test_cut['Growth'], df_test_cut['Predicted']))  # 4.351558902090816
print(mean_absolute_percentage_error(df_test_cut['Growth'], df_test_cut['Predicted']))  # 0.02538521069383894
'''
'''
# ансамбли алгоритмов
df_cut = df[['Growth', 'Weight', 'Sex', 'Hair length', 'Children number']]
df_cut = df_cut.dropna()
sns.pairplot(df_cut, hue='Sex')
plt.show()
model = RandomForestClassifier(max_depth=2, random_state=0)
model.fit((df_cut[['Growth', 'Weight', 'Hair length', 'Children number']].values.reshape(-1, 4)),
          y=df_cut['Sex'].values)

# работа с тестовыми данными
df_test = pd.read_csv(r"C:/Users/gurin/Downloads/Python/students_test.csv")
df_test_cut = df_test[['Growth', 'Weight', 'Sex', 'Hair length', 'Children number']]
df_test_cut = df_test_cut.dropna()
df_test_cut['Predicted'] = model.predict(df_test_cut[['Growth', 'Weight',
                                                      'Hair length', 'Children number']].values.reshape(-1, 4))
print(pd.crosstab(df_test_cut['Predicted'], df_test_cut['Sex']))  # матрица ошибок

# построение наглядной диаграммы, которая показывает ошибочные результаты
df_test_cut['Code'] = '0'
df_test_cut.loc[(df_test_cut['Sex'] == 'мужской') & (df_test_cut['Predicted'] == 'женский'), 'Code'] = '1'
df_test_cut.loc[(df_test_cut['Sex'] == 'женский') & (df_test_cut['Predicted'] == 'мужской'), 'Code'] = '2'
sns.scatterplot(data=df_test_cut, x='Weight', y='Growth', hue='Code')
plt.show()

# вероятности принадлежности к классам
result = model.predict_proba(df_test_cut[['Growth', 'Weight',
                                          'Hair length', 'Children number']].values.reshape(-1, 4))
print(result)
df_test_cut['pr class 0'] = result[:, 0]  # вероятность принадлежности к женщинам
df_test_cut['pr class 1'] = result[:, 1]  # вероятность принадлежности к мужчинам
print(df_test_cut)
print(df_test_cut[(df_test_cut['pr class 1'] < 0.5) & (df_test_cut['Sex'] == 'мужской')])
print(df_test_cut.sort_values(by='pr class 1', ascending=True))
'''
'''
# градиентный бустинг
df_cut = df[['Growth', 'Weight', 'Sex', 'Hair length', 'Children number']]
df_cut = df_cut.dropna()
sns.pairplot(df_cut, hue='Sex')
plt.show()
model = GradientBoostingClassifier(random_state=0)
model.fit((df_cut[['Growth', 'Weight', 'Hair length', 'Children number']].values.reshape(-1, 4)),
          y=df_cut['Sex'].values)

# работа с тестовыми данными
df_test = pd.read_csv(r"C:/Users/gurin/Downloads/Python/students_test.csv")
df_test_cut = df_test[['Growth', 'Weight', 'Sex', 'Hair length', 'Children number']]
df_test_cut = df_test_cut.dropna()
df_test_cut['Predicted'] = model.predict(df_test_cut[['Growth', 'Weight',
                                                      'Hair length', 'Children number']].values.reshape(-1, 4))
print(pd.crosstab(df_test_cut['Predicted'], df_test_cut['Sex']))  # матрица ошибок
print(precision_recall_fscore_support(df_test_cut['Sex'], df_test_cut['Predicted']))

# построение наглядной диаграммы, которая показывает ошибочные результаты
df_test_cut['Code'] = '0'
df_test_cut.loc[(df_test_cut['Sex'] == 'мужской') & (df_test_cut['Predicted'] == 'женский'), 'Code'] = '1'
df_test_cut.loc[(df_test_cut['Sex'] == 'женский') & (df_test_cut['Predicted'] == 'мужской'), 'Code'] = '2'
sns.scatterplot(data=df_test_cut, x='Weight', y='Growth', hue='Code')
plt.show()
'''
'''
# машинное обучение с помощью модуля catboost (задача регрессии)
train, test = train_test_split(df_3, train_size=0.6, random_state=42)  # разбиение данных на 2 выборки
val, test = train_test_split(test, train_size=0.5, random_state=42)  # разбиение на валидационную и тестовую выборки
X = ['model', 'year', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']  # нецелевые признаки
y = ['price']  # целевой признак
cat_features = ['model', 'transmission', 'fuelType']  # категориальные признаки
parameters = {'cat_features': cat_features,
              'learning_rate': 0.08,  # отрегулировать так, чтобы 'bestTest' был ближе к тысячной итерации
              'eval_metric': 'MAPE',  # mean absolute percentage error
              'random_seed': 42,
              'verbose': 100}  # выводить каждую сотую итерацию
model = CatBoostRegressor(**parameters)
model.fit(train[X], train[y], eval_set=(val[X], val[y]))
test['price_pred'] = model.predict(test[X])
print(model.best_iteration_)
print(mean_absolute_error(test['price'], test['price_pred']))
print(mean_absolute_percentage_error(test['price'], test['price_pred']))

# обучение на всех данных (объединение train и val)
train_full = pd.concat([train, val])
parameters = {'iterations': model.best_iteration_ + 1,
              'cat_features': cat_features,
              'eval_metric': 'MAPE',
              'learning_rate': 0.08,
              'random_seed': 42,
              'verbose': 100}
model = CatBoostRegressor(**parameters)
model.fit(train_full[X], train_full[y])
test['price_pred_all'] = model.predict(test[X])
print(mean_absolute_error(test['price'], test['price_pred_all']))
print(mean_absolute_percentage_error(test['price'], test['price_pred_all']))

# анализ ошибок
test['error'] = test['price_pred'] - test['price']
plt.hist(test['error'])
plt.grid(True)
plt.show()
test['error_abs'] = abs(test['error'])  # абсолютная ошибка
plt.hist(test['error_abs'])
plt.grid(True)
plt.show()
print(test['error_abs'].describe(), end='\n\n')
print(test.sort_values('error_abs', ascending=False))  # сортировка по самым большим ошибкам


# анализ абсолютной ошибки
def print_error(col):
    t = test.groupby(col)[['error_abs', 'error']].agg(['count', 'mean'])
    t.columns = ['_'.join(col).strip() for col in t.columns.values]  # убрать мультииндекс названий столбцов
    t = t.drop('error_count', axis=1)  # удалить повторяющийся столбец
    t['mean_error_diff'] = t['error_abs_mean'] - test['error_abs'].mean()
    t['mean_error'] = test['error_abs'].mean()  # добавление столбца со средней ошибкой
    print(t, end='\n\n')


test['price_group'] = pd.qcut(test['price'], 5)
print_error('price_group')
print_error('year')
print(test, end='\n\n')
print(model.get_feature_importance(prettified=True))  # оценка важности параметров

# модуль shap
shap.initjs()
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(test[X])
print(train['price'].mean())
# Насколько сильно каждый параметр смещает цену (price_pred равна сумме каждой фичи и средней цены):
print(pd.DataFrame(shap_values, columns=X))
shap.force_plot(explainer.expected_value, shap_values[0, :], test[X].iloc[0, :], matplotlib=True, show=True)

# создание общей таблицы на основе shap и test
shap_cols = [x + '_shap' for x in X]
shap_values_df = pd.DataFrame(shap_values, columns=shap_cols)
test_shap = pd.concat([test.reset_index(), shap_values_df], axis=1)
test_shap = test_shap.sort_values('error_abs', ascending=False)
print(test_shap)
shap.force_plot(explainer.expected_value, test_shap[shap_cols].values[0, :],
                test_shap[X].iloc[0, :], matplotlib=True, show=True)
plot = shap.force_plot(explainer.expected_value, test_shap[shap_cols].head(10).values,
                       test_shap[X].head(10), show=False)
shap.save_html(r"C:/Users/gurin/Downloads/Python/uk-used-cars/index.htm", plot)
plot_2 = shap.force_plot(explainer.expected_value, test_shap[shap_cols].values, test_shap[X], show=False)
shap.save_html(r"C:/Users/gurin/Downloads/Python/uk-used-cars/index_2.htm", plot_2)
shap.dependence_plot("year", shap_values, test[X], show=True, interaction_index='model')
shap.summary_plot(shap_values, test[X], show=True)  # серым подсвечены категориальные признаки
'''
'''
# машинное обучение с помощью модуля catboost (задача классификации (уйдёт ли клиент из компании))
# В задачах классификации нужно указывать параметр stratify, чтобы была равная доля по целевому признаку (Exited):
train, test = train_test_split(df_4, train_size=0.6, random_state=42, stratify=df_4['Exited'])
val, test = train_test_split(test, train_size=0.5, random_state=42, stratify=test['Exited'])
train_full = pd.concat([train, val])
phik_overview = train_full.drop('Surname', axis=1).phik_matrix()
print(phik_overview['Exited'].sort_values(ascending=False))
X = ['CustomerId', 'CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance',
     'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']
cat_features = ['Geography', 'Gender']
y = ['Exited']
train_data = Pool(data=train[X],
                  label=train[y],
                  cat_features=cat_features)
valid_data = Pool(data=val[X],
                  label=val[y],
                  cat_features=cat_features)
test_data = Pool(data=test[X],
                 label=test[y],
                 cat_features=cat_features)
params = {'verbose': 100,
          'random_seed': 42,
          'learning_rate': 0.01}
model = CatBoostClassifier(**params)
model.fit(train_data, eval_set=valid_data)
# Добавление в таблицу score (score - оценка склонности оттока людей из компании):
test['score_catboost'] = model.predict_proba(test[X])[:, 1]  # в некоторых случаях score равен
print(test['score_catboost'].nunique(), len(test))  # вероятности, но так происходит не всегда


def uplift(df, score, pct):
    exited_all = df['Exited'].sum()
    df = df.sort_values(score, ascending=False)
    exited_found = df.head(round(len(df) * pct))['Exited'].sum()
    return (exited_found / exited_all) / pct


def print_metrics(df, score):
    print(log_loss(df['Exited'], df[score]))
    print(uplift(df, score, 0.2))


print_metrics(test, 'score_catboost')
print(model.get_feature_importance(prettified=True))

# модуль shap
shap.initjs()
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(test[X])
shap.summary_plot(shap_values, test[X], show=True)  # серым подсвечены категориальные признаки
shap.dependence_plot("NumOfProducts", shap_values, test[X], show=True, interaction_index='Age')
test['y_pred'] = (test['score_catboost'] > 0.5) * 1  # 0.5 - порог (threshold), можно установить другое значение
print(test)

# метрики классификации
print(confusion_matrix(test['Exited'], test['y_pred']))  # матрица ошибок
# Составляющие матрицы ошибок (confusion matrix):
# true negative - истинно-отрицательный
# false positive - ложно-положительный, ошибка I рода (ложное срабатывание)
# false negative - ложно-отрицательный, ошибка II рода (ложный пропуск)
# true positive - истинно-положительный
tn, fp, fn, tp = confusion_matrix(test['Exited'], test['y_pred']).ravel()
recall = tp / (tp + fn)  # полнота (TPR - true positive rate, sensitivity)
print(recall)  # 0.4643734643734644
print(recall_score(test['Exited'], test['y_pred']))  # 0.4643734643734644
precision = tp / (tp + fp)  # точность
print(precision)  # 0.7714285714285715
print(precision_score(test['Exited'], test['y_pred']))  # 0.7714285714285715
f1 = (2 * recall * precision) / (recall + precision)
print(f1)  # 0.5797546012269938
print(f1_score(test['Exited'], test['y_pred']))  # 0.5797546012269938
print((test['Exited'] == test['y_pred']).mean())  # accuracy
print((tp + tn) / (tp + tn + fp + fn))  # accuracy (аналогично предыдущему)
print(accuracy_score(test['Exited'], test['y_pred']))  # accuracy (аналогично предыдущему)
print(classification_report(test['Exited'], test['y_pred']))

# предикт с другим порогом (общее количество порогов равно количеству уникальных значений скоров плюс 1)
thrs = [0] + list(test['score_catboost'].unique())  # thresholds
result = []
for thr in thrs:
    test['y_pred_new'] = (test['score_catboost'] > thr) * 1
    result.append((thr, f1_score(test['Exited'], test['y_pred_new'])))
t = pd.DataFrame(result, columns=['thr', 'f1'])
print(t.sort_values('f1', ascending=False))
t.plot(x='thr', y='f1', style='o', grid=True)
plt.show()

# ROC - receiver operating characteristic, рабочая характеристика приёмника, кривая зависимости TPR от FPR
fprs, tprs, thrs = roc_curve(test['Exited'], test['score_catboost'])
roc = pd.DataFrame({'fpr': fprs, 'tpr': tprs, 'thr': thrs})
print(roc)
roc['random'] = roc['fpr']
roc['ideal'] = 1
roc.plot(x='fpr', y=['tpr', 'random', 'ideal'], figsize=(6, 6), grid=True)
plt.show()

# 2-ой способ построения ROC-curve:
fpr, tpr, threshold = roc_curve(test['Exited'], test['score_catboost'])
roc_auc = auc(fpr, tpr)
plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label='AUC = %0.2f' % roc_auc)
plt.legend(loc='lower right')
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

# AUC - area under curve, площадь под кривой
print(roc_auc_score(test['Exited'], test['score_catboost']))
print(average_precision_score(test['Exited'], test['score_catboost']))

# кросс-валидация
train_full_data = Pool(train_full[X],
                       label=train_full[y],
                       cat_features=cat_features)
params = {'verbose': 100,
          'eval_metric': 'AUC',
          'loss_function': 'Logloss',
          'random_seed': 42,
          'learning_rate': 0.01}
cv_data = cv(
    params=params,
    pool=train_full_data,
    fold_count=5,
    shuffle=True,
    partition_random_seed=0,
    stratified=False,
    verbose=False
)
print(cv_data)
print(cv_data[cv_data['test-AUC-mean'] == cv_data['test-AUC-mean'].max()])
n_iters = cv_data[cv_data['test-AUC-mean'] == cv_data['test-AUC-mean'].max()]['iterations'].values[0]
print(n_iters)  # выводит лучшую итерацию по кросс-валидации

# повторное обучения с лучшей итерацией
params = {'iterations': n_iters,
          'verbose': 100,
          'eval_metric': 'AUC',
          'loss_function': 'Logloss',
          'random_seed': 42,
          'learning_rate': 0.01}
model = CatBoostClassifier(**params)
model.fit(train_full_data)
test['y_score_cross_val'] = model.predict_proba(test_data)[:, 1]
print(roc_auc_score(test['Exited'], test['y_score_cross_val']))
'''

"""
# SQL-ЗАПРОСЫ
import sqlite3
import pandas as pd
pd.set_option('display.width', None)
df = pd.read_csv(r"C:\\Users\\gurin\\Downloads\\Python\\german_credit_augmented.csv")
# Всегда нужно менять строковый тип данных на объект типа "дата":
df['contract_dt'] = pd.to_datetime(df['contract_dt'], format='%Y-%m-%d %H:%M:%S')
con = sqlite3.connect('db')  # подключение к базе данных (connection)
print(df)
df.to_sql('german_credit', con, index=False, if_exists='replace')


def select(sql):
    print(pd.read_sql(sql, con), end='\n\n')


sql = '''
SELECT t.age * 3 AS age_mult_3, t.housing  -- обозначение комментария в SQL
FROM german_credit AS t  -- правилом хорошего тона является указание alias'а таблицы
LIMIT 5'''
select(sql)

sql = '''
SELECT t.* FROM german_credit AS t  -- всегда указывать таблицу, поля которой извлекаются, т. к. явное лучше неявного
WHERE t.contract_dt BETWEEN '2007-01-01' AND '2007-12-31'  -- Сам день 2007-12-31 в выборку не попадет, т.к. BETWEEN
      AND t.purpose IN ('car', 'repairs')                  -- включает все до 00:00 верхней границы,
ORDER BY t.contract_dt                                     -- поэтому лучше писать до '2008-01-01'.
'''
select(sql)

# сохранение результата запроса в отдельную таблицу
cur = con.cursor()
sql = '''
DROP TABLE IF EXISTS greater_1000_credit;
CREATE TABLE greater_1000_credit AS
SELECT * FROM german_credit AS t
WHERE t.credit_amount > 1000'''
print(cur.executescript(sql))  # <sqlite3.Cursor object at 0x000002A4635ABF40>
sql = '''SELECT * FROM greater_1000_credit AS t'''
select(sql)

# UNION
jan = pd.DataFrame({'month': ['jan', 'jan'], 'revenue': [1, 2]})
feb = pd.DataFrame({'month': ['feb', 'feb'], 'revenue': [1, 2]})
jan.to_sql('jan', con, index=False, if_exists='replace')
feb.to_sql('feb', con, index=False, if_exists='replace')
sql = '''
SELECT * FROM jan AS t
UNION ALL
SELECT * FROM feb AS t'''
select(sql)

sql = '''
SELECT t.revenue FROM jan AS t
UNION  -- UNION в отличие от UNION ALL удаляет дубликаты
SELECT t.revenue FROM feb AS t'''
select(sql)

# GROUP BY
sql = '''
SELECT t.sex,
       Count(*) AS cnt,
       Avg(t.credit_amount) AS credit_amount_avg
FROM german_credit AS t
GROUP BY t.sex'''
select(sql)

sql = '''
SELECT DISTINCT t.age
FROM german_credit AS t
ORDER BY t.age DESC
LIMIT 10'''
select(sql)

# нахождение дубликатов
t = pd.DataFrame({'id': [1, 1, 2, 2, 3],
                  'name': ['a', 'b', 'c', 'd', 'e']})
t.to_sql('dupl_test', con, index=False, if_exists='replace')
print(t)

sql = '''SELECT * FROM dupl_test AS t'''
select(sql)

sql = '''
SELECT *
FROM   dupl_test AS t
WHERE  t.id IN (SELECT t.id
                FROM   dupl_test AS t
                GROUP  BY t.id
                HAVING Count(1) > 1)'''  # Count(1) аналогично Count(*)
select(sql)

# разделение данных на интервалы
sql = '''
SELECT CASE
         WHEN t.credit_amount < 1000 THEN '<1000'
         WHEN t.credit_amount < 2000 THEN '1000-2000'
         WHEN t.credit_amount < 3000 THEN '2000-3000'
         WHEN t.credit_amount >= 3000 THEN '>= 3000'
         ELSE 'other'
       END AS credit_amount_bin,
       Count(1) AS credit_cnt
FROM   german_credit AS t
GROUP  BY 1'''
select(sql)

# CTE (Common Table Expressions)
sql = '''
WITH id_cnt
     AS (SELECT t.id,
                Count(1) AS cnt
         FROM   dupl_test AS t
         GROUP BY t.id),
     id_cnt_2
     AS (SELECT *
         FROM   id_cnt AS t
         WHERE  t.cnt > 1)
SELECT *
FROM   id_cnt_2 AS t
WHERE  t.id = 1'''
select(sql)

# JOIN
users = pd.DataFrame({'id': [1, 2, 3], 'name': ['gleb', 'john snow', 'tyrion']})
items = pd.DataFrame({'user_id': [1, 3, 3], 'item_name': ['hleb', 'gold', 'wine'], 'value': [5, 100, 20]})
users.to_sql('users', con, index=False, if_exists='replace')
items.to_sql('items', con, index=False, if_exists='replace')
sql = '''
SELECT u.*,
       i.item_name,
       i.value,
       i.user_id
FROM   users AS u
       LEFT JOIN items AS i
              ON u.id = i.user_id'''  # всегда прописывать alias таблиц в условии join, чтобы избежать ошибок и путаницы
select(sql)

# CROSS JOIN
sql = '''
WITH users
     AS (SELECT 1 AS user_id
         UNION ALL
         SELECT 2 AS user_id
         UNION ALL
         SELECT 3 AS user_id),
     month
     AS (SELECT Date('2021-03-01') AS month
         UNION ALL
         SELECT Date('2021-04-01') AS month)
SELECT *
FROM   users AS t
       INNER JOIN month AS m
         ON 1 = 1'''  # INNER JOIN ON 1 = 1 аналогично CROSS JOIN
select(sql)

# JOIN таблицы саму на себя
t = pd.DataFrame({'dt': pd.to_datetime(['2021-04-01', '2021-04-02', '2021-04-03'], format='%Y-%m-%d'),
                  'revenue': [1, 2, 3]})
t.to_sql('revenue', con, index=False, if_exists='replace')
# подсчёт кумулятивной выручки (1-ый способ)
sql = '''select
t.dt,t.revenue, sum(r.revenue) as cumsum from revenue t
join revenue r on r.dt <= t.dt
group by t.dt, t.revenue'''
select(sql)

# подзапросы
transactions = pd.read_csv(r"C:/Users/gurin/Downloads/Python/german_credit_augmented_transactions.csv")
transactions.to_sql('client_transactions', con, index=False, if_exists='replace')
min_date = '''SELECT date(min(t.dt),'start of month') FROM client_transactions AS t'''
max_date = '''SELECT date(max(t.dt),'start of month') FROM client_transactions AS t'''
# Нельзя просто выполнить группировку по датам, т. к. за сентябрь отсутствуют транзакции, сначала нужно
# сгенерировать всевозможные даты, затем выполнить LEFT JOIN к этим датам:
sql = f'''
WITH RECURSIVE dates(month) AS  -- dates - название таблицы, month - название столбца
    (VALUES(({min_date}))
    UNION ALL
    SELECT date(month, '+1 month')
    FROM dates
    WHERE month < ({max_date})),
trans_month AS
    (SELECT date(t.dt, 'start of month') AS month,
    count(1) AS transaction_cnt,
    SUM(t.amount) as amount_sum
    FROM client_transactions AS t
    GROUP BY 1
    ORDER BY 1)
SELECT t.month,
       coalesce(tm.transaction_cnt, 0) AS transaction_cnt,
       coalesce(tm.amount_sum, 0) AS amount_sum
FROM dates AS t
LEFT JOIN trans_month tm ON t.month = tm.month
ORDER BY t.month'''
select(sql)

# оконные функции
# подсчёт кумулятивной выручки (2-ой способ)
sql = '''
SELECT t.*,
       SUM(t.revenue) OVER (ORDER BY t.dt) AS cum_sum
FROM   revenue AS t'''
select(sql)

t = pd.DataFrame({'dep': ['a', 'a', 'a', 'a', 'a',
                         'b', 'b', 'b', 'b', 'b'],
                  'emp': ['aa', 'ab', 'ac', 'ad', 'ae',
                         'ba', 'bb', 'bc', 'bd', 'be'],
                  'sal': [5, 5, 3, 2, 1,
                         5, 4, 3, 2, 1]})
t.to_sql('salary', con, index=False, if_exists='replace')
sql = '''
SELECT t.*,
       RANK()
         OVER (
           PARTITION BY t.dep
           ORDER BY t.sal DESC) AS rnk,
       Dense_rank()
         OVER (
           partition BY t.dep
           ORDER BY t.sal DESC) AS d_rnk
FROM salary AS t'''
select(sql)
"""

'''
# ВИЗУАЛИЗАЦИЯ ДАННЫХ
# МОДУЛЬ MATPLOTLIB
import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]  # значения по x
squares = [1, 4, 9, 16, 25]  # значения по y
plt.grid(lw=1, ls='-')  # добавление сетки на график (lw - linewidth)
plt.plot(input_values, squares, linewidth=5, color='red')
plt.plot(input_values, squares, lw=12, color='black', zorder=0)  # zorder=0 - поместить график на задний план
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)  # размер шрифта делений на осях
plt.scatter(2, 10, s=200)  # нанести точку на график (s - толщина точки)
plt.annotate('A', (2, 11), fontsize=20)  # нанести надпись на график
plt.show()
'''
'''
x_values = list(range(1, 1001, 50))
y_values = [x ** 2 for x in x_values]
plt.scatter(x_values, y_values, edgecolors='red', s=40)  # edgecolors - цвет контура точек
plt.axis([0, 1100, 0, 1100000])  # назначение диапазона для каждой оси
plt.show()
'''
'''
x_values = list(range(-1000, 1001))
y_values = [x**2 for x in x_values]
# Меньшие значения y_values светлее, большие значения - темнее (можно сделать с=x_values):
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=40)  # cmap - цветовая карта
# path = 'C:\\Users\\gurin\\Downloads\\Python\\picture.png'
# plt.savefig(path, bbox_inches='tight') # 2-ой аргумент отсекает лишние пропуски
plt.show()
'''
'''
x = list(range(-100, 101))
y_1 = [i ** 3 for i in x]
y_2 = [i * 10000 for i in x]
plt.plot(x, y_1, c='red', label='y = x ** 3')
plt.plot(x, y_2, c='blue', label='y = 10000x')
# Закраска области между графиками:
plt.fill_between(x, y_1, y_2, facecolor='aqua', alpha=0.1)  # alpha - степень прозрачности
plt.legend(loc=2)  # loc - местоположение легенды
plt.show()
'''
'''
# построение гистограммы
import numpy as np
y = np.random.standard_cauchy(size=10**7)
plt.hist(y, range=(0, 5), bins=50, density=True)
plt.show()
'''
'''
# построение круговых графиков
import numpy as np
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
print(r)
print(theta)
plt.figure(figsize=(6, 6))
plt.axes(projection='polar')
plt.scatter(theta, r, s=400*r**2, c=theta, cmap='hsv', alpha=0.8)
plt.show()
'''
'''
# построение круговых диаграмм
counts = [15, 8, 4]
plt.figure(figsize=(5, 5))
plt.pie(counts,
        colors=['royalblue', 'gold', 'green'],  # цвета долей
        labels=['dogs', 'cats', 'humsters'],  # подписи
        startangle=120,  # начальный угол
        autopct='%.2f%%',  # формат вывода значений долей
        explode=(0, 0.2, 0.2))  # вынос частей
plt.show()
'''
'''
# построение графика с погрешностями
import numpy as np
x = np.linspace(-5, 5, 40)
y = np.sin(x) + np.tanh(2 * (x - 2))
yerr = (2 * np.random.sample(size=y.size))
plt.figure(figsize=(10, 5))
plt.errorbar(x, y,
             yerr=yerr,
             ecolor='forestgreen',
             capsize=10,  # ширина планки погрешностей
             elinewidth=1.5)
plt.show()
'''
'''
# построение плотностных графиков
import numpy as np
def func(x, y):
    return (x - 1)**2 - (y + 2)**2


x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)
x, y = np.meshgrid(x, y)
z = func(x, y)
fig, ax = plt.subplots(1, 1, figsize=(6, 5))
obj = ax.imshow(z, cmap=plt.cm.seismic, vmin=-400, vmax=400)
fig.colorbar(obj)
plt.show()


def func2(x, y):
    r = x ** 2 + y ** 2
    return -np.sqrt(r)


u = func2(x, y)
fig, ax = plt.subplots(1, 1, figsize=(6, 5))
mapp = ax.pcolormesh(x, y, u, cmap='inferno', shading='auto', edgecolor='face')
fig.colorbar(mapp)
plt.show()
'''
'''
# построение 3D графиков
import numpy as np
def func3(x, y):
    return x ** 4 - y ** 4


x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)
x, y = np.meshgrid(x, y)
z = func3(x, y)
fig, ax = plt.subplots(1, 1, figsize=(6, 6), subplot_kw={'projection': '3d'})
ax.plot_surface(x, y, z / z.max(), cmap=plt.cm.ocean_r)
ax.view_init(30, 60)  # угол просмотра
plt.show()
'''
'''
from random import choice
class RandomWalk():
    """Класс для генерирования случайных блужданий."""
    def __init__(self, num_points=500):
        """Инициализирует атрибуты блуждания."""
        self.num_points = num_points
        # все блуждания начинаются с точки (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Вычисляет все точки блуждания."""
        # Шаги генерируются до достижения нужной длины:
        while len(self.x_values) < self.num_points:
            # Определение направления и длины перемещения:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            # Обработка нулевых перемещений:
            if x_step == 0 and y_step == 0:
                continue
            # Вычисление следующих значений x и y:
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)


rw = RandomWalk(5000)
rw.fill_walk()
point_numbers = list(range(rw.num_points))
print(list(zip(rw.x_values, rw.y_values)))  # координаты x и y
plt.figure(dpi=100, figsize=(10, 6))  # назначение размера области просмотра
# с увеличением порядковго номера point_numbers изменяется цвет точки
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap='jet', s=15)
plt.colorbar(label='Color Intensity')
#plt.plot(rw.x_values, rw.y_values, linewidth=1)
plt.scatter(0, 0, c='green', s=100)  # выделение первой точки
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)  # выделение последней точки
plt.show()
'''

'''
# ЧЕРЕПАШЬЯ ГРАФИКА
import turtle
from random import randrange
# В Python 3 для того, чтобы использовать цвет в формате RGB,
# нужно предварительно установить значение colormode в 255:
turtle.Screen().colormode(255)


def turtle_1():
    turtle.forward(100)
    turtle.right(90)  # поворот по часовой стрелки
    turtle.backward(250)
    turtle.shapesize(4)  # размер черепашки
    turtle.shape('turtle')  # стрелка меняется на черепашку
    turtle.left(120)  # поворот против часовой стрелки
    turtle.forward(100)
    turtle.setheading(230)  # задать угловое направление (поворот против часовой стрелки)
    turtle.forward(100)
    print(turtle.heading())  # 230.0 (узнать текущее направление против часовой стрелки)
    turtle.penup()  # поднимает перо (не оставляет за собой след)
    turtle.forward(200)
    turtle.pendown()
    turtle.pencolor('cyan')
    turtle.dot(10, 'blue')  # нарисовать точку (можно задать размер и цвет)
    turtle.forward(200)
    turtle.stamp()  # оставить штамп внешнего вида курсора (например, черепашки)
    turtle.circle(80)
    turtle.clear()
    turtle.forward(100)


# turtle_1()


def turtle_2():
    turtle.Screen().setup(1200, 700)  # размер графического окна, ширина и высота (в пикселях)
    turtle.pensize(5)  # изменение размера пера
    color = (13, 56, 240)  # кортеж (r, g, b)
    turtle.pencolor(color)  # цвет пера, кортеж в качестве аргумента
    # если использовать turtle.color(), то и черепашка и цвет пера станет заданным цветом
    # turtle.color(): turtle.pencolor() и turtle.fillcolor()
    turtle.fillcolor('red')  # выбрать цвет заполнения фигуры (чёрный цвет по умолчанию)
    turtle.begin_fill()  # включаем заливку
    turtle.circle(80)
    turtle.end_fill()  # выключаем заливку

    turtle.pencolor(130, 240, 200)  # значения r, g, b в качестве аргументов
    turtle.circle(50, steps=5)  # steps - количество углов
    turtle.Screen().bgcolor('black')  # установка цвета фона
    turtle.pencolor('green')
    turtle.circle(100, extent=150)  # extent - угол, который пройдёт черепашка
    print(turtle.heading())  # 150.0 (после extent направление черепашки остаётся по касательной круга)
    turtle.back(500)
    turtle.clearscreen()
    turtle.forward(400)


# turtle_2()

# turtle.clear() стирает все рисунки в графическом окне, но не меняет положение черепашки,
# цвета пера и цвета фона графического окна (если несколько черепашек, то стирает за указанной)
# turtle.clearscreen() стирает все рисунки в графическом окне, меняет цвет пера на черный,
# а цвет фона на белый, и возвращает черепашку в исходное положение в центр графического окна

def turtle_3():
    turtle.hideturtle()  # скрывает черепашку
    turtle.speed(1)  # число от 0 до 10
    # 0 - отключает анимацию (всё происходит мгновенно), 1 - самая медленная, 10 - самая быстрая
    turtle.goto(100, 150)  # перемещает черепашку в указанные координаты, либо turtle.setpos()
    position = turtle.pos()
    print(position, type(position))  # (100.00,150.00) <class 'turtle.Vec2D'>
    turtle.showturtle()  # показывает черепашку
    turtle.setx(-300)  # устанавливает координату x, у не меняется
    turtle.sety(-300)  # устанавливает координату у, х не меняется


# turtle_3()


def turtle_4():
    turtle.speed(1)
    turtle.hideturtle()
    turtle.goto(-120, 120)
    turtle.write('Сверху', move=True, align='center', font=('Arial', 17, 'bold'))
    turtle.goto(50, -120)  # move (будет ли двигаться черепашка по мере рисования текста)
    turtle.write('Снизу', move=False, align='left', font=('Times New Roman', 25, 'normal'))
    turtle.goto(100, 20)  # align может быть: right, center, left
    turtle.write('Справа', move=True, align='right', font=('Helvetica', 20, 'italic'))


# turtle_4()
'''
'''
def move_turtles(turtles, dist, angle):
    for turtle in turtles:    # все черепашки из списка делают одни и те же действия
        turtle.forward(dist)
        turtle.right(angle)


turtles = []                   # список черепашек
head = 0
num_turtles = 10               # количество черепашек
for i in range(num_turtles):
    turt = turtle.Turtle()     # создаем черепашку и устанавливаем ее свойства
    turt.setheading(head)
    turt.pensize(2)
    turt.color(randrange(256), randrange(256), randrange(256))
    turt.speed(1)
    turt._tracer(2, 1000)  # выполняется каждое n-е обновление экрана; задержка обновления холста
    turtles.append(turt)       # добавляем черепашку в список
    head = head + 360/num_turtles
for i in range(70):
    move_turtles(turtles, 20, i)
'''
'''
def move_up():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x, y + 5)


def move_down():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x, y - 5)


def move_left():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x - 5, y)


def move_right():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x + 5, y)


turtle.showturtle()  # отображаем черепашку
turtle.pensize(3)  # устанавливаем размер пера
turtle.shape('turtle')
turtle.Screen().listen()  # устанавливаем фокус на экран черепашки
turtle.Screen().onkey(move_up, 'Up')  # регистрируем функцию на нажатие клавиши наверх
turtle.Screen().onkey(move_down, 'Down')  # регистрируем функцию на нажатие клавиши вниз
turtle.Screen().onkey(move_left, 'Left')  # регистрируем функцию на нажатие клавиши налево
turtle.Screen().onkey(move_right, 'Right')  # регистрируем функцию на нажатие клавиши направо
turtle.done()  # предотвращает закрытие холста, аналогично turtle.mainloop()
'''
'''
turtle.speed(0)
def random_color():
    return randrange(256), randrange(256), randrange(256)


def draw_circle(x, y, r):
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    color = random_color()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def left_mouse_click(x, y):  # Вспомогательная функция, чтобы задать радиус, т. к. в функцию
    draw_circle(x, y, 10)    # onclick подаётся функция с двумя аргументами х и у.


turtle.hideturtle()
turtle.Screen().onclick(left_mouse_click)  # аргументы функции "left_mouse_click" не пишутся
turtle.Screen().listen()
turtle.mainloop()
'''
'''
turtle.Screen().bgcolor('blue')
moon = turtle.Turtle()
moon.hideturtle()
moon.dot(200, 'orange')
clouds = {0: turtle.Turtle(), 1: turtle.Turtle()}
for cloud in clouds:
    clouds[cloud].hideturtle()
    # clouds[cloud]._tracer(2, 50)
    clouds[cloud].pencolor('blue')
    clouds[cloud].penup()
while 1:
    for i in range(200, -201, -1):
        clouds[i % 2].goto(i, 0)
        clouds[i % 2].dot(200)
        clouds[(i + 1) % 2].clear()
'''
