#!/usr/bin/env python 
#
# Selection sort

import random


def selection_sort(lst):
    n = len(lst)
    
    for i in range(n-1):
        pos = i
        
        for j in range(i+1, n):
            if lst[j] < lst[pos]:
                pos = j
                
        if pos != i:
            lst[i], lst[pos] = lst[pos], lst[i]
    
    return lst


lst = random.sample(range(10000), 20)
assert selection_sort(lst) == sorted(lst), 'Something went wrong'