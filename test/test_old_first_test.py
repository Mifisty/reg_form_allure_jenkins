import os

import allure
from selene import browser, be, have, by, command  # noqa


def test_registration():
    # Ниже тест который был до рефакторинга в нужны вид с pageobjects
    with allure.step('open registration form page'):
        browser.open('/automation-practice-form')

    with allure.step('fill registration data'):
        browser.element('#firstName').should(be.blank).type('Evgenii')
        browser.element('#lastName').should(be.blank).type('Mif')
        browser.element('#userEmail').should(be.blank).type('email@mail.ru')
        browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
        browser.element('#userNumber').should(be.blank).type('91234567890')

        browser.element('#dateOfBirthInput').with_(timeout=browser.config.timeout * 1.5).click()
        browser.element('.react-datepicker__year-select').click().element(by.text('1985')).click()
        browser.element('.react-datepicker__month-select').click().element(by.text('August')).click()
        browser.element(
            f'.react-datepicker__day--022:not'
            f'(.react-datepicker__day--outside-month)').click()

        browser.element('#subjectsInput').type('maths').press_enter()
        browser.element('#subjectsInput').type('eng').press_enter()

        browser.element('#hobbiesWrapper > div.col-md-9.col-sm-12 > '
                        'div:nth-child(1) > label').click()

        # добавить картинку
        browser.element('#uploadPicture').send_keys(os.path.abspath('test/pic.jpg'))
        browser.element('#currentAddress').perform(command.js.scroll_into_view)
        browser.element('#currentAddress').type('Earth').press_enter()
        browser.element('#state').click()
        browser.element('#react-select-3-option-2').click()
        browser.element('#city').click()
        browser.element('#react-select-4-option-1').click()

        browser.element('#submit').click()

    # Проверка заполненности
    with allure.step('should registered user with'):
        browser.element('.modal-header').should(have.text('Thanks for submitting the form'))

        # проверяет по любоу 1 символу всю таблицу

        browser.element('.table > tbody > tr:nth-child(1)').should(have.text('Evgenii Mif'))
        browser.element('.table > tbody > tr:nth-child(2)').should(have.text('email@mail.ru'))
        browser.element('.table > tbody > tr:nth-child(3)').should(have.text('Male'))
        browser.element('.table > tbody > tr:nth-child(4)').should(have.text('9123456789'))
        browser.element('.table > tbody > tr:nth-child(5)').should(have.text('22 August,1985'))
        browser.element('.table > tbody > tr:nth-child(6)').should(have.text('Maths, English'))
        browser.element('.table > tbody > tr:nth-child(7)').should(have.text('Sports'))
        browser.element('.table > tbody > tr:nth-child(8)').should(have.text('pic.jpg'))
        browser.element('.table > tbody > tr:nth-child(9)').should(have.text('Earth'))
        browser.element('.table > tbody > tr:nth-child(10)').should(have.text('Haryana Panipat'))

        # Тест закончен закрыть окно

        browser.element('#closeLargeModal').click()
