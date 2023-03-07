ingredients = {
    "I": 2,
    "M": 1,
    "C": 3,
    "W": 1,
}
ice_cream = 0
milk = 0
ice_cube = 0
whipped_cream = 0

input = input()
for ingredient in input:
    if ingredient == "I":
        ice_cream += 1
    elif ingredient == "M":
        milk += 1
    elif ingredient == "C":
        ice_cube += 1
    else:
        whipped_cream += 1

if ingredients["I"] > ice_cream:
    print("I")
elif ingredients["M"] > milk:
    print("M")
elif ingredients["C"] > ice_cube:
    print("C")
else:
    print("W")
