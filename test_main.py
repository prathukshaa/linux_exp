def test_addition():
    assert 1 + 1 == 2

import pytest

def raises_error():
    raise ValueError("Oops")

def test_raises_error():
    with pytest.raises(ValueError):
        raises_error()

