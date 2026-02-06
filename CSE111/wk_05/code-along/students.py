import os; os.system('cls')
import csv

def main():
    KEY_INDEX = 0
    NAME_INDEX = 1

    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = 'students.csv'
    full_path = os.path.join(script_dir, filename)

    students = read_dictionary(full_path, KEY_INDEX)
    i_number = input('Please enter an I-Number: ')
    student = students[i_number]
    name = student[NAME_INDEX]
    print(f'The student\'s name is {name}')

def read_dictionary(filename, key_column_index):
    s_dictionary = {}
    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                s_dictionary[key] = row_list
    
    return s_dictionary

if __name__ == "__main__":
    main()