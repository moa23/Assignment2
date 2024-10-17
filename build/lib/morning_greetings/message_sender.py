def send_messages(email, message):
    if not email:
        raise ValueError("Email address is missing!")
    print(f"Sending message to {email}: {message}")