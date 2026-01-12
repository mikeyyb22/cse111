LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def main():
    user_input = True

    while user_input == True:
        user_password = input('Input password to test: ')
        if user_password == 'q' or user_password == 'Q':
            user_input = False
        else:
            password_strength(user_password)

def word_in_file(word, filename, case_sensitive):
    pass

def word_has_character(word, character_list):
    pass

def word_complexity(word):
    pass

def password_strength(password, min_length=10, strong_length=16):
    print(password)

if __name__ == "__main__":
    main()