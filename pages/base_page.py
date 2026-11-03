import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    def scroll_to(self, locator):
        element = self.wait_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        return element

    @allure.step("Клик по элементу")
    def click(self, locator):
        element = self.scroll_to(locator)
        self.wait_clickable(locator).click()
        return element

    @allure.step("Ввод текста")
    def type_text(self, locator, text):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_visible(locator).text

    def is_visible(self, locator):
        return self.wait_visible(locator).is_displayed()
