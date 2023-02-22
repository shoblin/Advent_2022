import os
import functions.function as func

PATH_DATA = os.path.dirname(__file__)


def count_calories(task_list):
    calories = []
    current_calories = 0

    for calorie in task_list:
        if calorie:
            current_calories += int(calorie)
        else:
            calories.append(current_calories)
            current_calories = 0

    calories.append(current_calories)

    return sorted(calories, reverse=True)


def main():
    lst = func.read_file(PATH_DATA, 'input.txt')
    calories = count_calories(lst)
    print(calories[0])
    print(sum(calories[0:3]))


if __name__ == '__main__':
    main()