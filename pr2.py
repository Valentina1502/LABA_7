#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Рассмотрим пример работы декоратора"""


def decorator_function(func):
    def wrapper():
        print('функция обертка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обернутую функцию...')
        func()
        print('Выходим из обертки')
    return wrapper


@decorator_function
def hello_world():
    print('hello, world')


if __name__ == '__main__':
    hello_world()