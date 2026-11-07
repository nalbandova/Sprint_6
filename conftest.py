import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.order_page import OrderPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open()
    page.accept_cookies()
    return page

@pytest.fixture
def order_page(driver):
    return OrderPage(driver)
