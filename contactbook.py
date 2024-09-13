# Contact Manager System in Python

contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact for {name} added successfully!")

def view_contacts():
    if contacts:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")
    else:
        print("No contacts found.")

def search_contact():
    search_term = input("Search by name or phone number: ")
    found_contacts = {name: details for name, details in contacts.items() if search_term in name or search_term in details['phone']}
    
    if found_contacts:
        for name, details in found_contacts.items():
            print(f"\nName: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
    else:
        print("No contact found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input(f"Enter new phone number (Current: {contacts[name]['phone']}): ")
        email = input(f"Enter new email (Current: {contacts[name]['email']}): ")
        address = input(f"Enter new address (Current: {contacts[name]['address']}): ")
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact for {name} updated successfully!")
    else:
        print(f"No contact found for {name}.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} deleted successfully!")
    else:
        print(f"No contact found for {name}.")

def menu():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the Contact Manager.")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    menu()
