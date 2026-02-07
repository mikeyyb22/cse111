import os; os.system('cls')
import csv


def main():
    KEY_INDEX = 0
    KEY_NAME = 1
    KEY_PRICE = 2

    script_dir = os.path.dirname(os.path.abspath(__file__))
    product = 'products.csv'
    product_csv = os.path.join(script_dir, product)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    request = 'request.csv'
    request_csv = os.path.join(script_dir, request)

    product_dict = read_dictionary(product_csv, KEY_INDEX)
    print(f'All Products: {product_dict}')

    request_list = []
    with open(request_csv, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        print(f'Requested Items')
        for row_list in reader:
            if len(row_list) != 0:
                request_list.append(row_list)
        for item in request_list:
            product_no = item[0]
            product_quantity = item[1]
            product_obj = product_dict[product_no]
            print(f'{product_obj[KEY_NAME]}: {product_quantity} @ {product_obj[KEY_PRICE]}')



def read_dictionary(csv_file, index):
    my_dict = {}
    with open(csv_file, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[index]
                my_dict[key] = row_list

    return my_dict

if __name__ == "__main__":
    main()