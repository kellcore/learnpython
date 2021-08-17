from sys import exit


def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input(">> ")
    # if "0" in choice or "1" in choice:
    if choice.isdigit():
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    # this is an infinite loop
    while True:
        choice = input(">> ")

        if choice == "Take Honey":
            dead("The bear looks at you and then slaps your face off.")
            # sets bear moved to true
        elif choice == "Taunt Bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        # if bear_moved is true and you enter Taunt Bear again
        elif choice == "Taunt Bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        # if bear_moved is true and you enter open door, you move to gold room
        elif choice == "Open Door" and bear_moved:
            gold_room()
        else:
            print("I don't know what that means.")


def cthulu_room():
    print("Here you see the great evil Cthulu.")
    print("Cthulu has no concept of gender. It stares at you and you go insane.")
    print("Do you FLEE for your life or eat your HEAD?")

    choice = input(">> ")

    if "Flee" in choice:
        start()
    elif "Head" in choice:
        dead("Well, that was tasty!")
    else:
        cthulu_room()


def dead(why):
    print(why, "Good job!")
    # exit() quits the program -> exit(0) is a clean exit and exit(1) throws an error
    exit(0)


def start():
    print("You are in a dark room.")
    print("There is a door to your RIGHT and LEFT.")
    print("Which one do you take?")

    choice = input(">> ")

    if choice == "Left":
        bear_room()
    elif choice == "Right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
