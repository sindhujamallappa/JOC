def fizzbuzz(r):
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