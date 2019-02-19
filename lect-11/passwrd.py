def hasVowels(word):
    if type(word) == str:
        # Proceed to check if there is a
        # vowel
        for letter in word:
            if letter in "aeiou":
                return True
#        print("Hi")
    
        return False
        # Outside the for loop
        
    else:
        return False
            
def fooFor():
    for x in range(5):
        print(x)
    print("Outside the for loop")
    
def fooWhile():
    x = 0
    while(x<5):
        # code for while
        print(x)
        x =x+1
    print("Outside the while loop")

def setPassword():
    # valid password:
    # length > 8
    # and contains'#'
    # e.g. ahiuo#17272 is valid
    # abc is invalid

    while not valid:
        psswrd = input("Enter your password :")
        valid = (len(psswrd)>8) and ('#' in psswrd)
        if valid:
            break
    print("Out of the loop")


        
##        if valid:
##            print("This is a valid password")
##        else:
##            print("this is an invalid password")


    



    
