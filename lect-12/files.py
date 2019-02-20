# Data and how to get data into our programs

def foo(lst):
    
    # Data that is created and/or defined inside functions
    # only exists in memory as long as the function is running
    for item in lst:
        print(item)

# Data in programs is not persistent

mylst = ['duck', 'cow', 'cat']
foo(mylst)
# Files give us a way to store data permanently
# You can create the data by opening up a text file
# write the data manually
# Save the file
# Assume that a data file exists

# Goal 1: Read information from the file into our program

# Step 1: Open the file
f = open('myDataWithIDLE.txt')
# f is a connection to our file

# Step 2a: Read from the file
'''
 - read all the data
 - read one line at a time
'''
mydata = f.read() # Reads all the data
# as one giant string
# okay to do for small or medium size files
# for large files: read one line at a time


# Step 2b: Process the data


# Step 3: Close the file
f.close()












