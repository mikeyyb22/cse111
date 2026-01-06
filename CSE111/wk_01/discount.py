import datetime

today = datetime.date.today()
day_number = today.weekday()        # 0-6
subtotal = 1.0

while subtotal != 0.0:
    subtotal = float(input(f'Please input subtotal: '))
    newsubtotal = 0.0

    if subtotal == 0.0:
        break

    day_number = 2

    if day_number == 1 or day_number == 2:
        if subtotal >= 50.0:
            discount = subtotal * 0.1
            newsubtotal = subtotal
            newsubtotal -= discount
        else:
            difference = 50 - subtotal
            print(f'To get the 10% discount, you must spend ${difference:.2f} more.')
            newsubtotal = subtotal
            discount = 0.0
    else:
        newsubtotal = subtotal
        discount = 0.0

    tax = newsubtotal * 0.06
    newsubtotal += tax

    print(f'Subtotal: ${subtotal:.2f}\nDiscount: ${discount:.2f}\nTax: ${tax:.2f}\nTotal: ${newsubtotal:.2f}')