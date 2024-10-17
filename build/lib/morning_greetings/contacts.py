class Contacts:
    def __init__(self):
        self.contacts = []
        
        
    def add_contact(self, name, contact_info, prefered_time="08:00 AM"):
        
        contact = {
            'name':name,
            'contact_info': contact_info,
            'prefered_time': prefered_time
        }
        
        self.contacts.append(contact)
        
    def remove_contact(self, name):
        self.contacts = [c for c in self.contacts if c['name'] != name]
        
    def get_contacts(self):
        return self.contacts