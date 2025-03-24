
from Main import is_prime
from Main import is_even
from Main import is_odd

def test_is_prime():
    assert is_prime(3) is True
    assert is_prime(7) is True
    assert is_prime(4) is False


def test_is_even():
    assert is_even(3) is False
    assert is_even(4) is True
    assert is_even(12) is True


def test_is_odd():
    assert is_odd(3) is True
    assert is_odd(5) is True
    assert is_odd(12) is False
