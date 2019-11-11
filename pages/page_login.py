from selenium.webdriver.common.by import By
from pages.page import BasePage


class LoginPage(BasePage):
    url = BasePage.baseurl

    email_address_textbox = (By.XPATH, '//INPUT[@placeholder="Email address"]')
    email_right_arrow = (By.XPATH, "//DIV[@class='next-step ready']")
    password_textbox = (By.XPATH, '//INPUT[@name="password"]')
    login = (By.XPATH, '//BUTTON[text()="login"]')

    def enter_email_address(self, email_address):
        if self.wait_for_element(self.email_address_textbox):
            self.send_keys(email_address, self.email_address_textbox)
            self.click(self.email_right_arrow)

    def enter_password(self, password):
        if self.wait_for_element(self.password_textbox):
            self.send_keys(password, self.password_textbox)
            self.click(self.login)


