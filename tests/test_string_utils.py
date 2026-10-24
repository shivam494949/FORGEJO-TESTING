from src.string_utils import is_palindrome, reverse


def test_reverse():
    assert reverse("abc") == "cba"


def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("hello")
