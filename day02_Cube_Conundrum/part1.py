import re


def is_game_possible(items, color):
    for elem in items:
        cube_number = int(re.search("\d+", elem).group())
        if "red" in color and cube_number > 12:
            return False
        if "green" in color and cube_number > 13:
            return False
        if "blue" in color and cube_number > 14:
            return False
    return True


def get_content_puzzle(file_path):
    with open(file_path, "r") as f:
        content = f.readlines()
    return content


def get_games_sum(content):
    red_pattern = r'\d+ red'
    green_pattern = r'\d+ green'
    blue_pattern = r'\d+ blue'

    games_sum = 0
    for items in content:
        game_number = re.search("\d+", items).group()
        red_cubes = re.findall(red_pattern, items)
        if is_game_possible(red_cubes, "red"):
            green_cube = re.findall(green_pattern, items)
            if is_game_possible(green_cube, "green"):
                blue_cube = re.findall(blue_pattern, items)
                if is_game_possible(blue_cube, "blue"):
                    games_sum += int(game_number)
    return games_sum


filename = "./input/puzzle.txt"
filename_sample = "./input/sample_puzzle.txt"

content = get_content_puzzle(filename)
answer = get_games_sum(content)
print(answer)
