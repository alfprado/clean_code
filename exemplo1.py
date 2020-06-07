#!/usr/bin/python
# -*- coding: utf-8 -*-


def elapse(year):
    days = 365
    '''
    Substituir esse trecho pela função is_leap

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    '''
    if is_leap(year):
        days += 1
    for day in range(1, days + 1):
        print("Day {} of {}".format(day, year))


def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


if __name__ == "__main__":
    elapse(2000)
