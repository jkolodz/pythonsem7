# -*- coding: utf-8 -*-

import math as m
import random
from typing import List

def random_matrix(a):
    for x in range(len(a)):
        for y in range(len(a[x])):
            a[x][y]=random.random()
    return a

def add_matrix(a,b):
    if(len(a)!=(len(b))):
        print("wrong lenhth")
        return 0;
    
    c=a;
   
    for x in range(len(a)):
        for y in range(len(a[x])):
            print(a[x][y]+b[x][y])
            c[x][y]=a[x][y]+b[x][y]
    return c;

def new_matrix(size):
    a=[0]*size
    matrix=[a]*size
    return matrix
    
def dot_product(a, b):
    
    if(len(a)!=(len(b))):
        print("wrong lenhth")
        return 0;
    sum=0
    for i in range (len(a)):
        sum+=a[i]*b[i]
    return sum

def mysort(arr):
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if(arr[j]<arr[j+1]):
                arr[j], arr[j+1]= arr[j+1],arr[j]

def square_root(a:int,b:int,c:int)->List[int]:

    delta=b*b-4*a*c
    if(abs(delta)<10**-8):
        return ((-b)/2/a)
    if(delta<0):
        print("No roots")
        return 0
       
    sqrt1=((-b+m.sqrt(delta))/2/a)
    sqrt2=((-b-m.sqrt(delta))/2/a)
    return [sqrt1, sqrt2]

def main():
    print("hello")
    q=square_root(1,2,-4)
    
    q=[None]*20
    for i in range(len(q)):
       q[i]=random.random();
    q2=q1=q
    q1.sort(reverse=True)
    mysort(q2)
    print(q2==q1)
    
    a=[1,2,3,4,5]
    b=[5,6,1,6,3]
    print("dot product is", dot_product(a, b))
    
    size=3
    a=new_matrix(size)
    b=new_matrix(size)    
    a=random_matrix(a)
    b=random_matrix(b)

    c=add_matrix(a, b)
    print(a,"\n")
    print(b,"\n")
    print(c,"\n")
        
if __name__ == '__main__':
    main()
    