def FizzBuzz(x):
    # if x is a multiple of 3 print Fizz
    if x % 15  == 0:
        print("FizzBuzz")
        return
    else:
        # you can nest if-else statements
        if x % 3 == 0:
            print("Fizz")
        else:
            if x % 5 == 0:
                print("Buzz")
            else:
                print(x)

def FizzBuzz_2(x):
    # if x is a multiple of 3 print Fizz
    if x % 15  == 0:
        print("FizzBuzz")       
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)


            

