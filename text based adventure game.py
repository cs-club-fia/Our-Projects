def move(location, direction):
    if direction in locations[location]["exits"]:
        return locations[location]["exits"][direction]
    else:
        print("You can't go that way.")
        return location

def pick_up_item(location, item):
    if item in items and items[item]["location"] == location:
        items[item]["location"] = "inventory"
        print("You picked up the", item)
    else:
        print("You can't pick up that item.")

def use_item(item):
    if item == "sword":
        print("You used the sword.")
    else:
        print("You can't use that item.")

def main():
    current_location = "start"
    inventory = []

    while True:
        print(locations[current_location]["description"])

        if items[item]["location"] == current_location:
            print("You see a", item)

        command = input("What do you want to do? (move, pick up, use, quit) ")

        if command == "move":
            direction = input("Which direction do you want to go? ")
            current_location = move(current_location, direction)
        elif command == "pick up":
            item = input("What do you want to pick up? ")
            pick_up_item(current_location, item)
        elif command == "use":
            item = input("What do you want to use? ")
            use_item(item)
        elif command == "quit":
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    locations = {
        "start": {
            "description": "You are standing at the beginning of your adventure.",
            "exits": {"north": "forest"}
        },
        "forest": {
            "description": "You are in a dense forest.",
            "exits": {"south": "start", "east": "cave"}
        },
        "cave": {
            "description": "You have entered a dark cave.",
            "exits": {"west": "forest"}
        }
    }

    items = {
        "sword": {"description": "A sharp sword", "location": "cave"}
    }

    main()
