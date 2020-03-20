from src.utils import add
import pytest


@pytest.mark.parametrize('x, y, result', [
    (10, 10, 20),
    (5, 5, 10),
    (1, 1, 2)
])
def test_add(x, y, result):
    assert add(x, y) == result
