ice_cream = 0
milk = 0
ice_cube = 0

ingredients = input()
for ingredient in ingredients:
    if ingredient == "I":
        ice_cream += 1
    elif ingredient == "M":
        milk += 1
    else:
        ice_cube += 1

if 2 > ice_cream:
    print("I")
elif 1 > milk:
    print("M")
elif 3 > ice_cube:
    print("C")
else:
    print("W")
