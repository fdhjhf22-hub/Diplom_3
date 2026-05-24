import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        drv = webdriver.Firefox(service=service)
    else:
        service = ChromeService(ChromeDriverManager().install())
        drv = webdriver.Chrome(service=service)
    drv.maximize_window()
    yield drv
    drv.quit()