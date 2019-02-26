import random
from math import floor

def binary_insertion_sort(a):
    for j in range(1, len(a)):
        x = a[j]
        start = i = 0
        end   = j
        # Binary Search
        while start < end:
            m = floor( (start+end)/2 )
            if x > a[m]:
                start = m+1
            else:
                end = m
        i = start
        # insertion
        for k in range(j-i):
            a[j-k] = a[j-k-1]
        a[i] = x
    return a

def generate_random_sequence():
    a = []
    indices = random.randint(2, 11)
    for i in range(indices):
        a.append(random.randint(-100, 100))
    return a

def test(n):
    for trial in range(n):
        a = generate_random_sequence()
        assert binary_insertion_sort(a) == sorted(a)
        print('trail {trial}/{n} passed'.format_map(vars()))

if __name__ == '__main__':
    test(1000000)
