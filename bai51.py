# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:22:35 2024

@author: Admin
"""

def ktra_giatri():
    gtri = input('Nhập giá trị:')
    #if gtri.replace('.','',1).replace('-','',1).isdigit():
     #gtri = float(gtri)
    #cach2 kiem tra, ep kieu int()
    
    #if giatri.lstrip('-').isdigit():
        #gtri = int(gtri)
    #vidu: -123-, catdautrutruocvasau
    if gtri.strip('-').isdigit():
        gtri = int(gtri)
    if -86 <= gtri <= 90:
        return gtri
    print('Kông hợp lệ,nhập lại')
    return ktra_giatri()
if __name__=='__main__':
    print(ktra_giatri())
    
    