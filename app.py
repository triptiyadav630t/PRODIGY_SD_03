import sqlite3
import re

# Function to create the contacts table if it doesn't exist
def create_contacts_table():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    phone INTEGER,
                    email TEXT
                 )''')
    conn.commit()
    conn.close()

# Function to add a new contact with validation
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")

    # Email validation using regular expression
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        print("Invalid email address. Please enter a valid email.")
        return

    # Phone number validation
    if not phone.isdigit() or len(phone) < 7:
        print("Invalid phone number. Please enter a valid phone number.")
        return

    # If validation passes, add the contact
    add_contact_to_database(name, phone, email)
    print("Contact added successfully.")

# Function to add a new contact to the database
def add_contact_to_database(name, phone, email):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()

# Function to view all contacts
def view_contacts():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    contacts = c.fetchall()
    conn.close()
    if contacts:
        print("\n--- Contacts ---")
        print("ID\tName\tPhone\tEmail")
        for contact in contacts:
            print(f"{contact[0]}\t{contact[1]}\t{contact[2]}\t{contact[3]}")
    else:
        print("No contacts found.")

# Function to edit a contact
def edit_contact():
    view_contacts()
    contact_id = input("Enter the ID of the contact you want to edit: ")
    new_phone = input("Enter new phone number: ")
    new_email = input("Enter new email address: ")

    # Email validation using regular expression
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if new_email and not re.match(email_pattern, new_email):
        print("Invalid email address. Please enter a valid email.")
        return

    # Phone number validation
    if new_phone and (not new_phone.isdigit() or len(new_phone) < 7):
        print("Invalid phone number. Please enter a valid phone number.")
        return

    # If validation passes, update the contact
    update_contact_in_database(contact_id, new_phone, new_email)
    print("Contact updated successfully.")

# Function to update an existing contact in the database
def update_contact_in_database(contact_id, new_phone, new_email):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("UPDATE contacts SET phone=?, email=? WHERE id=?", (new_phone, new_email, contact_id))
    conn.commit()
    conn.close()
    
def delete_contact():
    view_contacts()
    contact_id = input("Enter the ID of the contact you want to delete: ")
    delete_contact_from_database(contact_id)
    print("Contact deleted successfully.")

# Function to delete a contact from the database
def delete_contact_from_database(contact_id):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()    

# Main function
def main():
    create_contacts_table()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delet")
        print("5.Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact
        elif choice == '5':
            print("Exiting program.")    
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
