import allure
from pages.main_page import MainPage

@allure.feature("Основная функциональность")
class TestMainPage:
    @allure.title("Переход в Конструктор")
    def test_go_to_constructor(self, driver):
        page = MainPage(driver)
        with allure.step("Открываем главную страницу"):
            page.open()
        with allure.step("Кликаем на «Конструктор»"):
            page.click_constructor()
        assert page.find_element(MainPageLocators.CONSTRUCTOR_HEADER).is_displayed()

    @allure.title("Переход в Ленту заказов")
    def test_go_to_order_feed(self, driver):
        page = MainPage(driver)
        with allure.step("Открываем главную страницу"):
            page.open()
        with allure.step("Кликаем на «Лента Заказов»"):
            page.click_orders_feed()
        assert "feed" in page.get_current_url()

    @allure.title("Открытие модального окна ингредиента")
    def test_ingredient_modal_opens(self, driver):
        page = MainPage(driver)
        with allure.step("Открываем главную страницу"):
            page.open()
        with allure.step("Закрываем куки-баннер, если есть"):
            page.close_cookie_banner()
        with allure.step("Кликаем по ингредиенту"):
            page.click_ingredient()
        assert page.find_element(MainPageLocators.MODAL_HEADER).is_displayed()

    @allure.title("Закрытие модального окна по крестику")
    def test_modal_closes(self, driver):
        page = MainPage(driver)
        with allure.step("Открываем главную страницу"):
            page.open()
        with allure.step("Кликаем по ингредиенту"):
            page.click_ingredient()
        with allure.step("Закрываем модальное окно"):
            page.close_modal()
        with allure.step("Ожидаем, что модальное окно невидимо"):
            page.wait_for_modal_invisibility()

    @allure.title("Увеличение счётчика ингредиента при добавлении")
    def test_counter_increments(self, driver):
        page = MainPage(driver)
        with allure.step("Открываем главную страницу"):
            page.open()
        with allure.step("Получаем начальное значение счётчика"):
            initial = int(page.get_ingredient_counter())
        with allure.step("Перетаскиваем ингредиент в корзину"):
            page.add_ingredient_to_basket()
        with allure.step("Ждём увеличения счётчика"):
            page.wait_for_counter_increase(initial)