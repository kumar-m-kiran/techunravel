#!/usr/bin/python
'''
Description : Script to
1. show the performance bottleneck when numpy append is used directly
2. efficient way to handle the loading of numpy array

How to Run and sample result

blr-lvtb9:~/workspace/git/techunravel/examples/python$ python numpy_append_performance.py
-------------------------------
Time taken to directly append to numpy [0.0650050640106], nr elements after append [10000]
Time taken to indirectly append to numpy [0.00114607810974], nr elements after append [10000]
-------------------------------
Time taken to directly append to numpy [0.21977686882], nr elements after append [20000]
Time taken to indirectly append to numpy [0.00235295295715], nr elements after append [20000]
-------------------------------
Time taken to directly append to numpy [0.663153886795], nr elements after append [30000]
Time taken to indirectly append to numpy [0.00346493721008], nr elements after append [30000]
-------------------------------
Time taken to directly append to numpy [1.36484885216], nr elements after append [40000]
Time taken to indirectly append to numpy [0.00476002693176], nr elements after append [40000]
-------------------------------
Time taken to directly append to numpy [2.40069913864], nr elements after append [50000]
Time taken to indirectly append to numpy [0.00593090057373], nr elements after append [50000]

'''
import numpy as np
import time as tm

def numpy_direct_append(num_elements):
    st_tm = tm.time()
    arr_numpy = []
    for x in range(num_elements):
        arr_numpy = np.append(arr_numpy,x)
    en_tm = tm.time()
    print("Time taken to directly append to numpy [%s], nr elements after append [%s]" % ((en_tm - st_tm), len(arr_numpy)));

def numpy_indirect_append(num_elements):
    st_tm = tm.time()
    arr_lst = []
    arr_numpy = []
    for x in range(num_elements):
        arr_lst.append(x)

    arr_numpy = np.array(arr_lst)
    en_tm = tm.time()
    print("Time taken to indirectly append to numpy [%s], nr elements after append [%s]" % ((en_tm - st_tm), len(arr_numpy)));

if __name__ == "__main__":
    for num_elements in (10000,20000,30000,40000,50000):
        print('-------------------------------')
        numpy_direct_append(num_elements)
        numpy_indirect_append(num_elements)
