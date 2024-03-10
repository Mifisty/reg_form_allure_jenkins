import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    # browser.config.timeout = 3.0                          # таймаут для операций
    # driver_options.add_argument('--headless')                 # не открывать браузер для теста
    # browser.config.click_by_js = True               #клики через джаву
    # browser.config.type_by_js = True                #текст вводится мгновенно через джава скрипт
    browser.config.driver_options = driver_options

# Отчет аллюра  - ' allure serve tests/allure-results  '