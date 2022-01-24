#! /usr/bin/env python3
# -*- coding: utf-8 -*_

'''функции как объекты первого класса'''


def hello_world():
    print('Hello, world!')

#2 определение функции внутри других функций
def wrapper_function():
    def hello_world1():
        print('Hello000000 world!')
    hello_world1()

#3 передача функции в качестве аргументов и возвращение их из других функций
def higher_order(func):
    print('Получена функция {} в качестве аргумента'.format(func))
    func()
    return func


if __name__ == '__main__':
    hello_world()
    #1 хранение функции в переменных
    h = hello_world
    h()
    #2
    wrapper_function()
    #3
    higher_order(hello_world)
