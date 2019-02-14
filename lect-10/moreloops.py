def maxGPAOfStudents(lst):
    '''return the maximum gpa of
       in a list of Student
       Student('name', 'major', 'gpa')
       '''
    # Traverse the list
    # Go through each of the elements of the list
    if (lst == []):
        return
    # Assuming that we have a non empty list
    maxGPA = lst[0].gpa
    
    for s in lst:
        #print(s)
        #sumGPA = sumGPA + s.gpa
        if s.gpa > maxGPA:
            maxGPA = s.gpa
        
    return maxGPA
    

from collections import namedtuple
Student = namedtuple("Student","name major gpa")

l1 = [Student("Angel", "ACT", 3.0),
      Student("Joe", "CS", 2.0),
      Student("Jack", "CS", 4.5),
      Student("Jak", "CS", 4.0)]

print(" The max GPA is", maxGPAOfStudents([]))  

def containsOddNumber(lst):
    ''' return True if ANY
    element is odd, else return Fale'''
    
    for x in lst:
        if(x%2 ==1):
            return True
    return False

def largestOddNumber(lst):
    ''' return the largest odd element or -1'''

    maxOdd = -1
    for x in lst:
        if(x%2 == 1):
            if x > maxOdd:
                maxOdd = x
            
    return maxOdd


print("Expect 17", largestOddNumber([1, 17, 20]))

def indexlargestOddNumber(lst):
    
    indexmaxOdd = 0
    for i in range(len(lst)):
        if(lst[i]%2 == 1):
            if lst[i] > lst[indexmaxOdd]:
                indexmaxOdd = i
            
    return indexmaxOdd


print("Expect 1", indexlargestOddNumber([1, 17, 20]))

print("Expect 0", indexlargestOddNumber([111, 17, 20]))


















