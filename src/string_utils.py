"""String helper functions."""


def reverse(s):
    return s[::-1]


def is_palindrome(s):
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
