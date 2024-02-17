import random

def mixing_printing(string: str):
    splitted_words = string.split(" ")
    
    random.shuffle(splitted_words)
    output_sequence = ' '.join(splitted_words)
    return output_sequence

    
print(mixing_printing("Hello World How Are You?"))
        