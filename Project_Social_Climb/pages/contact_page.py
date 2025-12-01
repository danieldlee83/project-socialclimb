from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID,"1067063_134998pi_1067063_134998")
        self.last_name_input = (By.ID,"1067063_135001pi_1067063_135001")
        self.email_input = (By.ID,"1067063_135004pi_1067063_135004")
        self.phone_input = (By.ID,"1067063_135007pi_1067063_135007")
        self.company_url_input = (By.ID,"1067063_135010pi_1067063_135010")
        self.social_climb_input = (By.ID,"1067063_135013pi_1067063_135013")
        self.submit_button = (By.CSS_SELECTOR, "#pardot-form input[type='submit']")
        self.error_message = (By.CSS_SELECTOR, "p.errors")
        self.iframe_locator = (By.CSS_SELECTOR, "iframe[src*='info.socialclimb.com']")

    def switch_to_iframe(self):
        """Switch to the contact form iframe when it becomes available."""
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(self.iframe_locator)
        )

    def _enter_text(self, locator, text, timeout=10):
        """Helper to enter text into a field after waiting for visibility."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def enter_first_name(self, first_name): self._enter_text(self.first_name_input, first_name)

    def enter_last_name(self, last_name): self._enter_text(self.last_name_input, last_name)

    def enter_email(self, email): self._enter_text(self.email_input, email)

    def enter_phone(self, phone): self._enter_text(self.phone_input, phone)

    def enter_company_url(self, company_url): self._enter_text(self.company_url_input, company_url)

    def enter_referral_source(self, text): self._enter_text(self.social_climb_input, text)
    
    def click_submit_button(self, timeout=10):
        """Click the submit button when it becomes clickable."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.submit_button)
            ).click()
        except Exception as e:
            raise RuntimeError("Submit button not clickable") from e

