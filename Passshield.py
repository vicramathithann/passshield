import re
import random
import string

def generate_strong_password():
    """Generate a random strong password."""
    all_chars = string.ascii_letters + string.digits + "@$!%*?&#"
    password = ''.join(random.choice(all_chars) for _ in range(12))
    return password

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Check password length
    if len(password) < 6:
        remarks = "Password too short! Use at least 8 characters."
    elif len(password) >= 8:
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1

    # Check for digits
    if re.search(r"[0-9]", password):
        strength += 1

    # Check for special characters
    if re.search(r"[@$!%*?&#]", password):
        strength += 1

    # Evaluate overall strength
    if strength <= 2:
        remarks = "Weak password"
        suggestion = generate_strong_password()
        print("Suggested stronger password:", suggestion)
    elif strength == 3:
        remarks = "Moderate password"
        suggestion = generate_strong_password()
        print("Try using a stronger password like:", suggestion)
    elif strength >= 4:
        remarks = "Strong password"
    
    return remarks

# Main program
password = input("Enter your password: ")
print(check_password_strength(password))
