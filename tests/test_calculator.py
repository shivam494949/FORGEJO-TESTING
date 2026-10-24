from src.calculator import add, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    from src.calculator import multiply
    assert multiply(3, 4) == 12


def test_divide():
    import pytest
    from src.calculator import divide
    assert divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
