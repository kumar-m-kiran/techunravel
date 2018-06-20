#!/usr/bin/python

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
