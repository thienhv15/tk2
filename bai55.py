# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 20:36:40 2024

@author: Admin
"""

def chu_vi(dai,rong):
    cv = (dai+rong)*2
    return cv

def dien_ticch(dai,rong):
    dt = dai*rong
    return dt

def ve_hinh(dai,rong):
  hinh_chu_nhat = ""
  for i in range(rong):
    hinh_chu_nhat += '*' * dai + '\n'
  return hinh_chu_nhat

if __name__=='__main__':
    print(chu_vi(2, 3))
    print(dien_ticch(2, 3))
    print(ve_hinh(2,3))