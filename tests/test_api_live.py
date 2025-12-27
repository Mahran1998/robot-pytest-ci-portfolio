import os
import requests

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")

def test_health_live():
    r = requests.get(f"{BASE_URL}/health", timeout=5)
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_calc_add_live():
    r = requests.get(f"{BASE_URL}/calc/add", params={"a": 2, "b": 3}, timeout=5)
    assert r.status_code == 200
    data = r.json()
    assert data["sum"] == 5

def test_create_item_live():
    r = requests.post(f"{BASE_URL}/items", json={"name": "book", "price": 10.129}, timeout=5)
    assert r.status_code == 201
    data = r.json()
    assert data["name"] == "book"
    assert data["price"] == 10.13
    assert data["tax"] == 2.74  # 10.13 * 0.27 = 2.7351 -> 2.74
    assert data["id"] >= 1

def test_create_item_negative_price_returns_400():
    r = requests.post(f"{BASE_URL}/items", json={"name": "bad", "price": -1}, timeout=5)
    assert r.status_code == 400
    assert "price must be" in r.json()["detail"]
