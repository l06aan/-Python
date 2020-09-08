# Задание-1:
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль

def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y is'n be a zero"
    except ValueError:
        return "enter only number"
print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))

# Задание-2:
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def my_func(name, surname, byear, city, email, phone):
    print(fname, surname, byear, city, email, phone)

my_func(name= 'anna', surname='agf', byear=1992, city='Spb', email='email', phone='0232')

# Задание-3:
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    sequence = [x, y, z]
    total = []
    max_1 = max(sequence)
    total.append(max_1)
    sequence.remove(max_1)
    max_2 = max(sequence)
    total.append(max_2)
    print(sum(total))
my_func(-4, 2, 0)

#Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень'''

def my_func(x, y):
    return 1 / x ** abs(y)
    #return x ** y
print(my_func(2, -3))

#Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

import sys

result = 0
while True:
    line = input("Enter number or special token q fo exite: ")
    tokens = line.split(" ")
    for token in tokens:
        try:
            number = float(token)
            result += number
        except:
            if token == 'q':
                print(f"You sum is {result}. Program is terminated")
                exit(0)
            else:
                print(f"You sum is {result}. Input error", file=sys.stderr)
                exit(1)
#print(result)
#exit()
