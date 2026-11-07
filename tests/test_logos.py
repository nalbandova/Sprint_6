import allure

from urls import BASE_URL, DZEN_URL_PART


@allure.feature("Логотипы")
class TestLogos:
    @allure.title("Логотип Самоката ведёт на главную страницу")
    def test_scooter_logo(self, main_page):
        main_page.click_order("top")
        main_page.click_scooter_logo()
        assert main_page.is_home_page()
        assert main_page.get_current_url().rstrip("/") == BASE_URL.rstrip("/")

    @allure.title("Логотип Яндекса открывает Дзен в новом окне")
    def test_yandex_logo(self, main_page):
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        assert main_page.wait_url_contains(DZEN_URL_PART)
    