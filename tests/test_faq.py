import allure
import pytest

from data import FAQ_ANSWERS


@allure.feature("Вопросы о важном")
class TestFaq:
    @allure.title("Вопрос №{index}: при клике открывается ответ")
    @pytest.mark.parametrize("index, expected_part", FAQ_ANSWERS)
    def test_answer_opens(self, main_page, index, expected_part):
        main_page.open_question(index)
        assert expected_part in main_page.get_answer_text(index)
