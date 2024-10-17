import datetime


def log_message(contact, message):
    with open("message_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - sent to {contact['name']}: {message} \n")