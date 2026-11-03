import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage


@allure.feature("Логотипы")
class TestLogos:
    @allure.title("Логотип Самоката ведёт на главную страницу")
    def test_scooter_logo(self, main_page, driver):
        main_page.click_order(MainPage.ORDER_BUTTON_TOP)
        main_page.click(MainPage.LOGO_SCOOTER)
        assert main_page.is_home_page()
        assert driver.current_url.rstrip("/") == MainPage.URL.rstrip("/")

    @allure.title("Логотип Яндекса открывает Дзен в новом окне")
    def test_yandex_logo(self, main_page, driver):
        main_page.click_yandex_logo()
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 15).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url
