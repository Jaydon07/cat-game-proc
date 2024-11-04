import questionary

cat_attributes = {
    "intelligence": 50,
    "energy": 50,
    "weight": 50,
    # change the inital values above
}

def percent_confirmer():
    if cat_attributes["energy"] > 100:
        cat_attributes["energy"] = 100
    
    if cat_attributes["intelligence"] > 100:
        cat_attributes["intelligence"] = 100
    
    return

def cat_failed():
    if cat_attributes["energy"] <= 10:
        print(f"Energy low! Make sure to give {name} some relaxation.")
    elif cat_attributes["energy"] <= 0:
        print(f"{name} ran out of energy. You have failed.")
        exit()
    
    if cat_attributes["intelligence"] <= 10:
        print(f"Intelligence low! Make sure to train {name} or let them rest.")
    elif cat_attributes["intelligence"] <= 0:
        print(f"{name} is now too dumb to live! You have failed.")
        exit()

    if cat_attributes["weight"] <= 10:
        print(f"Weight low! Make sure to feed {name}.")
    elif cat_attributes["energy"] <= 0:
        print(f"{name} got too skinny. You have failed.")
        exit()
    
    if cat_attributes["weight"] >= 100:
        print(f"{name} got too fat. You have failed.")
        exit()
    elif cat_attributes["weight"] >= 90:
        print(f"Weight too high! Make sure to let {name} exercise.")
    
    return

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = questionary.text("Enter a name for your cat.").ask()
colour = questionary.select(
    "Choose a colour (use arrow keys): ",
    choices=[
        "White",
        "Black",
        "Grey",
        "Red",
        "Blue",
        "Yellow",
        "Orange",
        "Green",
        "Purple",
        "Pink",
    ]).ask()

# start the while loop
while True:
    # Finish the string below
    option = int(input(f"What would you like to do?\n\n1. Play with {name}\n2. Train {name}\n3. Feed {name}\n4. Put {name} to sleep\n5. Show stats\n6. Exit\n"))
    if option < 1 or option > 6:
        pass
    if option == 1:
        print(f"Now playing with {name}. The cat is having so much fun!")
        cat_attributes['energy'] -= 5
        cat_attributes['intelligence'] += 2
        cat_attributes['weight'] -= 10
        cat_failed()
        percent_confirmer()
        print(f"{name} has lost some weight and learned a lot from the game, though is also more tired.\n")
    elif option == 2:
        print(f"Now training {name} with new knowledge and skills.")
        cat_attributes['energy'] -= 5
        cat_attributes['intelligence'] += 7
        cat_attributes['weight'] -= 1
        cat_failed()
        percent_confirmer()
        print(f"{name} is now smarter, but also tired and marginally thinner.\n")
    elif option == 3:
        print(f"Now feeding {name}.")
        cat_attributes['energy'] -= 4
        cat_attributes['intelligence'] -= 5
        cat_attributes['weight'] += 8
        cat_failed()
        percent_confirmer()
        print(f"{name} has been well-fed, though is a bit more tired and less bright.\n")
    elif option == 4:
        print(f"{name} is now sleeping.")
        cat_attributes['energy'] += 5
        cat_attributes['intelligence'] += 4
        cat_attributes['weight'] -= 4
        cat_failed()
        percent_confirmer()
        print(f"{name} has been well-rested, regaining energy and recharging their brain, but also getting thinner.\n")
    elif option == 5:
        print("Name: " + name)
        print("Fur colour: " + colour)
        print("Energy: " + str(cat_attributes['energy']) + "%")
        print("Intelligence: " + str(cat_attributes['intelligence']) + "%")
        print("Weight: " + str(cat_attributes['weight']) + "%")
    elif option == 6:
        option_2 = questionary.confirm(f"Are you sure you want to quit? This will delete {name}!").ask()
        if option_2 == True:
            exit()
        else:
            pass
