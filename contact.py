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