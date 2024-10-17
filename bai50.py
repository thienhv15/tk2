# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:12:08 2024

@author: Admin
"""

def kiemtraso_n(n):
    if n>0 and n%2==0:
        return 1
    elif 0>n and n%2 != 0:
        return -1
    else:
        return 0
if __name__=='__main__':
    print(kiemtraso_n(-1))
