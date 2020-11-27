#!/usr/bin/env python3

print("Beginning test run.")

print("Import xor utils.")
from xor_utils import *

print("Import check block.")
from check_block import *

print("Import block.")
from block import *

print("Create block with defaults")
block = test()
print(block)

print('\n')
print("Stats for block - check_block.stats - DBUG mode")
print(stats(block, 'DBUG'))

print('\n')
print("Stats for block - check_block.stats - BOOL mode")
print(stats(block, 'BOOL'))

print('/n')
print("")