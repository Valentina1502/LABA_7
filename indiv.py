#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Объявите функцию с именем get_sq , которая вычисляет площадь
прямоугольника по двум параметрам: width и height – ширина и высота
прямоугольника и возвращает результат.
Определите декоратор для этой функции с именем (внешней функции)
func_show , который отображает результат на экране в виде строки
(без кавычек): "Площадь прямоугольника: <значение>".
Вызовите декорированную функцию get_sq
'''


def func_show(func):
    def wrapper(width, height):
        sq = func(width, height)
        print("Площадь прямоугольника {}.".format(sq))
        return sq
    return wrapper


@func_show
def get_sq(width, height):
    return width*height


if __name__ == '__main__':
    width = int(input("Ширина "))
    height = int(input("Высота "))
    get_sq(width, height)
