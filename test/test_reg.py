from selene import browser, be, have, by  # noqa
from reg_form_allure_jenkins.model.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name('Evgenii')
    registration_page.fill_last_name('Mif')
    registration_page.fill_email('email@mail.ru')

    registration_page \
        .fill_gender('Male') \
        .fill_mobile_number('91234567890') \
        .fill_date_of_birth(1985, 'August', 22)
    registration_page.fill_subjects('Maths', 'eng')
    registration_page.fill_hobbies('Sports')
    registration_page.upload_pic()
    registration_page.fill_current_address('Earth')
    registration_page.fill_state('Haryana')
    registration_page.fill_city('Panipat')
    registration_page.submit()

    registration_page.should_registered_user_with()
    registration_page.close_assert()
