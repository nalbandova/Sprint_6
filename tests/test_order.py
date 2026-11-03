import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from tests.data import ORDER_DATA_1, ORDER_DATA_2


@allure.feature("Заказ самоката")
class TestOrder:
    @allure.title("Позитивный сценарий заказа")
    @pytest.mark.parametrize(
        "button, data",
        [
            (MainPage.ORDER_BUTTON_TOP, ORDER_DATA_1),
            (MainPage.ORDER_BUTTON_BOTTOM, ORDER_DATA_2),
        ],
        ids=["top_button", "bottom_button"],
    )
    def test_order_flow(self, main_page, driver, button, data):
        main_page.click_order(button)
        order_page = OrderPage(driver)
        order_page.fill_first_step(data)
        order_page.fill_second_step(data)
        order_page.submit_order()
        assert order_page.is_success_shown()
