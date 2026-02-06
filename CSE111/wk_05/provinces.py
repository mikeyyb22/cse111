def main():
    provinces = read_file()
    provinces.pop(0)
    provinces.pop()

    provinces, ab_count = ab_replace(provinces)

    print(provinces)
    print(f'Alberta occurs {ab_count} times in the modified list.')


def read_file():
    province_list = []

    with open("provinces.txt", "rt") as text_file: 
        for line in text_file:
            clean_line = line.strip()
            province_list.append(clean_line)

    return province_list

def ab_replace(my_list):
    alberta_count = 0
    for index, value in enumerate(my_list):
        if value == "AB":
            my_list[index] = "Alberta"
        
    for index, value in enumerate(my_list):
        if value == "Alberta":
            alberta_count += 1

    return my_list, alberta_count

if __name__ == "__main__":
    main()