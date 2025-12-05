from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, locator, text, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click() 

    def switch_to_iframe(self, locator, timeout=10):
        """Switch to an iframe when it becomes available."""
        WebDriverWait(self.driver, timeout).until(
            EC.frame_to_be_available_and_switch_to_it(locator)
        )

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
        except TimeoutException:
            return False
        
    def is_button_disabled(self, locator):
        """Check if a button is disabled."""
        try:
            button = self.driver.find_element(*locator)
            return (not button.is_enabled()) or (button.get_attribute("disabled") is not None)
        except NoSuchElementException:
            return False

    def is_button_enabled(self, locator):
        """Check if a button is enabled."""
        try:
            button = self.driver.find_element(*locator)
            return button.is_enabled() and (button.get_attribute("disabled") is None)
        except NoSuchElementException:
            return False
        
    def get_text(self, locator, timeout=10):
        """Retrieve visible text from an element."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text
    
    def robust_click(self, locator, timeout=10):
        """
        More resilient click:
        - Waits until element is clickable
        - Scrolls into view
        - Falls back to ActionChains if normal click fails
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            # Ensure the element is scrolled into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

            try:
                element.click()
            except Exception:
                # Fallback: use ActionChains if normal click fails
                ActionChains(self.driver).move_to_element(element).click().perform()

            return element
        except TimeoutException as e:
            raise RuntimeError(f"Element {locator} not clickable") from e