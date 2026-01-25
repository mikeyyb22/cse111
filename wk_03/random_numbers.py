import random

def main():
    num_list = []
    word_list = []

    append_random_numbers(num_list)
    append_random_numbers(num_list, 5)
    print(num_list)

    append_random_words(word_list)
    append_random_words(word_list, 5)
    print(word_list)

    

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded_num = round(random_number, 1)
        numbers_list.append(rounded_num)

def append_random_words(words_list, quantity=1):
    candidates = ["arm", "car", "cloud", "head", "heal", "hydrogen", "jog",
        "join", "laugh", "love", "sleep", "smile", "speak",
        "sunshine", "toothbrush", "tree", "truth", "walk", "water"]
    
    for _ in range(quantity):
        word = random.choice(candidates)
        words_list.append(word)


if __name__ == "__main__":
    main()