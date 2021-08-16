# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 11:15:05 2021

@author: Sindhuja Mallappa
"""
# Rules
# given number n create a matrix of size n*n 
# n should b odd 
# sum of each, row and diagonal should be m

'''
Facts
M=n(n^2+1)/2

Patterns:
Position of 1 is in the middle row of the last column
next number ie. 2, 1 row less and 1 column more
    if no row above => go to last row
    if no column next(right) => first column
Position contains a number => col (-2) and row (+1)
if no row above and no column next =>(first row, second last column)
Steps:
1. In any magic square, 1 is located at position(n/2, n-1) n/2-row, n-1-column
2. Lets say the position of 1 i.e. (n/2,n-1) is (p,q)=(row,column) then the next number which is 2 is located at (p-1,q+1) podition
    Anytime if the calculated row position becomes -1 then make it n-1 and if column position becomes n then make it 0
3. If the calculated position already contains a number then decrement the column by 2 and increment the row by 1
4. If anytime the row position becomes -1 and columb becomes n, switch it to (0,n-2)
'''

def magic_square(n): #n-num of row n column
    
    magicSquare=[] #list used as a matrix
    for i in range(n): #row
        l=[] #initail list (empty)
        for j in range(n): #column
            l.append(0) #initially all values 0
        magicSquare.append(l) #after each row is appended to 0, row gets appended to the matrix
        
    i=n//2
    j=n-1
    
    num=n*n
    count=1
    
    while(count<=num):
        if(i==-1 and j==n):
            j=n-2
            i=0
        else:
            if(j==n):
                j=0
            if(i<0):
                i=n-1
                
        if(magicSquare[i][j]!=0):
            j=j-2
            i=i+1
            continue
        
        else:
            magicSquare[i][j]=count
            count+=1
        
        i=i-1
        j=j+1
        
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print()
        
    print("The sum of each row/column/diagonal is:" +str(n*(n**2+1)/2))
    
magic_square(3)