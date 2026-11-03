import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")
    HOME_HEADER = (By.XPATH, "//div[contains(@class,'Home_Header')]")

    @staticmethod
    def question_locator(index):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def answer_locator(index):
        return (By.ID, f"accordion__panel-{index}")

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Принять cookies")
    def accept_cookies(self):
        self.click(self.COOKIE_BUTTON)

    @allure.step("Открыть вопрос №{index}")
    def open_question(self, index):
        self.click(self.question_locator(index))

    def get_answer_text(self, index):
        return self.get_text(self.answer_locator(index))

    @allure.step("Нажать кнопку «Заказать»")
    def click_order(self, button_locator):
        self.click(button_locator)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click(self.LOGO_YANDEX)

    def is_home_page(self):
        return self.is_visible(self.HOME_HEADER)
