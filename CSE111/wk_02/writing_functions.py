def main():
    start_odo = int(input('Enter the first odometer reading(miles): '))
    end_odo = int(input('Enter the second odometer reading (miles): '))
    fuel_used = float(input('Enter the amount of fuel used (gallons): '))

    mpg = miles_per_gallon(start_odo, end_odo, fuel_used)
    lp100k = lp100k_from_mpg(mpg)

    print(f'{mpg} miles per gallon\n{lp100k} liters per 100 kilometers')

def miles_per_gallon(start, end, fuel):
    mpg = round(((end - start) / fuel), 1)
    return mpg

def lp100k_from_mpg(mpg):
    lp100k = round((235.215 / mpg), 2)
    return lp100k

main()