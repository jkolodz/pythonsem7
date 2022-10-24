# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:35:14 2022

@author: kubak
"""

def calculate():
    first_num=input("")
    if(first_num.find('i')!=-1):
        first_num=Complex(0,int(first_num.replace('i','')))
    else:
        first_num=Complex(int(first_num),0)
    symbol=input("")
    sec_num=input("")
    if(sec_num.find('i')!=-1):
        sec_num=Complex(0,int(sec_num.replace('i','')))
    else:
        sec_num=Complex(int(sec_num),0)
        
    if (symbol=='+'):
        c=(first_num+sec_num)
    if( symbol=='-'):
        c=(first_num-sec_num)
    print(c)
    return c

    

class Complex(object):

    def __init__(self,real_,imag_=0.0):
        self.real=real_
        self.imag=imag_
    def __add__(a,b):
        c= Complex(a.real+b.real, a.imag+b.imag)
        return c
    def __mul__(a,b):
        c = Complex(a.real*b.real-b.imag*a.imag, a.imag*b.real+a.real*b.imag)
        return c
    def __str__(self):
        return "%g,%g" % (self.real, self.imag)
    
    @classmethod
    def str_to_cmplx(cls, a):
        if(a.find('i')!=-1):
            a=Complex(0,int(a.replace('i','')))
        else:
            a=Complex(int(a),0)
        return a
    
def main():
    a = Complex(1,1)
    b= Complex (-1, 1)

    c=a+b
    d=a*b
    e = Complex.str_to_cmplx("26i")
    print(a)
    print(b)
    print(c)
    print(d)
    
    calculate()
    
if __name__ == '__main__':
    main()
    