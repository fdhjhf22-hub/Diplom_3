from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_current_url(self):
        return self.driver.current_url

    def execute_script(self, script, *args):
        self.driver.execute_script(script, *args)

    def wait_for_invisibility(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))