#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


def br_check(s):
    start = time.perf_counter()
    m = 0
    for c in s:
        if c == '(':
            m += 1
        elif c == ')':
            m -= 1
            if m < 0:
                return False

    print(f"Время выполнения функции = {time.perf_counter() - start}")
    return m == 0


if __name__ == '__main__':
    if br_check(input('Введите строку: ')):
        print('True')
    else:
        print('False')