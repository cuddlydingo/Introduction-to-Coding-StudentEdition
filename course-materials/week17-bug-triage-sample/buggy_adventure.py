def show_menu():
    print("1) Start")
    print("2) Score")
    print("3) Exit")


def start_game(points):
    choice = input("Choose left/right: ")
    if choice == "left":
        points + 10
    elif choice == "right":
        points + 5
    else:
        print("Unknown path")
    return points


def main():
    score = "0"

    while True:
        show_menu()
        pick = input("Menu choice: ")

        if pick == "1":
            score = start_game(score)
        elif pick == "2":
            print("Score:", score + 5)
        elif pick == "3":
            print("Goodbye")
            break
        else:
            print("Invalid")


main()
