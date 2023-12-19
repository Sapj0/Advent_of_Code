import re


def get_power_set(red_max, green_max, blue_max):
    return int(red_max)*int(green_max)*int(blue_max)


def get_cube_number(set, color):
    if "red" in color:
        try:
            return int(re.search(red_pattern, set).group().split(" ")[0])
        except:
            return 0
    if "green" in color:
        try:
            return int(re.search(green_pattern, set).group().split(" ")[0])
        except:
            return 0
    if "blue" in color:
        try:
            return int(re.search(blue_pattern, set).group().split(" ")[0])
        except:
            return 0
    return 0


def get_content_puzzle(file_path):
    with open(file_path, "r") as f:
        content = f.readlines()
    return content


def get_sum_games(content):
    answer = 0
    for items in content:
        game_number = re.search("\d+", items).group()
        cube_set = items.split(":")[1].split(";")
        red, green, blue = 0, 0, 0
        for element in cube_set:
            element = element.strip()
            if get_cube_number(element, "red") >= red:
                red = get_cube_number(element, "red")
            if get_cube_number(element, "green") >= green:
                green = get_cube_number(element, "green")
            if get_cube_number(element, "blue") >= blue:
                blue = get_cube_number(element, "blue")
        answer += get_power_set(red, green, blue)
    return answer


filename = "./input/puzzle.txt"
filename_sample = "./input/sample_puzzle.txt"

red_pattern = r'\d+ red'
green_pattern = r'\d+ green'
blue_pattern = r'\d+ blue'

content = get_content_puzzle(filename)
answer = get_sum_games(content)
print(answer)
