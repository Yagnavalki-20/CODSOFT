# Initialize the contact dictionary
contacts = {}

def display_contact():
    """Function to display all contacts."""
    print("\nName\t\tContact Number")
    print("-" * 30)
    for name, number in contacts.items():
        print(f"{name}\t\t{number}")
    print("-" * 30)

def add_contact():
    """Function to add a new contact."""
    name = input("Enter the contact name: ").strip()
    phone = input("Enter the mobile number: ").strip()
    if name in contacts:
        print(f"{name} already exists with number {contacts[name]}.")
        overwrite = input("Do you want to overwrite it? (y/n): ").strip().lower()
        if overwrite == 'y':
            contacts[name] = phone
            print("Contact updated successfully.")
        else:
            print("Contact not updated.")
    else:
        contacts[name] = phone
        print("Contact added successfully.")

def search_contact():
    """Function to search for a contact."""
    search_name = input("Enter the contact name to search: ").strip()
    if search_name in contacts:
        print(f"{search_name}'s contact number is {contacts[search_name]}.")
    else:
        print("Name not found in contact book.")

def edit_contact():
    """Function to edit an existing contact."""
    edit_name = input("Enter the contact name to edit: ").strip()
    if edit_name in contacts:
        print(f"Current number for {edit_name} is {contacts[edit_name]}.")
        new_number = input("Enter the new mobile number: ").strip()
        contacts[edit_name] = new_number
        print("Contact updated successfully.")
    else:
        print("Name not found in contact book.")

def delete_contact():
    """Function to delete a contact."""
    del_name = input("Enter the contact name to delete: ").strip()
    if del_name in contacts:
        confirm = input(f"Do you want to delete the contact '{del_name}'? (y/n): ").strip().lower()
        if confirm == 'y':
            del contacts[del_name]
            print(f"Contact '{del_name}' deleted successfully.")
            if contacts:
                display_contact()
            else:
                print("Contact book is now empty.")
        else:
            print("Deletion canceled.")
    else:
        print("Name not found in contact book.")

def main():
    """Main function to run the contact book application."""
    while True:
        print("\nContact Book Menu:")
        print("1. Add new contact")
        print("2. Search contact")
        print("3. Display contacts")
        print("4. Edit contact")
        print("5. Delete contact")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue  # Restart the loop if input is invalid

        if choice == 1:
            add_contact()
        elif choice == 2:
            search_contact()
        elif choice == 3:
            if not contacts:
                print("Contact book is empty.")
            else:
                display_contact()
        elif choice == 4:
            edit_contact()
        elif choice == 5:
            delete_contact()
        elif choice == 6:
            print("Exiting the contact book. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
