import re


def validate_email(email):
    for i in range(len(email)):
        if email[i] == " ":
            return False
        elif email[i] == "@":
            return re.search(".com", email[i:])


def get_email():
    email = input("Enter an email address to test for validity, Q to quit: ")

    return email


def display_message(email_valid):
    if not email_valid:
        print("Not a valid email address. Please try again.")
    else:
        print("Valid email address.")


if __name__ == "__main__":
    while True:
        email_address = get_email()
        if email_address.lower() == "q":
            break
        display_message(validate_email(email_address))
