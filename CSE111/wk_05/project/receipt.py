
# Exceeding the Requirements - Buy 1, Get 1 half-off for item D083
    # Lines 52-53
    # Lines 63-71
    # Lines 78-79

import os; os.system('cls')
import csv
import datetime


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

    store_name = 'Mikey\'s Market'
    print(f'{store_name}')

    order_price = 0.0
    request_list = []
    discount_counter = 0
    discount_item = 'D083'
    try: 
        with open(request_csv, 'rt') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            print(f'Requested Items')
            for row_list in reader:
                if len(row_list) != 0:
                    request_list.append(row_list)
            for item in request_list:
                product_no = item[0]
                product_quantity = int(item[1])
                try:
                    product_obj = product_dict[product_no]
                except KeyError:
                    print(f'Error: unknown product ID in the request.csv file')
                    print(f'{product_no}')
                else:
                    if product_no == discount_item:
                        discount_counter += product_quantity
                    print(f'{product_obj[KEY_NAME]}: {product_quantity} @ {product_obj[KEY_PRICE]}')
                    item_price = product_quantity * float(product_obj[KEY_PRICE])
                    order_price += item_price
    except FileNotFoundError as error:
        print(f'Error: Missing File.')
        print(f'{error}')
    except PermissionError:
        print(f'You do not have permission to open this file.')

    discount_amt = 0
    if discount_counter > 1:
        if discount_counter % 2 == 1:
            items_discounted = (discount_counter - 1) / 2
        else:
            items_discounted = discount_counter / 2
        discount_product = product_dict[discount_item]
        discount_amt = items_discounted * (float(discount_product[KEY_PRICE]) / 2)
        order_price -= discount_amt
        
    sales_tax = order_price * 0.06
    total_price = order_price + sales_tax
    now = datetime.datetime.now()
    formatted_date = now.strftime('%a %d %b %H:%M:%S %Y')

    if discount_amt != 0:
        print(f'You saved {discount_amt:.2f} today on {discount_counter} {discount_product[KEY_NAME]}s.')
    print(f'Subtotal: {order_price:.2f}')
    print(f'Sales Tax: {sales_tax:.2f}')
    print(f'Total: {total_price:.2f}')
    print(f'Thank you for shopping at {store_name}.')
    print(f'{formatted_date}')

def read_dictionary(csv_file, index):
    my_dict = {}
    try:
        with open(csv_file, 'rt') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row_list in reader:
                if len(row_list) != 0:
                    key = row_list[index]
                    my_dict[key] = row_list
    except FileNotFoundError as error:
        print(f'Error: Missing File.')
        print(f'{error}')
    except PermissionError:
        print(f'You do not have permission to open this file.')

    return my_dict

if __name__ == "__main__":
    main()