#!/usr/bin/env python3

from xor_utils import xor_many


def check_block(block, mode):
    p1 = xor_many([int(block[1]), block[5], block[9], block[13],
                   int(block[3]), block[7], block[11], block[15]])
    b1 = bool(p1 == 0)

    p2 = xor_many([block[2], block[6], block[10], block[14],
                   block[3], block[7], block[11], block[15]])
    b2 = bool(p2 == 0)

    p4 = xor_many([block[4], block[6], block[12], block[14],
                   block[5], block[7], block[13], block[15]])
    b4 = bool(p4 == 0)

    p8 = xor_many([block[12], block[8], block[10], block[14],
                   block[13], block[9], block[11], block[15]])
    b8 = bool(p8 == 0)

    if mode=="debug":
        return p1,b1,p2,b2,p4,b4,p8,b8
    elif mode=="boolean"
        return b1,b2,b4,b8
