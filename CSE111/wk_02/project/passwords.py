import os

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def main():
    user_input = True
    strength = 0

    while user_input == True:
        user_password = input('Input password to test: ')
        if user_password == 'q' or user_password == 'Q':
            user_input = False
        else:
            strength = password_strength(user_password)

def word_in_file(word, filename, case_sensitive=False):
    if case_sensitive == True:
        with open(filename, "r", encoding="utf-8") as pwd_file:
            for line in pwd_file:
                clean_line = line.strip()
                if clean_line == word:
                    return True
                else:
                    continue
            return False
    else:
        word = word.lower()
        with open(filename, "r", encoding="utf-8") as word_file:
            for line in word_file:
                clean_line = line.strip()
                if clean_line == word:
                    return True
                else:
                    continue
            return False

def word_has_character(word, character_list):
    for i in range(len(character_list)):
        for char in word:
            if character_list[i] == char:
                return True
    return False

def word_complexity(word):
    complexity_score = 1
    has_lower = word_has_character(word, LOWER)
    if has_lower == True:
        complexity_score += 1

    has_upper = word_has_character(word, UPPER)
    if has_upper == True:
        complexity_score += 1

    has_digits = word_has_character(word, DIGITS)
    if has_digits == True:
        complexity_score += 1

    has_special = word_has_character(word, SPECIAL)
    if has_special == True:
        complexity_score += 1

    return complexity_score

def password_strength(password, min_length=10, strong_length=16):
    test1 = word_in_file(password, full_path_words)
    if test1 == True:
        print(f'Password is a dictionary word and is not secure.')
        strength = 0
        return strength
    else:
        test2 = word_in_file(password, full_path_pwds, case_sensitive=True)
        if test2 == True:
            print(f'Password is a commonly used password and is not secure.')
            strength = 0
            return strength
        else:
            if min_length > len(password):
                print(f'Password is too short and is not secure.')
                strength = 1
                return strength
            elif len(password) > strong_length:
                print(f'Password is long, length trumps complexity. This is a good password.')
                strength = 5
                return strength
            else:
                complexity = word_complexity(password)
                strength = complexity
                print(f'Passed all tests. Strength score is {strength}')
                return strength

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = "wordlist.txt"
full_path_words = os.path.join(script_dir, filename)

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = "toppasswords.txt"
full_path_pwds = os.path.join(script_dir, filename)

if __name__ == "__main__":
    main()