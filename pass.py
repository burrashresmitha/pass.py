import random
import string

def generate_password(length=12):
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the defined characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Get desired password length from the user
password_length = int(input("Enter the desired length for the password: "))

# Generate and print the password
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)
