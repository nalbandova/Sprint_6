# Sprint_6: автотесты для Яндекс.Самокат

Стек: Python, Selenium, pytest, Allure. Браузер: Firefox.

## Запуск
    pip install -r requirements.txt
    pytest --alluredir=allure_results
    allure serve allure_results

## Отчёт
    allure generate allure_results -o allure-report --clean
