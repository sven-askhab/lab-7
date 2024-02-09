#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':

    a = list(map(float, input().split()))
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    max_el = max(a, key=abs)
    print("Максимальный по модулю элемент:", max_el)

    positivs = [i for i, x in enumerate(a) if x > 0]

    if len(positivs) >= 2:
        start_in = positivs[0]
        end_in = positivs[1]
        sum_between = sum(value for idx, value in enumerate(
                            a[start_in + 1:end_in], start=start_in + 1)
                        )
        print("Сумма элементов:", sum_between)
    else:
        print("Недостаточно положительных элементов в списке.")
