"""Exceeding the Requirements: 
    Ask user if he/she wants to buy, then collects phone # if yes
    Stores phone # in volumes.txt
"""

import math
import datetime
import os

# Example input: 205/60R15
# formula v = ((pi*(w**2)a)*((w*a)+(2540*d)))/10000000000

directory = r"C:/Users/mcgeh/Desktop/VSCode Files/CSE111/wk_01"
filename = "volumes.txt"
full_path = os.path.join(directory, filename)
os.makedirs(directory, exist_ok=True)
today_date = datetime.date.today()

tire_width = int(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
wheel_diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))
pi = math.pi

tire_volume = ((pi*(tire_width**2)*aspect_ratio)*((tire_width*aspect_ratio)+(2540*wheel_diameter)))/10000000000
tire_volume = round(tire_volume, 2)

print(f'The approximate volume is {tire_volume} liters')

user_buy = input('Would you like to buy tires with the dimensions entered? (Y/N): ').upper()

if user_buy == "Y":
    user_phone = input('Please enter your phone #: ')
    with open(full_path, "at") as volumes_file:
        print(today_date, tire_width, aspect_ratio, wheel_diameter, tire_volume, user_phone, sep=", ", end="\n", file=volumes_file, flush=True)
else:
    with open(full_path, "at") as volumes_file:
        print(today_date, tire_width, aspect_ratio, wheel_diameter, tire_volume, sep=", ", end="\n", file=volumes_file, flush=True)

