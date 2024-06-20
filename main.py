import math, random


def calculate_hit_dice_average(lvl, dice):
    average_hp = dice + (math.ceil(dice / 2) * (lvl - 1))

    return average_hp

def calculate_hit_dice_rolled(lvl, dice):
    rolled_hp = dice + (random.randint(1, dice) * (lvl-1))

    return rolled_hp

def calculate_hit_dice_rolled_advantage(lvl, dice):
    roll_a = calculate_hit_dice_rolled(lvl, dice)
    roll_b = calculate_hit_dice_rolled(lvl, dice)
    roll_c = calculate_hit_dice_rolled(lvl, dice)

    return max(roll_a, roll_b, roll_c)

def calculate_multiple_chars_hp(num, lvl, dice):
    list_chars_hp_average = []

    for i in range(num):
        result = calculate_hit_dice_rolled(lvl, dice)
        #result = calculate_hit_dice_rolled_advantage(lvl, dice)
        list_chars_hp_average.append(result)

    return list_chars_hp_average

def calculate_best_result(num, lvl, dice):
    average_hp = calculate_hit_dice_average(lvl, dice)
    list_rolled_hp = calculate_multiple_chars_hp(num, lvl, dice)

    total_rolled_hp = 0
    average_better = 0
    same_hp = 0

    for i in range(num):
        total_rolled_hp += list_rolled_hp[i]

        if average_hp > list_rolled_hp[i]:
            average_better += 1
        elif average_hp == list_rolled_hp[i]:
            same_hp += 1


    average_rolled_hp = float("{:.2f}".format(total_rolled_hp / num))
    perc_avg_better = float("{:.2f}".format((average_better / num) * 100))
    perc_same_hp = float("{:.2f}".format((same_hp / num) * 100))
    perc_rolled_better = float("{:.2f}".format(100 - perc_same_hp -perc_avg_better))

    return average_hp, average_rolled_hp, perc_avg_better, perc_rolled_better, perc_same_hp


def test_dice(num, lvl, dice):
    print("\n\n-------- d%i --------" %dice)
    result = calculate_best_result(num, lvl, dice)

    print ("Average HP:            ", result[0],
           "\nAverage rolled HP:     ", result[1],
           "\nBetter to use average: ", result[2], "%",
           "\nBetter to use rolled:  ", result[3], "%",
           "\nDoesn't matter:        ", result[4], "%")


test_dice(1000000, 20, 6)
test_dice(1000000, 20, 8)
test_dice(1000000, 20, 10)
test_dice(1000000, 20, 12)
