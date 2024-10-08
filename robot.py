# Import random to randomize items in zones, and numpy to generate map
import random
import numpy

# List of items to randomize in zones
items = ['battery+','battery-']

# Initialize battery and inventory
battery = 100
inventory = {}

# Dictionary of zones with randomized items
zones = {
    f"zone{i}": random.sample(items,1)
    for i in range(0, 9)
}

# print(zones) # Print zones for debugging

# Generate Grid for navigation
zonemap = numpy.zeros([3,3])

# Randomize starting position
zonemap[random.randint(0,2)][random.randint(0,2)] = 1

print(zonemap)

run = 0
while run != 3:
    print("\n1. Move to adjacent zone")
    print("2. Check your battery and inventory")
    print("3. Quit Game")
    run = int(input("Enter your choice: "))

    match run:
        case 2:
            items = inventory.keys()
            print(f"Battery at {battery}, and you have")
            for key in items:
                print(f"{key} = {inventory[key]}")
        case 1:
            move = (input("Enter direction: ")
            if move == "up":
            elif move == "down":
            elif move == "left":
            elif move == "right":