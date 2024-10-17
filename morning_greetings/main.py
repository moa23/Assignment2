#Importing all the class and methods we need.
from morning_greetings.contacts import Contacts
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_messages
from morning_greetings.message_logger import log_message
from morning_greetings.contacts_manager import ContactsManager


def main():
    #Initialising the contactsmanager class and using the add_contact method to add new contacts in the list.
    contacts_manager = ContactsManager()
    contacts_manager.add_contact("Mo", "950995", "08:00")
    contacts_manager.add_contact("Ali", "9122225", "09:12")
    
    #Making a contacts variabel that assigned as all the contacts in contacts_manager. this is all the contact objects made in contactsManager class and the ones initialized here.
    contacts = contacts_manager.get_contacts()
    
    #A for loop that goes through all the contacts one by one. and for each contact we genereate a message. We send a message and log the message. And then we print it out.
    for contact in contacts:
        message = generate_message(contact)
        send_messages(contact, message)
        log_message(contact, message)
        
        print(contacts_manager.list_contacts())
    


#A default method for running the main method.
    
if __name__ == "__main__":
    main()