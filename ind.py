#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import collections


def br_check(list_1):
    if len(list_1) == 0:
        return True
    else:
        list_1 = list(map(str, list_1))
        f = list_1[0]
        a = list_1[-1]
        if f == '(':
            if a == ')':
                list_1.pop(0)
                list_1.pop(-1)
                return br_check(list_1)
            else:
                return False
        elif f == '[':
            if a == ']':
                list_1.pop(0)
                list_1.pop(-1)
                return br_check(list_1)
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    if br_check(input('Введите строку: ')):
        print('True')
    else:
        print('False')
