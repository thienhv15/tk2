# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 19:54:00 2024

@author: Admin
"""
import math
#a
def tong_1(n):
    tonga = 0
    for i in range(1,n+1):
        tonga += i
    return tonga
#b
def tong_binh_phuong(n):
    tongb = 0
    for i in range(1, n + 1):
        tongb += i * i
    return tongb
#c
def tong_nghich_dao(n):
    tongc = 0
    for i in range(1,n+1):
        tongc += 1/i
    return tongc
#d
def tong_giai_thua(n):
    tongd = 0
    for i in range(1, n + 1):
        tongd += math.factorial(i)
    return tongd
#e 
def  tong_tich(n):
    tonge = 1
    for i in range(1,n+1):
        tonge *= i
    return tonge
if __name__=='__main__':
    print(tong_1(3))
    print(tong_binh_phuong(4))
    print(tong_giai_thua(5))
    print(tong_nghich_dao(6))
    print(tong_tich(7))    
        