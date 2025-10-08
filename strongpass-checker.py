#!/usr/bin/env python3
"""
pass_checker.py
Simple Password Strength Checker for Kali Linux with visible input.
"""

import re
import random
import string
import argparse
import sys


def generate_strong_password(length=12):
    """Generate a random strong password."""
    all_chars = string.ascii_letters + string.digits + "@$!%*?&#"
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


def evaluate_strength(password):
    """
    Evaluate password and return (score, remarks, suggestion_if_any)
    Score is 0–5 (higher means stronger)
    """
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    # Digits
    if re.search(r"[0-9]", password):
        score += 1
    # Special characters
    if re.search(r"[@$!%*?&#]", password):
        score += 1

    # Remarks based on score
    if len(password) < 6:
        remarks = "Password too short! Use at least 8 characters."
    elif score <= 2:
        remarks = "Weak password"
    elif score == 3:
        remarks = "Moderate password"
    else:
        remarks = "Strong password"

    suggestion = None
    if score <= 3:
        suggestion = generate_strong_password(12)

    return score, remarks, suggestion


def main():
    parser = argparse.ArgumentParser(
        description="Password Strength Checker (visible input version)."
    )
    parser.add_argument(
        "-p", "--password",
        help="Password to check. If not given, will ask interactively."
    )
    parser.add_argument(
        "-g", "--generate",
        action="store_true",
        help="Generate a random strong password and exit."
    )
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=12,
        help="Length for generated passwords (default: 12)."
    )
    args = parser.parse_args()

    # Option to only generate password
    if args.generate:
        print(generate_strong_password(args.length))
        sys.exit(0)

    # Input visible password
    if args.password:
        password = args.password
    else:
        password = input("Enter your password: ")

    if not password:
        print("No password entered. Exiting.")
        sys.exit(1)

    # Evaluate and print result
    score, remarks, suggestion = evaluate_strength(password)
    print("\nPassword Strength Report")
    print("------------------------")
    print(f"Score: {score}/5")
    print(f"Result: {remarks}")
    if suggestion:
        print(f"Suggested stronger password: {suggestion}")

    sys.exit(0)


if __name__ == "__main__":
    main()
