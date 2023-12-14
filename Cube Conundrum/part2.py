import re


def sum_cube(items, color):
    for elem in items:
        cube_number = int(re.search("\d+", elem).group())
        if "red" in color and cube_number > 12:
            return False
        if "green" in color and cube_number > 13:
            return False
        if "blue" in color and cube_number > 14:
            return False
    return True


def multiply_cube(number):
    return False


def get_cube_power(set):
    return False


filename = "./input/puzzle.txt"
filename_sample = "./input/sample_puzzle.txt"

with open(filename, "r") as f:
    content = f.readlines()

red_pattern = r'\d+ red'
green_pattern = r'\d+ green'
blue_pattern = r'\d+ blue'

somme_games = 0

for items in content:
    game_number = re.search("\d+", items).group()
    cube_set = items.split(":")[1].split(";")
    cube_set[-1] = cube_set[-1].strip()
    for element in cube_set:
        red = get_cube_power(element)
        green = get_cube_power(element)
        blue = get_cube_power(element)

    # red_cubes = re.findall(red_pattern, items)
    # if sum_cube(red_cubes, "red"):
    #     green_cube = re.findall(green_pattern, items)
    #     if sum_cube(green_cube, "green"):
    #         blue_cube = re.findall(blue_pattern, items)
    #         if sum_cube(blue_cube, "blue"):
    #             somme_games += int(game_number)
    break

print("Bubul est quelqu'un de très très ...")

# print(somme_games)
