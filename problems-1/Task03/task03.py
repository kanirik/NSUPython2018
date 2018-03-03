############################################
# Author: Irina Kuznetsova                 #
# Program arguments: maximum number        #
############################################

import sys
from bitarray import bitarray
import time

def calcBitArray(n):
    ln = n - 1
    maxnum = n + 1
    lst = bitarray(ln)
    lst.setall(True)
    unity = bitarray(1)
    unity.setall(True)
    p = 0
    while 2 * p + 4 <= maxnum:
        lst[2 * p + 2: n : p + 2] = False
        pos = lst[p + 1:n].search(unity, 1)
        if len(pos) == 0:
            break
        else:
            p += pos[0] + 1
    return lst

def calcList(p, lst):
    lst = [0 if i!=p and i%p==0 else i for i in lst]
    lst=list(filter(lambda x:x!=0,lst))
    
    for i in lst:
        if (i>p):
            calcList(i,lst)
            break
    return lst


def calcSet(p, lst):
    lst = {0 if i!=2 and i%2==0 else i for i in lst}
    lst=set(filter(lambda x:x!=0,lst))

    for i in lst:
        if(i>p):
            calcSet(i,lst)
            break
    return lst

def arrayToList(array):
    return [i + 2 for i, el in enumerate(array) if el]

if __name__ == '__main__':
    n = int(sys.argv[1])
    b = list(range(2, n + 1))
    g = set(range(2, n + 1))
    time0 = time.time()
    array0 = calcBitArray(n)
    time1 = time.time()
    print 'time (BitArray): ', time1 - time0    
    time2 = time.time()
    listres = calcList(2, b)
    time3 = time.time()
    print 'time (List): ', time3 - time2
    time4 = time.time()
    setres = calcSet(2,g)
    time5 = time.time()
    print 'time (Set): ', time5 - time4

    # print arrayToList(array0)
    # print listres
    # print setres
