def play_intro():
    print("You stand at the edge of the Whispering Forest.")
    choice = input("Do you go left or right? ").strip().lower()

    if choice == "left":
        print("You find an old stone marker.")
    elif choice == "right":
        print("You hear running water in the distance.")
    else:
        print("You wait and the sun sets.")
