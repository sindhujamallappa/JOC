#To open a file
#Diffrent modes to open a FileExistsError
#r : read
#w : write(previous data is deleted)
#a : ppending mode, adds data to the present file
#r+ : opens the file, reads n writes - special mode to read n write symultaneously
#have to open the file in particular mode(is important)
with open("Filename.txt", "w") as myfile:
    print(Filename.read())
    #to write in the file
    Filename.write("Iam fine")
Filename.close()


random.randint(1,5) #1-5 inclusive(includes 5 and 1)
random.randrange(1,5) #4,1,3,2,4,3, exclusive to upper limit (excluding 5)
random.random() #0 - 1 random decimal numbers 0.8, 0.5, 0.9, 0.4, 0.3
random.randrange(1,10,2) #step 2, ie. only odd numbers
random.randrange(2,11,2) #step 2, ie. only even numbers
random.choics([1,2,3,4,5]) #generates random numbers from this list
mylist=[6,8,9,0]
random.choice(mylist) #same as above