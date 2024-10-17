#This is the contactsmanager class. this class includes different methods such as adding, removing, get and list contacts.

class ContactsManager:
    
    #This method initialises the class itself
    def __init__(self):
        self.contacts = [
        {"name": "Alice", "email": "abc@example.com", "preferred_time": "08:00 AM"},
        {"name": "Bob", "email": "bcd@example.com", "preferred_time": "09:00 AM"},
        {"name": "Charlie", "email": "cde@example.com", "preferred_time": "07:30 AM"}
                ]
     
     #this method for adding a new contact. A contact needs to have name, email and prefered_time to be added.
    def add_contact(self, name, email, preferred_time="08:00 AM"):
        
        contact = {
            'name': name,
            'email': email,
            'preferred_time': preferred_time
             }
        
        self.contacts.append(contact)
    
     
     #This method is for removing a contact.
    def remove_contact(self, name):
        
        self.contacts = [c for c in self.contacts if c['name'] != name]
        
    #This method is for getting contacts. This gets all of the contacts.
    def get_contacts(self):
        return self.contacts

    #This method is for listing all the contacts. this will list all the contacts with their name, email and prefered time.
    def list_contacts(self):
        
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")
            
            
        
        
