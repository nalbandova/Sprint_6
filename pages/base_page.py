import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть адрес {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Подставить значение в локатор")
    def format_locator(self, locator, value):
        by, template = locator
        return by, template.format(value)

    @allure.step("Дождаться, пока элемент станет видимым")
    def wait_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    @allure.step("Дождаться, пока элемент станет кликабельным")
    def wait_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    @allure.step("Прокрутить страницу к элементу")
    def scroll_to(self, locator):
        element = self.wait_visible(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", element)
        return element

    @allure.step("Клик по элементу")
    def click(self, locator):
        self.scroll_to(locator)
        self.wait_clickable(locator).click()

    @allure.step("Ввод текста в поле")
    def type_text(self, locator, text):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Нажать Enter в поле")
    def press_enter(self, locator):
        self.wait_visible(locator).send_keys(Keys.ENTER)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.wait_visible(locator).text

    @allure.step("Проверить, что элемент виден")
    def is_visible(self, locator):
        return self.wait_visible(locator).is_displayed()

    @allure.step("Получить текущий адрес страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Дождаться, пока адрес содержит {part}")
    def wait_url_contains(self, part, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(part))

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        