# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 20:53:44 2024

@author: Admin
"""

def tinh(*args, **kwargs):
    hinh = kwargs.get('hinh')
    tinh_thanh = kwargs.get('tinh')

    if hinh == 'vuong':
        canh = args[0]
        if tinh_thanh == 'cv':
            return 4 * canh 
        elif tinh_thanh == 'dt':
            return canh ** 2  

    elif hinh == 'tron':
        ban_kinh = args[0]
        if tinh_thanh == 'cv':
            return 2 * 3.14 * ban_kinh  
        elif tinh_thanh == 'dt':
            return 3.14 * ban_kinh ** 2  

    elif hinh == 'chu_nhat':
        chieu_dai = args[0]
        chieu_rong = args[1]
        if tinh_thanh == 'cv':
            return 2 * (chieu_dai + chieu_rong) 
        elif tinh_thanh == 'dt':
            return chieu_dai * chieu_rong 

    return "Hình không hợp lệ."

print(tinh(10, hinh='vuong', tinh='cv'))  
print(tinh(50, hinh='vuong', tinh='dt'))  
print(tinh(18, hinh='tron', tinh='cv'))   
print(tinh(20, 30, hinh='chu_nhat', tinh='cv'))  
