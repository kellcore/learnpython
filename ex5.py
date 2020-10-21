name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
height_in_cm = round(height * 2.54)
weight = 180  # lbs
weight_in_kilos = round(weight * 0.454)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {height_in_cm} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {weight_in_kilos} kilograms heavy.")
print("Actually, that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + height_in_cm + weight + weight_in_kilos
print(
    f"If I add {age}, {height}, {height_in_cm}, {weight}, and {weight_in_kilos} I get {total}.")
