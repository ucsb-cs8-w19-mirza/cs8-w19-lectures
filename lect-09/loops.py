# Topic
# Doing repetitive tasks in code
# without writing repetitive code
# DRY : Don't repeat yourself!
'''
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
'''

# Solution is loops
# for loop
y = 5 
for x in [1, 2, 3, 4, 5]:
    # Code that needs to be repeated
    # body of the for statement
    print("Hello")
    print(" x = ", x)

print("Loop is done")
name = "Harry Potter"
for y in name:
    print(y, end=",")

tup = (1, 10, 100, 200)
print("\n")

for t in tup:
    print(t, end=" ")

for x in range(5):
    # Think of range(n) as a function
    # that returns a list of number
    # 0 - n-1 
    print("Hello")
    print(" x = ", x)
    
print("\n\n\n")
for x in range(5):
    # Think of range(n) as a function
    # that returns a list of number
    # 0 - n-1
    for y in range(3):
        print("Hello"*y)

for x in range(1, 4, 2):
    # [1, 3]
    print(2**x, end=' ')

    
    





