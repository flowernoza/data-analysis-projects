food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.

# Convert to lists using split
food_cabinet = food.split(",")
equipment_cabinet = equipment.split(",")
pets_cabinet = pets.split(",")
sleep_aids_cabinet = sleep_aids.split(",")

# Alphabetize each list
food_cabinet.sort()
equipment_cabinet.sort()
pets_cabinet.sort()
sleep_aids_cabinet.sort()

# Display results
print("Food Cabinet:", food_cabinet)
print("Equipment Cabinet:", equipment_cabinet)
print("Pets Cabinet:", pets_cabinet)
print("Sleep Aids Cabinet:", sleep_aids_cabinet)


# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.

cargo_hold = [food_cabinet, equipment_cabinet, pets_cabinet, sleep_aids_cabinet]
print(cargo_hold)


# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.

sel = int(input("Please select a cabinet (0 - 3): "))


# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.

if sel >= 0:
    if sel < len(cargo_hold):
        print("Cabinet {} contents: {}".format(sel, cargo_hold[sel]))
    else:
        print("Error: Cabinet {} does not exist. Please choose a number between 0 and 3.".format(sel))


# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”

item = input("Enter the item you're looking for: ").strip().lower()
cabinet = cargo_hold[sel]

if item in cabinet:
    print(f"Cabinet {sel} contains {item}.")
else:
    print(f"Cabinet {sel} DOES NOT contain {item}.")
    
