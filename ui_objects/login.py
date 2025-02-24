# ui_objects/login_page.py

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = "username_locator"
        self.password_field = "password_locator"
        self.login_button = "login_button_locator"

    def enter_username(self, username):
        self.driver.find_element(self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(self.login_button).click()
