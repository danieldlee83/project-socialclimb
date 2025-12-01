from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.solution_link = (By.LINK_TEXT, "Solutions")
        self.features_link = (By.LINK_TEXT, "Features")
        self.resources_link = (By.LINK_TEXT, "Resources")
        self.company_link = (By.LINK_TEXT, "Company")
        self.contact_link = (By.LINK_TEXT, "Contact")
        self.blog_link = (By.LINK_TEXT, "Blog")
        self.login_link = (By.LINK_TEXT, "Login")

    def click_solutions_link(self): 
        """Click the 'Solutions' link on the main page."""
        self._click(self.solution_link)

    def click_features_link(self): self._click(self.features_link)

    def click_resources_link(self): self._click(self.resources_link)

    def click_company_link(self): self._click(self.company_link)

    def click_contact_link(self): self._click(self.contact_link)

    def click_blog_link(self): self._click(self.blog_link)

    def click_login_link(self): self._click(self.login_link)

    def _click(self, locator, timeout=10):
        """Wait until the element is clickable, then click it."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            return element
        except Exception as e:
            raise RuntimeError(f"Element {locator} not clickable") from e


