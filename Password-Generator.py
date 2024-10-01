import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    character_sets = []
    if use_uppercase:
        character_sets.append(string.ascii_uppercase)
    if use_lowercase:
        character_sets.append(string.ascii_lowercase)
    if use_digits:
        character_sets.append(string.digits)
    if use_symbols:
        character_sets.append(string.punctuation)

    if not character_sets:
        raise ValueError("At least one character set must be selected!")

    all_characters = ''.join(character_sets)

    # Ensure the password contains at least one of each selected type
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Fill the remaining length with random choices from all selected character sets
    for _ in range(length - len(password)):
        password.append(random.choice(all_characters))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)

# Example usage
length = int(input("Enter the desired password length: "))
use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
print("Generated Password:", password)
