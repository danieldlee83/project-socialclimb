from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CompanyPage:
    """
    Page Object representing the 'Company' section of SocialClimb's website.
    Provides methods to interact with and validate the presence of key links.
    """
    def __init__(self, driver):
        self.driver = driver
        self.links = {
            "about": (By.CSS_SELECTOR, "a[href='https://socialclimb.com/about/']"),
            "careers": (By.CSS_SELECTOR, "a[href='https://socialclimb.com/careers/']"),
            "leadership": (By.CSS_SELECTOR, "a[href='https://socialclimb.com/leadership/']"),
            "mentions": (By.CSS_SELECTOR, "a[href='https://socialclimb.com/blog/category/awards-announcements-mentions/']")
        }

    def click_link(self, locator, timeout=10):
        """
        Click a link after waiting until it is clickable.
        Args:
            locator (tuple): Selenium locator for the link.
            timeout (int): Maximum wait time in seconds.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def is_link_displayed(self, locator, timeout=10):
        """
        Check if a link is displayed on the page.
        Args:
            locator (tuple): Selenium locator for the link.
            timeout (int): Maximum wait time in seconds.
        Returns:
            bool: True if the link is visible, False otherwise.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element.is_displayed()
        except Exception:
            return False
