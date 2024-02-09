#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':

    a = list(map(int, input().split()))
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    count_zeros = 0

    for index, value in enumerate(a):
        if value == 0:
            count_zeros += 1
            print("Нулевой элемент найден на индексе:", index)

    print("Общее количество нулевых элементов:", count_zeros)
    