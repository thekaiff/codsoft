from beautifultable import BeautifulTable

# STEP 1 : DIFINE CONTACT CLASS

class Contact:
    def __init__(self, name, phone, email, address) -> None:
        self.name    = name
        self.phone   = phone
        self.email   = email
        self.address = address

    def __str__(self) -> str:
        return f"Name: {self.name},\nPhone no: {self.phone},\nEmail : {self.email},\nAddress: {self.address}"
   
    def to_list(self):
        return [self.name, self.phone, self.email, self.address]


# STEP 2 : CREATE CONTACT BOOK

class ContactBook:
    def __init__(self) -> None:
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)


    def search_contact(self,name,phone):
        for contact in self.contacts:
            if   contact.name == name or contact.phone == phone:
                print("\n Contact found!\n")
                return contact
            else:
                return f"\nContact not found!\n"
        
    def update_contact(self, name,phone):
        contact = self.search_contact(name,phone)
        if contact:
            print(f"\n\nCurrent details:\n{contact}")
            new_name = input(f"\nEnter new name ({contact.name}): ") or contact.name
            new_phone = input(f"Enter new phone number ({contact.phone}): ") or contact.phone
            new_email = input(f"Enter new email ({contact.email}): ") or contact.email
            new_address = input(f"Enter new address ({contact.address}): ") or contact.address

            contact.name = new_name
            contact.phone = new_phone
            contact.email = new_email
            contact.address = new_address

            print("\nContact updated successfully!")
        else:
            print("\nContact not found!")

    def dlt_contact(self, name):
        # Iterate over the contacts list to find the contact to delete
        for contact in self.contacts:
            if contact.name.lower() == name.lower():  # Ensure the comparison is case-insensitive
                self.contacts.remove(contact)  # Remove the contact from the list
                print(f"\nContact '{name}' deleted successfully.")
                return  # Exit the function after deleting the contact
        
        # If no contact is found with the given name, print a message
        print(f"\nContact '{name}' not found.")

    def display_contact(self):
         table = BeautifulTable()
         table.columns.header = ["name", "phone_no.", "email", "address"]
         for contact in self.contacts:
             table.rows.append(contact.to_list())
             if len(self.contacts) > 0:
                print(table)
             else:
                print("No contacts to display.")



# STEP 3 : IMPLEMENT THE USER INTERFACE 

def  main():
    contact_book = ContactBook()
    
    while True:
        menu = """
        Contact Book Menu:
        1. Add Contact
        2. Search Contact
        3. Update Contact
        4. Delete Contact
        5. View Contact List
        6. Exit
        """
        print(menu)

        choice = input("\nEnter your choice: ")

        if choice == "1":  # Add Contact
            name    = input("\nEnter your Name      : ")
            phone   = input("Enter your Phone no. : ")
            email   = input("Enter your Email     : ")
            address = input("Enter your Address   : ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print("\nContact added successfully!")

        elif choice == "2": # Search Contact
            name    = input("\nEnter the name to search : ")
            phone    = input("Enter the phone number to search : ")
            contact = contact_book.search_contact(name,phone)
            if contact : 
                print("\nContact found: \n")
                contact_book.display_contact()
            else: 
                return f"\nContact not found!"
            
        elif choice == "3": # Update Contact
            name = input("\nEnter the name of the contact to update: ")
            contact_book.update_contact(name,phone)
            
        elif choice == "4": # Delete Contact
            name = input("\nEnter the name of the contact to be deletd: ")
            contact_book.dlt_contact(name)
            print("Contact Deleted.")

        
        elif choice == "5": # Display Contacts
            print("\n\nAll Contacts: \n")
            contact_book.display_contact()

        elif choice == "6": # Exit
            print("\nGoodbye!\n")
            break
        
        else:
            print("\nInvalid choice...")

if __name__ == "__main__":
    main()


