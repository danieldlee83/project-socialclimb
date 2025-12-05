from selenium.webdriver.common.by import By
from Project_Social_Climb.pages.base_page import BasePage

class CompanyPage(BasePage):
    """
    Page Object representing the 'Company' section of SocialClimb's website.
    Provides methods to interact with and validate the presence of key links.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.links = {
            "about": (By.CSS_SELECTOR, "a[href='https://socialclimb.com/about/']"),
            "careers": (By.CSS_SELECTOR, "a[href='https://socialclimb.com/careers/']"),
            "leadership": (By.CSS_SELECTOR, "a[href='https://socialclimb.com/leadership/']"),
            "mentions": (By.CSS_SELECTOR, "a[href='https://socialclimb.com/blog/category/awards-announcements-mentions/']")
        }

    def is_link_visible(self, name):
        return self.is_link_displayed(self.links[name])

