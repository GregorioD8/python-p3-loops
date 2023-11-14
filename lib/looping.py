#!/usr/bin/env python3
import ipdb

def happy_new_year():
    # code goes here!
    for i in range(11):
        print(i)
        while i >= 1:
            i -= 1
    print("Happy New Year!")
    

def square_integers(int_list):
    squared_ints = [num * num for num in int_list]
    return squared_ints

def fizzbuzz():
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)
