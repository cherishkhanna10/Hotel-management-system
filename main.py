def welcome():
    print("Welcome to library management system ")
welcome()
def menu():
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")
while True:
    menu()
    choice=input("enter a number as per choice ::")
    if choice == "1":
        print("Add Book selected")

    elif choice == "2":
        print("Issue Book selected")

    elif choice == "3":
        print("Return Book selected")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")


