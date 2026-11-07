import allure
import pytest

from data import ORDER_DATA_1, ORDER_DATA_2


@allure.feature("Заказ самоката")
class TestOrder:
    @allure.title("Позитивный сценарий заказа")
    @pytest.mark.parametrize(
        "position, data",
        [("top", ORDER_DATA_1), ("bottom", ORDER_DATA_2)],
        ids=["top_button", "bottom_button"],
    )
    def test_order_flow(self, main_page, order_page, position, data):
        main_page.click_order(position)
        order_page.fill_first_step(data)
        order_page.fill_second_step(data)
        order_page.submit_order()
        assert order_page.is_success_shown()
        