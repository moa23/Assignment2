# A method for sending the messages. It has two parameters which is the email and the message.
def send_messages(email, message):
    # A test to check is there is any error. Like for example if there not any email, then a valueError will be raised.
    #If there is both email and the message, we print out the email and the message.
    if not email:
        raise ValueError("Email address is missing!")
    print(f"Sending message to {email}: {message}")