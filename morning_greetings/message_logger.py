import datetime

# A method for logging messages.
def log_message(contact, message):
    # opening the txt document and then writing the log information in there.
    with open("message_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - sent to {contact['name']}: {message} \n")