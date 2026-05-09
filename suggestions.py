import getpass
import random
import string

def hidden_input(prompt="Enter a password: "):
    return getpass.getpass(prompt)

def generate_strong_password(length=12):
    # Ensure at least one of each category
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("@$!%*?&")

    remaining_length = length - 4
    all_chars = string.ascii_letters + string.digits + "@$!%*?&"
    remaining = ''.join(random.choice(all_chars) for _ in range(remaining_length))

    password = upper + lower + digit + special + remaining
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)
