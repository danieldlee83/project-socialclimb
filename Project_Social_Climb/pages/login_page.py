from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.CSS_SELECTOR, "#input_0")
        self.password_input = (By.CSS_SELECTOR, "#input_1")
        self.email_input = (By.CSS_SELECTOR, "#input_2")
        self.forgot_login = (By.CSS_SELECTOR, "a[href='./forgot']")
        self.sign_in_button = (By.CSS_SELECTOR, "button[aria-label='LOG IN']")
        self.send_reset_link_button = (By.CSS_SELECTOR, "button[aria-label='SEND RESET LINK']")
        self.go_back_to_login = (By.CSS_SELECTOR, "a[href='./login']")

    def enter_username(self, username): self._enter_text(self.username_input, username)
    def enter_password(self, password): self._enter_text(self.password_input, password)
    def enter_email(self, email): self._enter_text(self.email_input, email)
    def click_forgot_password(self): self._click(self.forgot_login)
    def click_go_back_to_login(self): self._click(self.go_back_to_login)

    def _enter_text(self, locator, text, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def _click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def is_sign_in_button_disabled(self):
        try:
            button = self.driver.find_element(*self.sign_in_button)
            
            return not button.is_enabled() or button.get_attribute("disabled") is not None
        except NoSuchElementException:
            return False  

    def is_send_reset_link_button_enabled(self):
        try:
            button = self.driver.find_element(*self.send_reset_link_button)
            return button.is_enabled() and button.get_attribute("disabled") is None
        except NoSuchElementException:
            return False


