#!/usr/bin/python3
"""
    Prints text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input text

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove leading and trailing spaces initially
    text = text.strip()

    chars = ['.', '?', ':']
    result = ""
    skip_space = False

    for c in text:
        if c in chars:
            result += c + "\n\n"
            skip_space = True  # Skip next space if it's after punctuation
        elif c == ' ' and skip_space:
            continue
        else:
            result += c
            skip_space = False

    print(result, end="")  # Ensure no extra blank lines at the end
