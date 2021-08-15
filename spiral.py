# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 19:14:45 2021

@author: Sindhuja Mallappa
"""
import turtle
turtle.bgcolor("black")
seurat=turtle.Turtle()

width=5
height=7

dot_distance=25

seurat.setpos(-250,250)



def spiral(m,n):
    k=0 
    l=0
    flag=0
    seurat.color("white")    
    """m-no. of row
       n-no. of column
       a-matrix(list oof list)
       k-index of row
       l-index of column
    """
    
    while(k<m and l<n):
        
        if(flag==1):
            seurat.right(90)
        
        'Print frist row from the remaining rows'
        for i in range(l,n): #'if n is 4 it goes like 0,1,2,3(4 no.s and not 4)'
            seurat.forward(dot_distance)
        #print(a[k][i], end=" ")
         
        'go to second row'
        k+=1
        flag=1
        
        seurat.right(90)
        'print the last colum by traversing every row left'
        for i in range(k,m):
            seurat.forward(dot_distance)
            #print(a[i][n-1], end=" ")
            
        'go to last row- second last colum last row'
        n-=1
        seurat.right(90)

        if(k<m):
            for i in range(n-1, l-1, -1):  #last starting column in index & -1 reverse traversing'
                seurat.forward(dot_distance)
            #print(a[m-1] [i], end=" ")
                
            'second last row'
            m-=1
        seurat.right(90)

        if(l<n):
            'print the first column in the remaining column'
            for i in range(m-1, k-1, -1):
                seurat.forward(dot_distance)
                #print(a[i][l], end=" ")
            
            l+=1
            
"""a=[]
count=1
for i in range(4):
    l=[]
    for j in range(4):
        l.append(count)
        count+=1
    a.append(l)"""
    
spiral(20,20)