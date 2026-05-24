import random
import string
import requests
from datetime import date
from urls import AUTH_REGISTER_ENDPOINT, INGREDIENTS_ENDPOINT, ORDERS_ENDPOINT

def register_new_user():
    suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    email = f"order_{suffix}@ya.ru"
    password = "test_password"
    r = requests.post(AUTH_REGISTER_ENDPOINT, json={
        "email": email, "password": password, "name": "OrderTest"
    })
    r.raise_for_status()
    return r.json()["accessToken"]

def get_ingredients():
    r = requests.get(INGREDIENTS_ENDPOINT)
    r.raise_for_status()
    return [ing["_id"] for ing in r.json()["data"][:2]]

def create_order(token, ingredient_ids):
    headers = {"Authorization": token}
    r = requests.post(ORDERS_ENDPOINT, headers=headers, json={"ingredients": ingredient_ids})
    r.raise_for_status()
    return r.json()["order"]["number"]

def get_orders_data(token):
    headers = {"Authorization": token}
    r = requests.get(ORDERS_ENDPOINT, headers=headers)
    r.raise_for_status()
    data = r.json()
    orders = data["orders"]
    total = len(orders)
    today_str = str(date.today())
    today_orders = [o for o in orders if today_str in o.get("createdAt", "")]
    return total, len(today_orders), orders