from selene import browser, be, have

from reg_form_allure_jenkins import resource


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def fill_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self

    def fill_mobile_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not'
                        f'(.react-datepicker__day--outside-month)').click()
        return self

    def fill_subjects(self, value1, value2):
        browser.element('#subjectsInput').type(value1).press_enter()
        browser.element('#subjectsInput').type(value2).press_enter()
        return self

    def fill_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def upload_pic(self):
        browser.element('#uploadPicture').set_value(resource.path('pic.jpg'))
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value).press_enter()
        return self

    def fill_state(self, name):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def fill_city(self, name):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_registered_user_with(self):
        browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                'Evgenii Mif',
                'email@mail.ru',
                'Male',
                '9123456789',
                '22 August,1985',
                'Maths, English',
                'Sports',
                'pic.jpg',
                'Earth',
                'Haryana Panipat',
            )
        )
        return self

    def close_assert(self):
        browser.element('#closeLargeModal').click()
        return self
