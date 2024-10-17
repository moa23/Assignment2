#This is the contacts class. with different mehtods.
class Contacts:
    
    # We start by initilizingthe class itself. and it is a empty list.
    def __init__(self):
        self.contacts = []
        
    
    
    # A method for adding new contacts.    
    def add_contact(self, name, contact_info, prefered_time="08:00 AM"):
        
        contact = {
            'name':name,
            'contact_info': contact_info,
            'prefered_time': prefered_time
        }
        
        self.contacts.append(contact)
    # A method for removing a contact
    def remove_contact(self, name):
        self.contacts = [c for c in self.contacts if c['name'] != name]
    # A method for getting all the contacts.    
    def get_contacts(self):
        return self.contacts