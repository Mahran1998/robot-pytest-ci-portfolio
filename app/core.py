from __future__ import annotations

def add(a: int, b: int) -> int:
    return a + b

def safe_divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("division by zero")
    return a / b

def clamp_price(price: float) -> float:
    # Ensures non-negative and two decimals for consistent results.
    if price < 0:
        raise ValueError("price must be >= 0")
    return round(float(price), 2)

def calc_tax(price: float, tax_rate: float = 0.27) -> float:
    if tax_rate < 0:
        raise ValueError("tax_rate must be >= 0")
    return round(price * tax_rate, 2)

def apply_discount(price: float, percent: float) -> float:
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (1 - percent / 100.0), 2)
