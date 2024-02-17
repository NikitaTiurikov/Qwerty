import random


def mix(ls: list):
    new_list = []
    while len(new_list) != len(ls):
        word = random.choice(ls)
        if word not in new_list:
            new_list.append(word)
    return new_list


ls = ['Yellow', 'Pink', 'Green', 'Red', 'Black', 'White']

print(mix(ls))