# Phonebook Application

# Initialize an empty phonebook
phonebook = {}

# Function to add an entry to the phonebook
def add_entry(name, number):
    if name in phonebook:
        print(f"{name} is already in the phonebook.")
    else:
        phonebook[name] = number
        print(f"Added {name} with number {number}.")

# Function to search for an entry in the phonebook
def search_entry(name):
    if name in phonebook:
        print(f"{name}'s number is {phonebook[name]}.")
    else:
        print(f"{name} is not in the phonebook.")

# Function to delete an entry from the phonebook
def delete_entry(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Deleted {name} from the phonebook.")
    else:
        print(f"{name} is not in the phonebook.")

# Function to list all entries in the phonebook
def list_entries():
    if phonebook:
        print("Phonebook entries:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("The phonebook is empty.")

# Main loop for the phonebook application
def main():
    while True:
        print("\nPhonebook Application")
        print("1. Add Entry")
        print("2. Search Entry")
        print("3. Delete Entry")
        print("4. List Entries")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter the name: ")
            number = input("Enter the phone number: ")
            add_entry(name, number)
        elif choice == '2':
            name = input("Enter the name to search: ")
            search_entry(name)
        elif choice == '3':
            name = input("Enter the name to delete: ")
            delete_entry(name)
        elif choice == '4':
            list_entries()
        elif choice == '5':
            print("Exiting the Phonebook application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
