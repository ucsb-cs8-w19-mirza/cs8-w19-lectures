# Diba Mirza
# Jan 10, 2019
# lect02-v1.py
# Some silliness with Python strings

name = input("What is your name?")
output = "Hi " + name + name[-1]*5 + '!!!!'
print(output)
print("I meant hi " + name[0] + name[1]*5 + name[2:])
print("Sorry I have a cold,", name[2].upper() + name[1:])


