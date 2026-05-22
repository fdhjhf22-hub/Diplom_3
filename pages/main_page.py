from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import BASE_PAGE_URL

class MainPage(BasePage):
    def open(self):
        self.driver.get(BASE_PAGE_URL)

    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_orders_feed(self):
        self.click_element(MainPageLocators.ORDERS_FEED_BUTTON)

    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT)

    def close_modal(self):
        self.click_element(MainPageLocators.CLOSE_MODAL_BUTTON)

    def get_ingredient_counter(self):
        return self.find_element(MainPageLocators.INGREDIENT_COUNTER).text

    def get_total_counter(self):
        return self.find_element(MainPageLocators.TOTAL_COUNTER).text

    def get_daily_counter(self):
        return self.find_element(MainPageLocators.DAILY_COUNTER).text

    def is_order_in_progress(self, order_id):
        return order_id in self.find_element(MainPageLocators.IN_PROGRESS_SECTION).text

    def add_ingredient_to_basket(self):
        ingredient = self.find_element(MainPageLocators.INGREDIENT)
        basket = self.find_element(MainPageLocators.BASKET)
        self.driver.execute_script("""
            var src = arguments[0];
            var tgt = arguments[1];
            var dt = new DataTransfer();
            src.dispatchEvent(new DragEvent('dragstart', { dataTransfer: dt, bubbles: true }));
            tgt.dispatchEvent(new DragEvent('dragover', { dataTransfer: dt, bubbles: true }));
            tgt.dispatchEvent(new DragEvent('drop', { dataTransfer: dt, bubbles: true }));
            src.dispatchEvent(new DragEvent('dragend', { dataTransfer: dt, bubbles: true }));
        """, ingredient, basket)

    def wait_for_counter_increase(self, initial):
        WebDriverWait(self.driver, 10).until(
            lambda d: int(self.get_ingredient_counter()) > initial
        )

    def close_cookie_banner(self):
        try:
            cookie_btn = self.find_element(MainPageLocators.COOKIE_BUTTON)
            cookie_btn.click()
        except:
            pass