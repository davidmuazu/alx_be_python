def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        item = ""
        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ").strip()
            if item in shopping_list:
                print(f"{item} already in shopping list")
            else:
                shopping_list.append(item)
                print(f"{shopping_list}, {item} was added")
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter item name: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{shopping_list}, {item} was removed")
            else:
                print(f"{item} not found in shopping list")
            pass
        elif choice == '3':
            # Display the shopping list
            #print(f"{shopping_list}")
            print("\nYour shopping list:")
            for lst, item in enumerate(shopping_list, start=1):
                print(f"{lst}. {item}")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
