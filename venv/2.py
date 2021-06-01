import re


fhand = open("mbox.txt", "w+")
print(fhand)

purse = dict()
purse["money"] = 12
purse["candy"] = 50

print(purse["money"])

counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))

a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)