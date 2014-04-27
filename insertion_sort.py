#!/usr/bin/env python 
#
# Insertion sort

import random


def insertion_sort(lst):
    for i, item in enumerate(lst):
        prev = i - 1
        while prev >= 0 and lst[prev] > item:
            lst[prev+1], lst[prev] = lst[prev], item
            
            prev = prev - 1
    
    return lst

        
lst = random.sample(range(10000), 20)
assert insertion_sort(lst) == sorted(lst), 'Something went wrong'