#!/usr/bin/env python3
"""
Palindrome Checker - A utility to check if strings are palindromes.

A palindrome is a word, phrase, number, or other sequence of characters
that reads the same forward and backward (ignoring spaces, punctuation, and case).
"""

def is_palindrome(text):
    """
    Check if the given text is a palindrome.

    Args:
        text (str): The text to check

    Returns:
        bool: True if text is a palindrome, False otherwise
    """
    if not text:
        return True

    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def main():
    """Run interactive palindrome checker."""
    print("=== Palindrome Checker ===\n")

    test_cases = [
        "racecar",
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw",
        "hello",
        "Madam",
        "12321",
        "12345"
    ]

    print("Testing examples:")
    for test in test_cases:
        result = is_palindrome(test)
        status = "✓ IS" if result else "✗ NOT"
        print(f'{status} a palindrome: "{test}"')

    print("\n" + "="*40)
    print("Try your own! (Press Ctrl+C to exit)\n")

    try:
        while True:
            user_input = input("Enter text to check: ").strip()
            if not user_input:
                continue

            if is_palindrome(user_input):
                print(f'✓ "{user_input}" IS a palindrome!\n')
            else:
                print(f'✗ "{user_input}" is NOT a palindrome.\n')
    except (KeyboardInterrupt, EOFError):
        print("\n\nGoodbye!")


if __name__ == "__main__":
    main()
