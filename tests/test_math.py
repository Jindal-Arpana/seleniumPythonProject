import pytest


def add_two_numbers(num1, num2):
    return num1 + num2


@pytest.mark.math
def test_small_numbers():
    assert add_two_numbers(4, 4) == 8, "The sum of 4 and 4 should be 8"


@pytest.mark.math
def test_large_numbers():
    assert add_two_numbers(1000, 2000) == 3000, "The sum of 1000 and 2000 should be 3000"
