import random


def main():
    print("Welcome to Camel!")
    print("""You have stolen a Camel to get across the Sahara Desert.
However, the natives are after you. You must survive the journey and outrun the natives.
Hint: Conserve your resources""")

    # Variables
    playerTraveled = 0
    nativesTraveled = -20
    thirst = 0
    camelFatigue = 0
    canteen = 3
    oasis = -1
    nativesFlank = -1
    done = False

    # Main Loop
    while not done:
        nativesBehind = playerTraveled - nativesTraveled
        moderateSpeed = random.randrange(6, 12)
        fullSpeed = random.randrange(11, 18)
        print("""
        a. Ahead at moderate speed
        b. Ahead at full speed
        c. Stop for the night
        d. Drink for your canteen
        e. Status check
        q. Quit""")

        userInput = input("What do you choose? ")
        if userInput.lower() == "q":
            done = True

        # Ahead at moderate speed
        elif userInput.lower() == "a":
            print("You traveled", moderateSpeed, "miles.")
            playerTraveled += moderateSpeed
            nativesTraveled += random.randrange(7, 13)
            thirst += 1
            camelFatigue += 1
            oasis = random.randrange(1, 20)
            nativesFlank = random.randrange(1, 20)

        # Ahead at full speed
        elif userInput.lower() == "b":
            print("You traveled", fullSpeed, "miles.")
            playerTraveled += fullSpeed
            nativesTraveled += random.randrange(7, 13)
            thirst += 1
            camelFatigue += random.randrange(2, 4)
            oasis = random.randrange(1, 20)
            nativesFlank = random.randrange(1, 20)

        # Stop for the night
        elif userInput.lower() == "c" and not done:
            print("Your camel is fully rested.")
            nativesTraveled += random.randrange(7, 13)
            camelFatigue *= 0

        # Drink from your canteen
        elif userInput.lower() == "d":
            if canteen == 0:
                print("Your canteen is empty.")
            else:
                canteen -= 1
                print("You are fully hydrated.")
                print("You have", canteen, "drinks remaining")
                thirst *= 0

        # Status Check
        elif userInput.lower() == "e":
            print("You have traveled", playerTraveled, "miles.")
            print("The natives are", nativesBehind, "miles behind you.")
            print("You have", canteen, "drinks remaining")

        if oasis == 15 and not done:
            print("""You lucked out. You stumbled upon an oasis.
You are fully hydrated and your hors is fully rested.
You also refilled your canteen.""")
            thirst *= 0
            camelFatigue *= 0
            canteen = 3

        if nativesFlank == 15 and not done:
            nativesTraveled += 20
            print("The natives have found a shortcut and gained some ground.")

        if 4 < thirst <= 6 and not done:
            print("You are thirsty.")

        if thirst > 6:
            print("You died of dehydration!")
            done = True

        if 5 < camelFatigue <= 8 and not done:
            print("Your camel is tired.")

        if camelFatigue > 8:
            print("""Your camel has died. You were now stranded in the desert.
The natives caught you and ate you because the were mad that you killed
their camel.""")
            done = True

        if nativesTraveled >= playerTraveled:
            print("""The natives have captured you. They were taking you back to
camp when you died of dehydration because they took your water.""")
            done = True

        if playerTraveled >= 200 and not done:
            print("""You made it out of the desert and have outrun the natives.
                  YOU WON!""")
            done = True

        if nativesBehind <= 15 and not done:
            print("The natives are getting close.")
            print("They are", nativesBehind, "miles behind you.")


main()
