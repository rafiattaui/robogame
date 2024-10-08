# Import random to randomize items in zones, and numpy to generate map using array
import random
import numpy

# List of items to randomize in zones
items = ['battery+','battery-','battery+']

# Initialize battery and inventory globally so functions can access it
global battery
global score
score = 0
battery = 20
inventory = {}


# Welcome message
print("Welcome to the robot game! You are a robot in a 3x3 grid, and you need to navigate to find the battery to recharge yourself.")
print("You can move up, down, left, and right. You can also check your battery and inventory. Good luck!")
print(" ")

# Dictionary of zones with randomized items
zones = {
    f"zone{i}": random.sample(items,1)
    for i in range(0, 9)
}
# print(zones) # Print zones for debugging

def battery_check(): # Check battery level
    batteries = list(zones.values())
    global battery
    if battery <= 0:
        print("Battery is empty, game over!")
        print(f"Your score is {score}")
        exit()
    remaining_batteries = sum(item.count('battery+') for item in zones.values())
    if remaining_batteries == 0:
        print("No more battery+ in zones, game over!")
        print(f"Your score is {score}")
        exit()
    

def giveitem(): # Function to give item to robot
    global battery
    item = str(zones[zone_locations[tuple(currentpos[0])]]) # Retrieve current location and robot and the zone at current position of robot.
    item = item[2:-2] # String still contains brackets and double quotes, so remove them
    if item == 'battery+': # Check if item is battery+
        battery += 10
        print(f"Found battery, battery level is now {battery}")
        score += 1 # Add 1 score for getting a battery
        
    elif item == 'battery-': # Check if item is battery-
        battery -= 10
        print(f"Lost battery, battery level is now {battery}")
        score -= 1 # Subtract 1 score for losing a battery
        
    zones[zone_locations[tuple(currentpos[0])]].pop() # Remove item from zone
    inventory[item] = inventory.get(item, 0) + 1 # Add item to inventory
    print(inventory)

# Assign zones to locations in the array, are these techincally linked lists?
zone_locations = {}
for i in range(3):
    for j in range(3):
        zone_locations[(i, j)] = f"zone{i*3 + j}"
# print(zone_locations) # Print zone locations for debugging

# Generate Grid for navigation
zonemap = numpy.zeros([3,3])

# Randomize starting position
startingzone = zonemap[random.randint(0,2)][random.randint(0,2)] =  1
print(" ")
print(zonemap)
print(" ")

# Game loop
run = 0
while run != 3: # Run game until user quits
    print("\n1. Move to adjacent zone")
    print("2. Check your battery and inventory")
    print("3. Quit Game")
    print(" ")
    run = int(input("Enter your choice: "))

    match run:
        case 2:
            items = inventory.keys()
            print(f"Battery at {battery}, and you have") # Print battery level
            for key in items: # Show inventory
                print(f"{key} = {inventory[key]}")
        case 1:
            move = (input("Enter direction: ")).lower() # Bear with me, why did I do this to myself?
            currentpos = numpy.argwhere(zonemap == 1) # Get current position of robot and stores it as a array [[x,y]]
            if move == "up":
                if currentpos[0][0] > 0: # Check if robot is at the top edge
                    zonemap[currentpos[0][0], currentpos[0][1]] = 0 # Set current position to 0
                    zonemap[currentpos[0][0] - 1, currentpos[0][1]] = 1 # Set new position to 1
                    print(f"{zonemap}\n")
                    giveitem()
                else:
                    print("Cannot move up, already at the top edge")
                    
            elif move == "down":
                if currentpos[0][0] < 3: # Check if robot is at the bottom edge
                    zonemap[currentpos[0][0], currentpos[0][1]] = 0
                    zonemap[currentpos[0][0] + 1, currentpos[0][1]] = 1
                    print(f"{zonemap}\n")
                    giveitem()
                else:
                    print("Cannot move up, already at the bottom edge")
            elif move == "left":
                if currentpos[0][1] > 0: # Check if robot is at the left edge
                    zonemap[currentpos[0][0], currentpos[0][1]] = 0
                    zonemap[currentpos[0][0], currentpos[0][1] - 1] = 1
                    print(f"{zonemap}\n")
                    giveitem()
                else: print("Already at the left edge")
                
            elif move == "right":
                if currentpos[0][1] < 3: # Check if robot is at the right edge
                    zonemap[currentpos[0][0], currentpos[0][1]] = 0
                    zonemap[currentpos[0][0], currentpos[0][1] + 1] = 1
                    print(f"{zonemap}\n")
                    giveitem()
                else:
                    print("Already at the right edge")
            
            else: print("Invalid move") # If user enters invalid move
            battery_check()
            
print("Bye")