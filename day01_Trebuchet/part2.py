import re

filename = "./input/puzzle.txt"

# Open the file and read its content.
with open(filename, "r") as f:
    content = f.readlines()

somme = 0

terms = ["one", "two", "three", "four",
         "five", "six", "seven", "eight", "nine","\d"]
number_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

pattern = re.compile("|".join(terms))
print(pattern)
regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))' 

for items in content:
    # number = pattern.findall(items)
    number = re.findall(regex, items)
    if number[0].isnumeric():
        res = number[0]
    else:
        res = ''.join(number_dict[number[0]])
    if number[-1].isnumeric():
        res2 = number[-1]
    else:
        res2 = ''.join(number_dict[number[-1]])
    str_somme = res + res2
    somme += int(res + res2)

print(somme)
