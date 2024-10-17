from morning_greetings.contacts import Contacts
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_messages
from morning_greetings.message_logger import log_message
from morning_greetings.contacts_manger import ContactsManager


def main():
    
    contactsManager = ContactsManager()
    contactsManager.add_contact("Mo", "950995", "08:00")
    contactsManager.add_contact("Ali", "9122225", "09:12")
    
    
    contacts = contactsManager.get_contacts()
    
    
    for contact in contacts:
        message = generate_message(contact)
        send_messages(contact, message)
        log_message(contact, message)
        
    
    print(contacts.get_contacts())
    
    
    print(generate_message("moha"))
    print(send_messages("haøø","akakm"))
    
    
    
if __name__ == "__main__":
    main()