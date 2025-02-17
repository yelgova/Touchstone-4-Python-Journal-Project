"""
Password Generator Script
-------------------------
This script generates a secure password based on user-defined criteria, including:
- Length of the password
- Inclusion of uppercase letters
- Inclusion of numbers
- Inclusion of special characters

User input is validated to ensure proper length and selection. The script then generates
a password using random character selection.

Author: Yelyzaveta Dolgova
Date: February 17, 2025
"""

import random
import string

def generate_password(length, use_uppercase, use_numbers, use_specials):
    """Generates a secure password based on user preferences"""
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special_characters = string.punctuation if use_specials else ''
    
    all_characters = lowercase_letters + uppercase_letters + numbers + special_characters
    
    if not all_characters:
        return "Error: No character types selected. Please enable at least one."
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Secure Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 4): "))
            if length < 4:
                print("Error: Password length should be at least 4 characters.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_specials = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    password = generate_password(length, use_uppercase, use_numbers, use_specials)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
