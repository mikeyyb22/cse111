# MASS is measured in Earth mass
# DISTANCE is measured in AU (Astronomical Units)

import math
import tkinter as tk
import csv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
celestial_bodies_filename = "celestial_bodies.csv"
celestial_bodies_full_path = os.path.join(script_dir, celestial_bodies_filename)

moons_filename = "moons.csv"
moons_full_path = os.path.join(script_dir, moons_filename)

def main():
    celestial_bodies = read_celestial_bodies_from_csv()
    moons = read_moons_from_csv()

    print(f"Choose an option below:\n1. Planet in relation to sun or another planet\n2. Moon in relation to planet")
    body_input = input()

    if body_input == "1":
        first_body_input = input(f"Enter name of first body: ").lower()
        second_body_input = input(f"Enter name of second body: ").lower()
        input_one_found = find_body(first_body_input, celestial_bodies)
        input_two_found = find_body(second_body_input, celestial_bodies)
        if input_one_found == True:
            first_body = get_body(first_body_input, celestial_bodies)
            first_body_mass = float(first_body["mass"])
            if input_two_found == True:
                second_body = get_body(second_body_input, celestial_bodies)
                second_body_mass = float(second_body["mass"])
                if first_body_mass < second_body_mass:
                    larger_body = second_body
                    smaller_body = first_body
                else:
                    larger_body = first_body
                    smaller_body = second_body
                r1 = calculate_r1(larger_body, smaller_body)
                print(f"The barycenter between {smaller_body["name"]} and {larger_body["name"]} is {r1:.2f}km from the center of {larger_body["name"]}.")
            else:
                second_body = create_body(second_body_input)
                second_body_mass = float(second_body["mass"])
                if first_body_mass < second_body_mass:
                    larger_body = second_body
                    smaller_body = first_body
                else:
                    larger_body = first_body
                    smaller_body = second_body
                r1 = calculate_r1(larger_body, smaller_body)
                print(f"The barycenter between {smaller_body["name"]} and {larger_body["name"]} is {r1:.2f}km from the center of {larger_body["name"]}.")
        else:
            first_body = create_body(first_body_input)
            first_body_mass = float(first_body["mass"])
            if input_two_found == True:
                second_body = get_body(second_body_input, celestial_bodies)
                second_body_mass = float(second_body["mass"])
                if first_body_mass < second_body_mass:
                    larger_body = second_body
                    smaller_body = first_body
                else:
                    larger_body = first_body
                    smaller_body = second_body
                r1 = calculate_r1(larger_body, smaller_body)
                print(f"The barycenter between {smaller_body["name"]} and {larger_body["name"]} is {r1:.2f}km from the center of {larger_body["name"]}.")
            else:
                second_body = create_body(second_body_input)
                second_body_mass = float(second_body["mass"])
                if first_body_mass < second_body_mass:
                    larger_body = second_body
                    smaller_body = first_body
                else:
                    larger_body = first_body
                    smaller_body = second_body
                r1 = calculate_r1(larger_body, smaller_body)
                print(f"The barycenter between {smaller_body["name"]} and {larger_body["name"]} is {r1:.2f}km from the center of {larger_body["name"]}.")


def read_celestial_bodies_from_csv():
    bodies = []

    with open(celestial_bodies_full_path, "rt") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            bodies.append(row)
    return bodies

def read_moons_from_csv():
    moons = []

    with open(moons_full_path, "rt") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            moons.append(row)
    return moons

def calculate_r1(large_body, small_body):
    r1 = 0.0
    m1 = float(large_body["mass"])
    m2 = float(small_body["mass"])
    d1 = float(large_body["distance"])
    d2 = float(small_body["distance"])
    a = d2 - d1
    r1 = a / (1 + (m1 / m2))
    r1 = au_to_km(r1)
    return r1

def calculate_r2(r1, a):
    return

def au_to_km(distance):
    return distance * 149600000

def hill_sphere(first_body, second_body):
    return

def find_body(body, bodies):
    input_found = False
    for planet in bodies:
            if body in planet.values():
                input_found = True
                body_dict = body
    return input_found

def get_body(body, bodies):
    body_dict = {}
    for planet in bodies:
        if body in planet.values():
            body_dict = planet

    return body_dict
    
def create_body(user_input):
    create_planet = input(f"{user_input} not found. Do you wish to create a body? (Y/N)").upper()
    if create_planet == "Y":
        create_name = user_input
        create_mass = input(f"Input mass of {create_name} in Earth mass: ")
        create_distance = input(f"Input distance of {create_name} from the sun in AU: ")
        new_dict = {"name": create_name, "mass": create_mass, "distance": create_distance}
        return new_dict
    else:
        return

if __name__ == "__main__":
    main()