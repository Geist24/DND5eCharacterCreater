import random


def highest_rolls() -> list:
    """
    A function that determines the rolls 5d6 and drops the lowest two rolls
    :return dice: returns a list of three numbers
    """
    dice = []
    low = 100
    index = 0
    roll_1 = random.randint(1, 6)
    dice.append(roll_1)
    roll_2 = random.randint(1, 6)
    dice.append(roll_2)
    roll_3 = random.randint(1, 6)
    dice.append(roll_3)
    roll_4 = random.randint(1, 6)
    dice.append(roll_4)
    roll_5 = random.randint(1, 6)
    dice.append(roll_5)
    for i in dice:
        if i < low:
            low = i
        else:
            index += 1
    dice.pop(index)
    low = 100
    index = 0
    for i in dice:
        if i < low:
            low = i
        else:
            index += 1
    dice.pop(index)
    return dice


def roll_stats() -> list:
    """
    Function that sums up 3d6 and returns it
    :return : Returns a list that contains 6 numbers
    """
    stats = []
    i = 0
    while i <= 6:
        stat = sum(highest_rolls())
        stats.append(stat)
    return stats
