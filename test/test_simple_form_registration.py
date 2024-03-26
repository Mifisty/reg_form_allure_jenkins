from reg_form_allure_jenkins.data import users
from reg_form_allure_jenkins.model.application import app
from reg_form_allure_jenkins.model.pages.registration_simple_form import SimpleRegistration


def test_simple_registration_form():
    simple_registration_page = SimpleRegistration()
    student = users.student

    simple_registration_page.open()
    simple_registration_page.fill_reg_user(student)
    simple_registration_page.should_simple_registered_user(student)


def test_simpl_app():
    student = users.student
    app.panel.open_simple_registration_form()
    app.simple_registration.fill_reg_user(student)
    app.simple_registration.should_simple_registered_user(student)
