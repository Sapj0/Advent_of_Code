import re

filename = "./day01_Trebuchet/input/puzzle.txt"

# Open the file and read its content.
with open(filename, "r") as f:
    content = f.readlines()

somme = 0

# print(content)
print(type(content))
for items in content:
    number = re.findall("\d", items)
    str_somme = number[0]+number[len(number)-1]
    somme += int(str_somme)
    
print(somme)
