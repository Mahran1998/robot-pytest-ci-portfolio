import pytest
from app.core import add, safe_divide, clamp_price, calc_tax, apply_discount

def test_add_basic():
    assert add(1, 2) == 3

@pytest.mark.parametrize("a,b,expected", [
    (0, 0, 0),
    (-1, 1, 0),
    (-5, -7, -12),
    (100, 50, 150),
])
def test_add_param(a, b, expected):
    assert add(a, b) == expected

def test_safe_divide_ok():
    assert safe_divide(10, 2) == 5

def test_safe_divide_float():
    assert safe_divide(1, 4) == 0.25

def test_safe_divide_zero_raises():
    with pytest.raises(ValueError):
        safe_divide(10, 0)

@pytest.mark.parametrize("price,expected", [
    (10, 10.0),
    (10.129, 10.13),
    (0, 0.0),
])
def test_clamp_price_rounding(price, expected):
    assert clamp_price(price) == expected

def test_clamp_price_negative_raises():
    with pytest.raises(ValueError):
        clamp_price(-1)

def test_calc_tax_default_rate():
    assert calc_tax(100.0) == 27.00

def test_calc_tax_custom_rate():
    assert calc_tax(100.0, tax_rate=0.1) == 10.00

def test_calc_tax_negative_rate_raises():
    with pytest.raises(ValueError):
        calc_tax(10.0, tax_rate=-0.1)

@pytest.mark.parametrize("price,percent,expected", [
    (100, 0, 100.00),
    (100, 10, 90.00),
    (199.99, 50, 99.99),
    (10, 100, 0.00),
])
def test_apply_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected

@pytest.mark.parametrize("percent", [-1, 101])
def test_apply_discount_invalid_percent(percent):
    with pytest.raises(ValueError):
        apply_discount(100, percent)
