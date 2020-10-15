class Room:

    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []
    print("You woke up in a haunted house. You must find your way outside.")
    # Garage 0
    room = Room("You are in the garage of the house.",
                None,
                1,
                None,
                None)
    room_list.append(room)
    # South Hall 1
    room = Room("You are in the south hall. The lights in the room are very dim.",
                4,
                2,
                None,
                0)
    room_list.append(room)
    # Office 2
    room = Room("You are in the office. The room is very very mess.",
                5,
                None,
                None,
                1)
    room_list.append(room)
    # Living room 3
    room = Room("You are in the living room. There is a very old TV on but has no signal.",
                6,
                4,
                None,
                None)
    room_list.append(room)
    # Kitchen 4
    room = Room("You are in the kitchen. You hear a noise, but no one is there.",
                None,
                5,
                1,
                3)
    room_list.append(room)
    # North Hall 5
    room = Room("You are in the north hall of in a house. The lights in the room are very dim.",
                8,
                None,
                2,
                4)
    room_list.append(room)
    # Bathroom 6
    room = Room("You are in the bathroom. You look in the mirror and see a man with a knife behind\nyou. When you turn around, he is gone.",
                None,
                None,
                3,
                None)
    room_list.append(room)
    # Deck
    room = Room("You are on the deck. The stairs are on the north side of the deck.",
                9,
                None,
                None,
                None)
    room_list.append(room)
    # Bedroom 8
    room = Room("You are in the bedroom. You hear footsteps coming your way. Then enters the man with knife.",
                None,
                None,
                5,
                7)
    room_list.append(room)

    current_room = 0

    done = False
    while not done:
        print(room_list[current_room].description)
        user_input = input("What direction do you want to go? ")

        if user_input.lower == "q" or user_input.lower() == "quit":
            done = True

        elif user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You cannot go that direction.")
            else:
                current_room = next_room

        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You cannot go that direction.")
            else:
                current_room = next_room

        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You cannot go that direction.")
            else:
                current_room = next_room

        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You cannot go that direction.")
            else:
                current_room = next_room

        else:
            print("The input was not understood.")

        if current_room == 9:
            print("You won!")
            done = True


main()
