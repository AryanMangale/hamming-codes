#!/usr/bin/env python3

def xor(a, b):
    return int(a) ^ int(b)


def xor_many(bit_array):
    temp = 0
    another_temp = 0
    for i in range(0, len(bit_array)):
        bit_val = bit_array[i]
        another_temp = xor(temp, bit_val)
        temp = another_temp
    return int(temp)
