# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 19:06:27 2024

@author: Admin
"""

import math
#bai52a
def can_bac_n(x,n):
    return x**(1/n)
#bai52b chuoi hoac chu so, giu lai so 0 dang truoc
def dao_so(n):
    return str(n)[::-1]
#so: mat so 0 dang truoc
def dao_so(n):
    return int(str(n)[::-1])
#cach 3 so
def dao(n):
    dao = 0
    while n>0:
        dao = dao*10 + n%10
        n//=10
    return dao

def ktra_chinhphuong(n):
    return int(math.sqrt(n))**2 == n

def ktr_nguyento(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
#so le
def tichsle(n):
    tich = 1
    for i in str(n): #str la tinh chu so le phai dung str(string), neu de khong noi la chu so thi dung for i ....range(1,n+1)
        if int(i)%2 != 0:
            tich *= int(i)
    return tich

#f
def tong_ngto_nho_n(n):
    tong_ngto = 0
    for i in range(2,n):
        if ktr_nguyento(i):
            tong_ngto += i
    return tong_ngto

def tong_chinhphuong(n):
    tong_cp = 0
    for i in range(1,n):
        if ktra_chinhphuong(i):
            tong_cp += i
    return tong_cp

def tong_uoc(n):
    tong = 0
    for i in range(1,n+1):
        if n%i == 0:
            tong += i
    return tong
if __name__=='__main__':
    print(can_bac_n(8, 3))
    print(dao_so(120345))
    print(dao(120345))
    print(ktra_chinhphuong(3))
    print(ktr_nguyento(2))
    print(tichsle(3))
    print(tong_ngto_nho_n(8))
    print(tong_chinhphuong(9))
    print(tong_uoc(12)) 
    
    