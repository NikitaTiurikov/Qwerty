from random import shuffle


def shuffle_list(lst: list):
    shuffle(lst)
    return lst


colors = ['Yellow', 'Pink', 'Green', 'Red', 'Black', 'White']
print(shuffle_list(colors))
