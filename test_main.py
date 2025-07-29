def test_addition():
    assert 1 + 1 == 2

import pytest

def raises_error():
    raise ValueError("Oops")

def test_raises_error():
    with pytest.raises(ValueError):
        raises_error()

import pytest
from main import add

def test_add():
    assert add(2, 3) == 5

def test_add_error():
    with pytest.raises(TypeError):
        add("a", 1)
