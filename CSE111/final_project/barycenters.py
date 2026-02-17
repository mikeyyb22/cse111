# MASS is measured in Earth mass
# DISTANCE is measured in AU (Astronomical Units)
# RADIUS is measured in km

import csv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
celestial_bodies_filename = "celestial_bodies.csv"
celestial_bodies_full_path = os.path.join(script_dir, celestial_bodies_filename)

moons_filename = "moons.csv"
moons_full_path = os.path.join(script_dir, moons_filename)

SOL_INDEX = 0

def main():
    celestial_bodies = read_celestial_bodies_from_csv()
    moons = read_moons_from_csv()
    program_run = True
    the_sun = celestial_bodies[SOL_INDEX]

    while program_run == True:
        print(f"Choose an option below:\n1. Planet in relation to sun\n2. Moon in relation to planet\n3. Quit")
        user_input = input()

        if user_input == "1":
            body_input = input(f"Enter name of planet: ").lower()
            body_found = find_body(body_input, celestial_bodies)
            if body_found == True:
                planet = get_body(body_input, celestial_bodies)
                r1 = calculate_r1(planet, the_sun)
                r1 = round(r1, 2)
                print(f"The barycenter between {planet["name"]} and the sun is {r1}km from the center of the sun.")
                outside_radius(the_sun, r1)
                continue

            else:
                planet = create_body(body_input)
                if planet == None:
                    continue
                else:
                    r1 = calculate_r1(planet, the_sun)
                    r1 = round(r1, 2)
                    print(f"The barycenter between {planet["name"]} and the sun is {r1}km from the center of the sun.")
                    outside_radius(the_sun, r1)
                    continue

        if user_input == "2":
            moon_input = input(f"Please enter the name of the moon: ").lower()
            moon_found = find_body(moon_input, moons)
            if moon_found == True:
                moon_1 = get_body(moon_input, moons)
                planet_1 = get_body(moon_1["planet"], celestial_bodies)
                temp_distance = planet_1["distance"]
                planet_1["distance"] = 0
                moon_r1 = calculate_r1(moon_1, planet_1)
                moon_r1 = round(moon_r1, 2)
                planet_1["distance"] = temp_distance
                print(f"The barycenter between {moon_1["name"]} and {planet_1["name"]} is {moon_r1:.2f}km from the center of {planet_1["name"]}.")
                outside_radius(planet_1, moon_r1)
                rH = hill_sphere(the_sun, planet_1)
                rH = round(rH, 2)
                calc_influence(rH, planet_1, moon_1)
                continue
            else:
                moon_1 = create_body(moon_input)
                if moon_1 == None:
                    continue
                planet_name = input(f"What planet does {moon_1["name"]} orbit? ").lower()
                planet_1 = get_body(planet_name, celestial_bodies)
                temp_distance = planet_1["distance"]
                planet_1["distance"] = 0
                moon_r1 = calculate_r1(moon_1, planet_1)
                moon_r1 = round(moon_r1, 2)
                planet_1["distance"] = temp_distance
                print(f"The barycenter between {moon_1["name"]} and {planet_1["name"]} is {moon_r1:.2f}km from the center of {planet_1["name"]}.")
                outside_radius(planet_1, moon_r1)
                rH = hill_sphere(the_sun, planet_1)
                rH = round(rH, 2)
                calc_influence(rH, planet_1, moon_1)
                continue

        else:
            program_run = False
            
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

def calculate_r1(small_body, large_body):
    r1 = 0.0
    m1 = float(large_body["mass"])
    m2 = float(small_body["mass"])
    d1 = float(large_body["distance"])
    d2 = float(small_body["distance"])
    a = abs(d2 - d1)
    r1 = a / (1 + (m1 / m2))
    r1 = au_to_km(r1)
    return r1

def au_to_km(distance):
    return distance * 149600000

def hill_sphere(sun, planet):
    m1 = float(sun["mass"])
    m2 = float(planet["mass"])
    a = float(planet["distance"])
    rH = a * ((m2/(3 * m1)) ** (1/3))
    rH = au_to_km(rH)
    return rH
    
def calc_influence(hill_sphere, planet, moon):
    a = float(moon["distance"])
    a = au_to_km(a)
    m1 = float(planet["mass"])
    m2 = float(moon["mass"])

    if a <= hill_sphere:
        if m2 > m1:
            print(f"You created a moon that is larger than the planet it is supposed to orbit. Therefore, {planet["name"]} actually has started to orbit {moon["name"]}. Nice.")
            return False
        print(f"{moon["name"]} is within the Hill Sphere of {planet["name"]}. The barycenter between the two bodies is \'meaningful\' and {moon["name"]} orbits {planet["name"]}.")
    else:
        print(f"{moon["name"]} is {a}km away from {planet["name"]}, so it is not within the Hill Sphere of {planet["name"]}. The barycenter of the two objects is mathematical and has little to no effect on either body. {moon["name"]} orbits the sun.")
    return True

def outside_radius(large_body, r1):
    radius = float(large_body["radius"])
    if r1 > radius:
        print(f"The barycenter lies outside of {large_body["name"]}!")
        return True
    return False

def find_body(body, bodies):
    input_found = False
    for planet in bodies:
            if body in planet.values():
                input_found = True
    return input_found

def get_body(body, bodies):
    body_dict = {}
    for planet in bodies:
        if body in planet.values():
            body_dict = planet

    return body_dict
    
def create_body(user_input):
    create_planet = input(f"{user_input} not found. Do you wish to create a body? (Y/N) ").upper()
    if create_planet == "Y":
        create_name = user_input
        create_mass = input(f"Input mass of {create_name} in Earth mass: ")
        create_distance = input(f"Input distance of {create_name} from the sun (or planet, if you are creating a moon) in AU: ")
        new_dict = {"name": create_name, "mass": create_mass, "distance": create_distance}
        return new_dict
    else:
        return None

if __name__ == "__main__":
    main()