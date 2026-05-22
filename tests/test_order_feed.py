import allure
from pages.main_page import MainPage
from helpers import register_new_user, get_ingredients, create_order, get_orders_data
from locators.main_page_locators import MainPageLocators

@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Счётчик 'Выполнено за всё время' увеличивается")
    def test_total_counter_increases(self, driver):
        page = MainPage(driver)
        with allure.step("Авторизуемся и получаем токен"):
            token = register_new_user()
        with allure.step("Открываем главную и переходим в ленту заказов"):
            page.open()
            page.click_orders_feed()
        with allure.step("Получаем исходные счётчики через API"):
            total_before, _, _ = get_orders_data(token)
        with allure.step("Создаём новый заказ"):
            ingredient_ids = get_ingredients()
            create_order(token, ingredient_ids)
        with allure.step("Получаем счётчики после создания заказа"):
            total_after, _, _ = get_orders_data(token)
        with allure.step("Проверяем, что общий счётчик увеличился на 1"):
            assert total_after == total_before + 1

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается")
    def test_daily_counter_increases(self, driver):
        page = MainPage(driver)
        with allure.step("Авторизуемся"):
            token = register_new_user()
        with allure.step("Открываем ленту заказов"):
            page.open()
            page.click_orders_feed()
        with allure.step("Получаем исходный счётчик за сегодня"):
            _, today_before, _ = get_orders_data(token)
        with allure.step("Создаём заказ"):
            ingredient_ids = get_ingredients()
            create_order(token, ingredient_ids)
        with allure.step("Получаем счётчик после заказа"):
            _, today_after, _ = get_orders_data(token)
        with allure.step("Проверяем, что счётчик за сегодня увеличился на 1"):
            assert today_after == today_before + 1

    @allure.title("Номер нового заказа появляется в 'В работе'")
    def test_order_appears_in_progress(self, driver):
        page = MainPage(driver)
        with allure.step("Авторизуемся"):
            token = register_new_user()
        with allure.step("Открываем ленту заказов"):
            page.open()
            page.click_orders_feed()
        with allure.step("Создаём заказ и получаем его номер"):
            ingredient_ids = get_ingredients()
            order_number = create_order(token, ingredient_ids)
        with allure.step("Проверяем через API, что заказ в работе"):
            _, _, orders = get_orders_data(token)
            created_order = next((o for o in orders if o["number"] == order_number), None)
            assert created_order is not None
            assert created_order["status"] in ["pending", "done"]