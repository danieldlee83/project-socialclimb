from selenium.webdriver.common.by import By
from Project_Social_Climb.pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.CSS_SELECTOR, "#input_0")
        self.password_input = (By.CSS_SELECTOR, "#input_1")
        self.email_input = (By.CSS_SELECTOR, "#input_2")
        self.forgot_login = (By.CSS_SELECTOR, "a[href='./forgot']")
        self.sign_in_button = (By.CSS_SELECTOR, "button[aria-label='LOG IN']")
        self.send_reset_link_button = (By.CSS_SELECTOR, "button[aria-label='SEND RESET LINK']")
        self.go_back_to_login = (By.CSS_SELECTOR, "a[href='./login']")

    def enter_username(self, username): 
        self.enter_text(self.username_input, username)
    
    def enter_password(self, password): 
        self.enter_text(self.password_input, password)
    
    def enter_email(self, email): 
        self.enter_text(self.email_input, email)
    
    def click_forgot_password(self): 
        self.click(self.forgot_login)
    
    def click_go_back_to_login(self): 
        self.click(self.go_back_to_login)
    
    def click_sign_in(self):
        self.click(self.sign_in_button)

    def is_sign_in_button_disabled(self):
        return self.is_button_disabled(self.sign_in_button)

    def is_send_reset_link_button_enabled(self):
        return self.is_button_enabled(self.send_reset_link_button)

    def login(self, username, password):
        """Perform the full login flow."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_sign_in()
