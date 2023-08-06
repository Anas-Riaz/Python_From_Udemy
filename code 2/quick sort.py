# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 14:51:31 2021

@author: SouLs-TaKeR
"""

def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        pivot=list.pop()
    lesser_list=[]
    greater_list=[]
    for items in list:
        if items < pivot:
            lesser_list.append(items)
        else:
            greater_list.append(items)
    return quick_sort(lesser_list) + [pivot] + quick_sort(greater_list)

def list_input():
    list = []
    n=int(input("enter no. of elements : "))
    for i in range(n):
        element=int(input("enter numbers : "))
        list.append(element)
    print(list)
    print(quick_sort(list))
    

list_input()