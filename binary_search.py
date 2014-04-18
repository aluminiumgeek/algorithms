#!/usr/bin/env python 
#
# Recursive implementation of binary search algorithm


def binary_search(iterable, key, imin=None, imax=None):
    if not len(iterable):
        return None

    if imin is None and imax is None:
        imin = 0
        imax = len(iterable)-1
    
    if imax < imin:
        return None
    else:
      imid = imin + (imax - imin) / 2
      
      if iterable[imid] > key:
          return binary_search(iterable, key, imin, imid-1)
      elif iterable[imid] < key:
          return binary_search(iterable, key, imid+1, imax)
      else:
          return imid


lst = [i**2 for i in range(500000)]

test_value = 45
index = binary_search(lst, test_value**2)

assert lst[index] == test_value**2, 'Incorrect value'
