import requests
from datetime import date
from urls import INGREDIENTS_ENDPOINT, ORDERS_ENDPOINT, AUTH_REGISTER_ENDPOINT, AUTH_LOGIN_ENDPOINT

def register_new_user():
    """Регистрирует уникального пользователя и возвращает токен."""
    import random, string
    suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    email = f"order_{suffix}@ya.ru"
    password = "test_password"
    r = requests.post(AUTH_REGISTER_ENDPOINT, json={
        "email": email, "password": password, "name": "OrderTest"
    })
    r.raise_for_status()
    return r.json()["accessToken"]

def get_ingredients():
    """Возвращает список ID двух первых ингредиентов."""
    r = requests.get(INGREDIENTS_ENDPOINT)
    r.raise_for_status()
    ingredients = r.json()["data"]
    return [ingredients[0]["_id"], ingredients[1]["_id"]]

def create_order(token, ingredient_ids):
    """Создаёт заказ с авторизацией и возвращает номер заказа."""
    headers = {"Authorization": token}
    r = requests.post(ORDERS_ENDPOINT, headers=headers, json={"ingredients": ingredient_ids})
    r.raise_for_status()
    return r.json()["order"]["number"]

def get_orders_data(token):
    """Возвращает общее количество заказов, количество за сегодня и список заказов."""
    headers = {"Authorization": token}
    r = requests.get(ORDERS_ENDPOINT, headers=headers)
    r.raise_for_status()
    data = r.json()
    orders = data["orders"]
    total = len(orders)
    today_str = str(date.today())
    today_orders = [o for o in orders if today_str in o.get("createdAt", "")]
    today_total = len(today_orders)
    return total, today_total, orders