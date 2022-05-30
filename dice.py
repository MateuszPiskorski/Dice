import re
from random import randint


def check_roll(roll):
    try:
        result = re.match(r'(\d+D\d+(\+|\-)\d+)|(D\d+(\+|\-)\d+)|(D\d+)|(\d+D\d+)', roll).group()
        return result
    except AttributeError:
        return False


def check_dice(dice):
    ALLOWED_DICES = [3, 4, 6, 8, 10, 12, 20, 100]
    if dice in ALLOWED_DICES:
        return True
    return False


def dice_roll():
    player_dice = input("""
    Roll the dice(s):
    pattern: xDy+z
    -> x - how many rolls do you want to do (1-n; optional)
    -> Dy - which dice do you want (available options: D3, D4, D6, D8, D10, D12, D20, D100)
    -> +z/-z - bonus/penalty (1-n; optional)
    place your choice here: """)

    player_dice = check_roll(player_dice)

    if not player_dice:
        print("Incorrect pattern")
        return dice_roll()
    player_dice_list = re.split(r"D|\+|\-", player_dice)

    dice_flag = check_dice(int(player_dice_list[1]))

    if not dice_flag:
        print("Incorrect dice type")
        return dice_roll()

    if player_dice_list[0] == "":
        player_dice_list[0] = 1

    player_dice_list = list(map(int, player_dice_list))

    if '-' in player_dice:
        result = player_dice_list[0] * randint(1, player_dice_list[1]) - player_dice_list[2]
        print("Wynik to:", result)
        return result
    elif '+' in player_dice:
        result = player_dice_list[0] * randint(1, player_dice_list[1]) + player_dice_list[2]
        print("Wynik to:", result)
        return result
    else:
        result = player_dice_list[0] * randint(1, player_dice_list[1])
        print("Wynik to:", result)
        return result


if __name__ == "__main__":
    dice_roll()
