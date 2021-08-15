def leaner_search(n,x):
    #sorted list
    element=[] #[] creates a list
    for i in range(1,101): #n+1 coz range gives numbers upto n-1
        element.append(i) #adds elements to the list

    flag=0
    #iterate in the list
    for i in element:
        if(i==x):
            print("Number is found at position" + str(i))
            flag=1
    if(flag==0):
        print("Number not found")