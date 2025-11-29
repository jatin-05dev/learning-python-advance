import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    user_length = int(input("Enter password length: "))
    print("Generated Password:", generate_password(user_length))



prefix = "AB"
number = 1

def generate_valid_code():
    global number
    code = f"{prefix}{number:03d}"
    number += 1
    return code

if __name__ == "__main__":
    for _ in range(5):
        print(generate_valid_code())
