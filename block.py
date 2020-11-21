#!/usr/bin/env python3

from xor_utils import xor_many


def create_block(data):
    column2 = xor_many([data[1], data[4], data[8]])
    column3 = xor_many([data[2], data[5], data[9]])
    column4 = xor_many([data[0], data[3], data[6], data[10]])

    row2 = xor_many([data[1], data[2], data[3]])
    row3 = xor_many([data[4], data[5], data[6]])
    row4 = xor_many([data[7], data[8], data[9], data[10]])

    bit1 = str(xor_many([column2, column4]))
    bit2 = str(xor_many([column3, column4]))
    bit4 = str(xor_many([row2, row4]))
    bit8 = str(xor_many([row3, row4]))
    bit0 = str(xor_many([bit1, bit2, bit4, bit8, xor_many(data)]))

    block = bit0+bit1+bit2+data[:1]+bit4+data[1:4]+bit8+data[4:7]+data[7:]

    return block