# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 12:46:47 2021

@author: Sindhuja Mallappa
"""

def Fizzbuzz(r):
    for i in range(1,r):
        if(i%3==0 and i%5==0):
            print("FizzBuzz")
        else:
            if(i%3==0):
                print("Fizz")
            else:
                if(i%5==0):
                    print("Buzz")               
                else:
                    print(i)