from reg_form_allure_jenkins.model.pages.registration_simple_form import SimpleRegistration


class LeftPanel:
    def __init__(self):
        self.simple_registration_page = SimpleRegistration()

    def open(self, first_button, second_button):
        if first_button == 'Elements' and second_button == 'Text Box':
            return self.simple_registration_page.open()

    def open_simple_registration_form(self):
        return self.open('Elements', 'Text Box')
