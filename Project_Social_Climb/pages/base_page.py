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


    # If you value readability in tests
    # def _get_button_state(self, locator):
    #     """Return True if button is enabled, False if disabled, None if not found."""
    #     try:
    #         button = self.driver.find_element(*locator)
    #         return button.is_enabled() and (button.get_attribute("disabled") is None)
    #     except NoSuchElementException:
    #         return None

    # def is_button_enabled(self, locator):
    #     state = self._get_button_state(locator)
    #     return state is True

    # def is_button_disabled(self, locator):
    #     state = self._get_button_state(locator)
    #     return state is False
     
    # If you value DRY code
    def is_button_state(self, locator, enabled=True):
        """
        Check if a button is enabled or disabled.
        Args:
            locator (tuple): Selenium locator for the button.
            enabled (bool): True to check if enabled, False to check if disabled.
        Returns:
            bool: True if the button matches the expected state, False otherwise.
        """
        try:
            button = self.driver.find_element(*locator)
            state = button.is_enabled() and (button.get_attribute("disabled") is None)
            return state if enabled else not state
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