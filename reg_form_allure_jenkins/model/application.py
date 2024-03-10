from reg_form_allure_jenkins.model.pages.left_panel import LeftPanel
from reg_form_allure_jenkins.model.pages.registration_simple_form import SimpleRegistration


class Application:
    def __init__(self):
        self.simple_registration = SimpleRegistration()
        self.panel = LeftPanel()


app = Application()
