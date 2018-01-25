#!/usr/bin/python3
# -*- coding: utf-8 -*-
while True:
    try:
        x = float(input("Please enter a number: "))
        y = 14 / x
        print(y)
    except ZeroDivisionError:
        print("Oops!  That was no valid number.  Try again...")
    except Exception:
        print("Oops! That was no number. Try again...")
