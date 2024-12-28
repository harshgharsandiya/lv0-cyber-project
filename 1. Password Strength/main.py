import string
import random

def check_password_strength(password):
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    is_long_enough = len(password) >= 8

    if all([has_upper, has_lower, has_digit, has_special, is_long_enough]):
        return "Strong"
    elif is_long_enough and (has_upper or has_lower) and (has_digit or has_special):
        return "Moderate"
    else:
        return "Weak"

def suggest_stronger_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(12))

password = input("Enter a password: ")
strength = check_password_strength(password)
print(f"Password strength: {strength}")

if strength != "Strong":
    print("Suggestion: ", suggest_stronger_password())