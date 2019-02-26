from math import floor

# Binary Search
def binary(x, a):
    i, j = 0, len(a)-1
    while i < j:
        m = int(floor( (i+j)/2 ))
        if x > a[m]:
            i = m+1
        else:
            j = m
    if x == a[i]: return i
    else: return 0

def ternary_search(x, a):
    m, copy, index = True, a, 0
    while len(a) > 1 and m != 0: # m == 0 means a 2 value sublist of a
        m = floor( len(a)/3 )
        # which third is x in?
        if x < a[m]: 
            a = a[:m]
        elif a[m] <= x < a[m*2]:
            a = a[m:m*2]
            index += m
        elif a[m*2] <= x <= a[-1]:
            a = a[m*2:]
            index += m*2
        else: # x > a[-1]
            return 0
    if copy[index] == x: return index
    elif copy[index+1] == x: return index+1
    else: return 0 # not found

def quarnary_search(x, a):
    m, copy, index = True, a, 0
    while len(a) > 1 and m != 0:
        m = floor( len(a)/4 )
        if x < a[m]:
            a = a[:m]
        elif a[m] <= x < a[m*2]:
            a = a[m:m*2]
            index += m
        elif a[m*2] <= x < a[m*3]:
            a = a[m*2:m*3]
            index += m*2
        elif a[m*3] <= x <= a[-1]:
            a = a[m*3:]
            index += m*3
        else:
            return 0
    if copy[index] == x: return index
    elif copy[index+1] == x: return index+1
    elif copy[index+2] == x: return index+2
    else: return 0


def test(n):
    seq = list(range(-n, n+1))
    for x in seq:
        print('searching for {x} in integers from -{n} to {n}'.format_map(vars()))
        assert binary(x, seq) == quarnary_search(x, seq) == ternary_search(x, seq)
    x = n*10
    print('searching for {x} in integers from -{n} to {n}'.format_map(vars()))
    assert binary(x, seq) == quarnary_search(x, seq)
    x = -x
    print('searching for {x} in integers from -{n} to {n}'.format_map(vars()))
    assert binary(x, seq) == quarnary_search(x, seq)

if __name__ == '__main__':
    test(100000)
