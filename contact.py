import json 
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input('Enter name: ')
    phone = input('Enter phone number: ')
    email = input('Enter email: ')
    contacts = load_contacts()
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print(f"Contact '{name}' added.")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts available, you have no friends.")
    else:
        print("Contact List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def update_contact():
    contacts = load_contacts()
    view_contacts()
    if contacts:
        contact_num = int(input("Enter the contact number to update: "))
        if 1 <= contact_num <= len(contacts):
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            contacts[contact_num - 1] = {"name": name, "phone": phone, "email": email}
            save_contacts(contacts)
            print(f"Contact {contact_num} updated.")
        else:
            print("Invalid contact number.")

def delete_contact():
    contacts = load_contacts()
    view_contacts()
    if contacts:
        contact_num = int(input("Enter the contact numner to delete: "))
        if 1 <= contact_num <= len(contacts):
            removed_contact = contacts.pop(contact_num - 1)
            save_contacts(contacts)
            print(f"Contact '{removed_contact['name']}' deleted.")
        else:
            print("Invalid contact number.")

def main():
    while True:
        print("\nContact Book CLI App")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()