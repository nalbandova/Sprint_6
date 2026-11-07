import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from urls import BASE_URL


class MainPage(BasePage):
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")
    ORDER_BUTTONS = {"top": ORDER_BUTTON_TOP, "bottom": ORDER_BUTTON_BOTTOM}
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")
    HOME_HEADER = (By.XPATH, "//div[contains(@class,'Home_Header')]")
    QUESTION = (By.ID, "accordion__heading-{}")
    ANSWER = (By.ID, "accordion__panel-{}")

    @allure.step("Открыть главную страницу")
    def open(self):
        self.open_url(BASE_URL)

    @allure.step("Принять cookies")
    def accept_cookies(self):
        self.click(self.COOKIE_BUTTON)

    @allure.step("Открыть вопрос №{index}")
    def open_question(self, index):
        self.click(self.format_locator(self.QUESTION, index))

    @allure.step("Получить текст ответа №{index}")
    def get_answer_text(self, index):
        return self.get_text(self.format_locator(self.ANSWER, index))

    @allure.step("Нажать кнопку «Заказать» ({position})")
    def click_order(self, position):
        self.click(self.ORDER_BUTTONS[position])

    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.click(self.LOGO_SCOOTER)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click(self.LOGO_YANDEX)

    @allure.step("Проверить, что открыта главная страница")
    def is_home_page(self):
        return self.is_visible(self.HOME_HEADER)
    