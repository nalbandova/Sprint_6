import allure
from selenium.webdriver.common.by import By

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

    METRO_OPTION = (By.XPATH, "//div[contains(@class,'Order_Text')][text()='{}']")
    RENTAL_OPTION = (By.XPATH, "//div[contains(@class,'Dropdown-option')][text()='{}']")
    COLOR_CHECKBOX = (By.ID, "{}")

    @allure.step("Заполнить первую часть формы заказа")
    def fill_first_step(self, data):
        self.type_text(self.NAME, data["name"])
        self.type_text(self.SURNAME, data["surname"])
        self.type_text(self.ADDRESS, data["address"])
        self.click(self.METRO)
        self.click(self.format_locator(self.METRO_OPTION, data["metro"]))
        self.type_text(self.PHONE, data["phone"])
        self.click(self.NEXT_BUTTON)

    @allure.step("Заполнить вторую часть формы заказа")
    def fill_second_step(self, data):
        self.type_text(self.DATE, data["date"])
        self.press_enter(self.DATE)
        self.click(self.RENTAL_DROPDOWN)
        self.click(self.format_locator(self.RENTAL_OPTION, data["period"]))
        self.click(self.format_locator(self.COLOR_CHECKBOX, data["color"]))
        self.type_text(self.COMMENT, data["comment"])

    @allure.step("Оформить заказ")
    def submit_order(self):
        self.click(self.ORDER_BUTTON)
        self.click(self.CONFIRM_BUTTON)

    @allure.step("Проверить, что появилось окно об успешном заказе")
    def is_success_shown(self):
        return self.is_visible(self.SUCCESS_MODAL)
    