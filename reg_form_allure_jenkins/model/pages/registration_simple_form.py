import allure

from reg_form_allure_jenkins.data.users import User
from selene import browser, be, have


class SimpleRegistration:
    @allure.step('открываем форму регистрации')
    def open(self):
        browser.open('/text-box')
        return self

    @allure.step('заполняем регистрационные данные')
    def fill_reg_user(self, user: User):
        browser.element('#userName').should(be.blank).type(f'{user.first_name} {user.last_name}')
        browser.element('#userEmail').should(be.blank).type(user.email)
        browser.element('#currentAddress').should(be.blank).type(user.address)
        browser.element('#permanentAddress').should(be.blank).type(f'{user.state} {user.city}')
        browser.element('#submit').click()

        return self

    @allure.step('проверяем регистрационные данные')
    def should_simple_registered_user(self, user: User):
        browser.element('#name').should(have.text
                                        (f'Name:{user.first_name} {user.last_name}'))
        browser.element('#email').should(have.text
                                         (f'Email:{user.email}'))
        browser.element('#output #currentAddress').should(have.text(f'Current Address :{user.address}'))
        browser.element('#output #permanentAddress').should(have.text(f'Permananet Address :{user.state} {user.city}'))

        # pass
