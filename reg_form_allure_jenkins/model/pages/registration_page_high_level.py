import allure
from selene import browser, be, by, have, command  # noqa

from reg_form_allure_jenkins import resource
from reg_form_allure_jenkins.data.users import User


class RegistrationPageHighLevel:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.mobile_number = browser.element('#userNumber')
        self.birth = browser.element('#dateOfBirthInput')
        self.birth_day = browser
        self.birth_month = browser.element('.react-datepicker__month-select')
        self.birth_year = browser.element('.react-datepicker__year-select')
        self.subj = browser.element('#subjectsInput')
        self.hobbies = browser.all('.custom-checkbox')
        self.upload = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.state2 = browser.all('[id^=react-select][id*=option]')
        self.city = browser.element('#city')
        self.city2 = browser.all('[id^=react-select][id*=option]')
        self.submit = browser.element('#submit')

    @allure.step('open registration form')
    def open(self):
        browser.open('/automation-practice-form')
        return self

    @allure.step('fill registration user')
    def fill_reg_user(self, user: User):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.email.type(user.email)
        self.gender.element_by(have.value(user.gender)).element('..').click()
        self.mobile_number.type(user.number)
        self.birth.click()
        self.birth_month.type(user.birth_month)
        self.birth_year.type(user.birth_year)
        self.birth_day.element(
            f'.react-datepicker__day--0{user.birth_day}:not'
            f'(.react-datepicker__day--outside-month)').click()
        self.subj.click().type(user.subjects).press_enter().type(user.subjects2).press_enter()
        self.hobbies.element_by(have.exact_text(user.hobbies)).click()
        self.upload.set_value(resource.path('pic.jpg'))
        self.current_address.type(user.address)
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        self.state2.element_by(have.exact_text(user.state)).click()
        self.city.click()
        self.city2.element_by(have.exact_text(user.city)).click()
        self.submit.click()

    @allure.step('should_registered_user_with')
    def should_registered_user_with(self, user: User):
        browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                str(user.number),
                f'{user.birth_day} {user.birth_month},{user.birth_year}',
                f'{user.subjects}, {user.subjects2}',
                user.hobbies,
                'pic.jpg',
                user.address,
                f'{user.state} {user.city}',
            )
        )
        browser.element('#closeLargeModal').click()
        return self
    # def close_assert(self):
    #     browser.element('#closeLargeModal').click()
