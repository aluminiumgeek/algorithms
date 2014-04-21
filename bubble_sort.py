#!/usr/bin/env python 
#
# Bubble sort

import random


def bubble_sort(lst):
    n = len(lst)
    
    swapped = True
    while swapped:
        swapped = False
        
        for i, item in enumerate(lst):
            if i != n-1 and lst[i] > lst[i+1]:
                lst[i+1], lst[i] = lst[i], lst[i+1]
                swapped = True
    
    return lst


lst = random.sample(range(10000), 20)
assert bubble_sort(lst) == sorted(lst), 'Something went wrong'