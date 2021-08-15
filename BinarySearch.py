def binary_search(a,x):
    first_pos = 0
    last_pos = len(a-1) #list of array elements starts with 0, len of array is len(a), last elemennt is accessed by a[len(a)-1] 
    flag=0

    while(first_pos<last_pos and flag==0):
        #compute the mid piont of the array
        mid =(first_pos+last_pos)//2 #//gives interger value, where as / gives the floating poit value
        if(x==a[mid]):
            flag==1
            print("The element is found at the position:" +str(mid+1))
            return
        else:
            if(x<a[mid]):
                last_pos = mid-1
            else:
                first_pos = mid+1

print("The number is not found")