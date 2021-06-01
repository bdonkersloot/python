x = 6
print(x)

# try except int casting
xlr = "Megs"
try:
    b = int(xlr)
except:
    print("cannot be done")

# while loop
n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1


# functions
def sayhi():
    print("Say hi to " + xlr)


sayhi()

# definite loop
for i in [2,1,5]:
    print(i)

# Single and double quotes are the same thing!
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print("Happy New Year:" + friend)
print("Done")

if (0 == 0.0):
    print("true")
else:
    print("false")

name = input("Enter:")
print(name)

apple = input("Enter a number:")
try:
    r = int(apple) + 10
    print(r)
except:
    print("Not a number")

# string stuff 
monty = "Monty Python"
print(monty[0:4])
print(monty[8:])

letter = "y" in monty
print(letter)

print(monty.lower())

