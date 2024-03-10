from selene import browser, be, have, by  # noqa
from reg_form_allure_jenkins.data import users
from reg_form_allure_jenkins.model.pages.registration_page_high_level import RegistrationPageHighLevel


def test_higt_registration():
    high_registration_page = RegistrationPageHighLevel()
    student = users.student

    high_registration_page.open()
    high_registration_page.fill_reg_user(student)
    high_registration_page.should_registered_user_with(student)

