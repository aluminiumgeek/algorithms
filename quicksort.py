#!/usr/bin/env python 
#
# Simple quicksort & in-place version

import random


def quicksort(lst):
    if len(lst) <= 1:
        return lst
    
    pivot = random.choice(lst)
    
    less = []
    greater = []
    
    for item in lst:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            greater.append(item)
    
    return quicksort(less) + [pivot] + quicksort(greater)


def in_place_qsort(lst, begin=0, end=None):
    if end is None:
        end = len(lst) - 1
    
    if end - begin > 0:
        pivot = lst[begin]
        
        left, right = begin, end
        
        while right > left:
            while lst[left] <= pivot and right > left:
                left += 1
            while lst[right] > pivot and right >= left:
                right -= 1
            
            if right > left:
                lst[left], lst[right] = lst[right], lst[left]
                
        lst[begin], lst[right] = lst[right], lst[begin]
        
        in_place_qsort(lst, begin, right-1)
        in_place_qsort(lst, right+1, end)


lst = random.sample(range(10000), 20)
assert quicksort(lst) == sorted(lst), 'Something went wrong'

lst = random.sample(range(10000), 20)
in_place_qsort(lst)
assert lst == sorted(lst), 'Something went wrong'
