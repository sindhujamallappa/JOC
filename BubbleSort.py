def bubble(a):
    n=len(a) #returns the lengthn of any list here list a

    for i in range(n):
        for j in range(0,n-i-1): #Exclude last element
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp

a=[5,2,1,4,8,0]
bubble(a)

for i in a:
    print(i)
    