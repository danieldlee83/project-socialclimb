from selenium.webdriver.common.by import By
from Project_Social_Climb.pages.base_page import BasePage

class ContactPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_input = (By.ID,"1067063_134998pi_1067063_134998")
        self.last_name_input = (By.ID,"1067063_135001pi_1067063_135001")
        self.email_input = (By.ID,"1067063_135004pi_1067063_135004")
        self.phone_input = (By.ID,"1067063_135007pi_1067063_135007")
        self.company_url_input = (By.ID,"1067063_135010pi_1067063_135010")
        self.social_climb_input = (By.ID,"1067063_135013pi_1067063_135013")
        self.submit_button = (By.CSS_SELECTOR, "#pardot-form input[type='submit']")
        self.error_message = (By.CSS_SELECTOR, "p.errors")
        self.iframe_locator = (By.CSS_SELECTOR, "iframe[src*='info.socialclimb.com']")

    def open_contact_form(self):
        self.switch_to_iframe(self.iframe_locator)

    def enter_first_name(self, first_name): 
        self.enter_text(self.first_name_input, first_name)

    def enter_last_name(self, last_name): 
        self.enter_text(self.last_name_input, last_name)

    def enter_email(self, email): 
        self.enter_text(self.email_input, email)

    def enter_phone(self, phone): 
        self.enter_text(self.phone_input, phone)

    def enter_company_url(self, company_url): 
        self.enter_text(self.company_url_input, company_url)

    def enter_referral_source(self, text): 
        self.enter_text(self.social_climb_input, text)
    
    def click_submit_button(self):
        self.click(self.submit_button)

