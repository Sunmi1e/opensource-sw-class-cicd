import pytest
from orderlab.pricing import subtotal, final_total

# T1
def test_subtotal_normal():
    assert subtotal(10_000, 2) == 20_000

# T2
def test_subtotal_zero():
    assert subtotal(0, 3) == 0

# T3
def test_subtotal_negative():
    with pytest.raises(ValueError):
        subtotal(-100, 2)

@pytest.mark.parametrize("bad_discount", [-1, 101])
def test_invalid_dicount(bad_discount):
    with pytest.raises(ValueError, match="invalid discount"):
        final_total(10_000, 2, bad_discount)

@pytest.mark.parametrize(
    "price, qty, discount, expected",
    [
        (10_000, 2, 0, 23_000),
        (49_999, 1, 0, 52_999),
        (50_000, 1, 0, 50_000),
        (50_001, 1, 0, 50_001),
        (10_000, 2, 10, 21_000),
        (10_000, 2, 100, 0),
    ],
)
def test_final_total(price, qty, discount, expected):
    assert final_total(price, qty, discount) == expected
