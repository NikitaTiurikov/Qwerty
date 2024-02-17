import random

def shuffle_sequence(sequence):
    words = sequence.split()

    random.shuffle(words)
    
    return ' '.join(words)

input_sequence = input("Введіть послідовність слів: ")

shuffled_sequence = shuffle_sequence(input_sequence)
print("Вихідні дані:", shuffled_sequence)