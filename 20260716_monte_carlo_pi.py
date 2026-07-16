# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:49:38 2026

@author: hyh19
"""
n,a=list(map(int,input().split()))
m=0
for _ in range (n):
    x,y=list(map(int,input().split()))
    if x*x+y*y<=a*a:
        m+=1
pi=4*m/n
print(pi)
    
