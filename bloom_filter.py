#!/usr/bin/env python 
#
# Implementation of Bloom filter, a space-efficient probabilistic data structure

from hashlib import sha256


class BloomFilter(object):
    
    def __init__(self, store_len=4*1024, probes=10, data=()):
        self.store = bytearray(store_len)
        self.probes = probes
        self.bins_len = store_len * 8
        
        self.update(data)
        
    def update(self, data):
        for key in data:
            for i in self.calc_probes(key):
                self.store[i/8] |= 2**(i%8)
    
    def calc_probes(self, key):
        h = int(sha256(str(key)).hexdigest(), 16)
        
        for _ in range(self.probes):
            yield h & self.bins_len - 1
            h >>= 15
            
    def __contains__(self, key):
        for i in self.calc_probes(key):
            if not self.store[i/8] & 2**(i%8):
                return False
        
        return True


# Test for false positives
a, b  = 0, 1
def fib():
    global a, b
    
    while True:
        a, b = b, a+b
        yield a
        
def test_false_positive(test_len, data, bloom_data):
    false_positive = 0
    for i in range(test_len):
        if i in bloom_data and i not in data:
            false_positive += 1

    print 'Store: {0}kB, errors: {1}/{2}'.format(
        len(bloom_data.store)/1024,
        false_positive,
        test_len
    )
        
fib_iter = fib()

set_of_data = [fib_iter.next() for _ in range(5000)]

test_len = 10000

for store_len in (2**j for j in range(16)):
    bloom_data = BloomFilter(store_len=store_len*1024, data=set_of_data)
    test_false_positive(test_len, set_of_data, bloom_data)
