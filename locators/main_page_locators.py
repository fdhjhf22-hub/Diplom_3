from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDERS_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient')]")
    MODAL_HEADER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    INGREDIENT_COUNTER = (By.XPATH, "//a[contains(@class, 'BurgerIngredient')]//p[contains(@class, 'counter__num')]")
    BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor')]")
    TOTAL_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DAILY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS_SECTION = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]")
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")
    COOKIE_BUTTON = (By.XPATH, "//button[contains(text(),'ринять')]")