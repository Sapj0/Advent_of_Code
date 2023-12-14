import re
from pathlib import Path

path = Path(__file__).parent / "../input/Trebuchet/puzzle.txt"

# Open the file and read its content.
with path.open() as f:
    puzzle_input = f.read()


def part1(puzzle_input):

    total = 0

    for line in puzzle_input.split('\n'):
        digits = re.findall(r'(\d)', line)
        total += int(digits[0] + digits[-1])

    return total



def part2(puzzle_input):

    def get_digit(x):
        return x if x.isnumeric() else str(letter_digits.index(x))
    
    letter_digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'  
    total = 0

    for line in puzzle_input.split('\n'):
        digits = re.findall(regex, line)
        print(digits[0], digits[-1])
        total += int(get_digit(digits[0]) + get_digit(digits[-1]))

    return total



print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))