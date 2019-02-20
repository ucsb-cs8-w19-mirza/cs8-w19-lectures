def countAnimals(filename):
    ''' filename is a string
        name of a file
        counts the number of animals
        in the file     
        closes the file
    '''
    f = open(filename)
    data = f.read()
    mylst  = data.split()
    numWords = len(mylst)
    f.close()
    return numWords

def countAnimals2(filename):
    ''' filename is a string
        name of a file
        counts the number of lines
        in the file     
        closes the file
    '''
    numLines = 0
    f = open(filename)
    # read one line at a time
    for line in f:
        print(line.strip())
        numLines = numLines +1

    # close the file
    f.close()
    return numLines

def readAfewLines(filename):
    f = open(filename)
    line = f.readline()
    count =0 # Lines read so far
    while line and count < 3:
        print(line.strip())
        line = f.readline() # Reads a single line
        count = count +1
    f.close()

def writeToFile(filename):
    f = open(filename, 'w')
    # open the file for writing
    f.write('Wow, you folks are really quiet!\n')
    f.close()
    
#print('The number of animals is', countAnimals2('animals.txt'))
readAfewLines('animals.txt')
writeToFile('msgFromDiba.txt')

