#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    w = "Weird"
    nw = "Not Weird"
    
    if(n % 2 != 0):
        print(w)
    elif (n % 2 == 0 and (n >= 2 and n <= 5)):
        print(nw)
    elif(n % 2 == 0 and (n > 6 and n <= 20)):
        print(w)
    elif(n % 2== 0 and n > 20):
        print(nw)
