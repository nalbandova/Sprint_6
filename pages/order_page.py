import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class OrderPage(BasePage):
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_DROPDOWN = (By.XPATH, "//div[contains(@class,'Dropdown-placeholder')]")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]/button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class,'Order_ModalHeader')][contains(text(),'Заказ оформлен')]")

    @staticmethod
    def metro_option(station):
        return (By.XPATH, f"//div[contains(@class,'Order_Text')][text()='{station}']")

    @staticmethod
    def rental_option(period):
        return (By.XPATH, f"//div[contains(@class,'Dropdown-option')][text()='{period}']")

    @staticmethod
    def color_checkbox(color):
        return (By.ID, color)

    @allure.step("Заполнить первую часть формы")
    def fill_first_step(self, data):
        self.type_text(self.NAME, data["name"])
        self.type_text(self.SURNAME, data["surname"])
        self.type_text(self.ADDRESS, data["address"])
        self.click(self.METRO)
        self.click(self.metro_option(data["metro"]))
        self.type_text(self.PHONE, data["phone"])
        self.click(self.NEXT_BUTTON)

    @allure.step("Заполнить вторую часть формы")
    def fill_second_step(self, data):
        self.type_text(self.DATE, data["date"])
        self.wait_visible(self.DATE).send_keys(Keys.ENTER)
        self.click(self.RENTAL_DROPDOWN)
        self.click(self.rental_option(data["period"]))
        self.click(self.color_checkbox(data["color"]))
        self.type_text(self.COMMENT, data["comment"])

    @allure.step("Оформить заказ")
    def submit_order(self):
        self.click(self.ORDER_BUTTON)
        self.click(self.CONFIRM_BUTTON)

    def is_success_shown(self):
        return self.is_visible(self.SUCCESS_MODAL)
