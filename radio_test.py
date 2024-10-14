# radio_test.py 
# V1.0 June 24, 2024
# Authored by: Michael Pham 

# The is a test script to facilitate a simple ping pong style communications test between two radios.

import time
from pysquared_eps import cubesat as c

debug_mode = True


options = ['A', 'B']

print( 
''' 
======================================= 
|                                     | 
|              WELCOME!               | 
|       Solar Test Version 1.0        |
|                                     |
=======================================
|       Please Select Your Test       | 
| 'A': All Tests (WIP)                |
| 'B': Solar Power (WIP)              |
| 'C': All Sensors                    |
| 'D': (WIP)                          |
| 'E': (WIP)                          | 
======================================= 
'''
    )

def debug_print(message):
    if debug_mode:
        print(message)

def run_all_tests():
    # TODO Implement All Tests
    print("Not implemented yet")

def all_sensors():
    


test_selection = input()

if test_selection not in options:
    print("Invalid Selection.")
    print("Please refresh the device and try again.")

else: 
    print(
    ''' 
    ======================================= 
    |                                     | 
    |       Verbose Output? (Y/N)         |
    |                                     |
    =======================================
    '''
        )
    
    verbose_selection = input()

    if verbose_selection == 'Y':
        debug_mode = True
    elif verbose_selection == 'N':
        debug_mode = False
    
print(
''' 
======================================= 
|                                     | 
|        Beginning Radio Test         | 
|       Radio Test Version 1.0        |
|                                     |
=======================================
'''
    )

while True:

    if test_selection == 'A':
        time.sleep(1)

    elif test_selection == 'B':
        time.sleep(1)

