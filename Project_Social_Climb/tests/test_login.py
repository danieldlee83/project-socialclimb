from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service())
    driver.maximize_window()
    driver.get("https://socialclimb.com/")
    driver.delete_all_cookies()
    yield driver
    driver.delete_all_cookies()
    driver.quit()

def test_login_sign_in_button_is_disabled(driver, main_page, login_page):
    """
    Verify that the sign-in button remains disabled
    when the 'I'm not a robot' checkbox is not checked.
    """
    main_page.click_login_link()

    assert "SocialClimb" in driver.title

    login_page.enter_username("test@example.com")
    login_page.enter_password("testexample")

    assert login_page.is_sign_in_button_disabled()

def test_login_forgot_password_link_works(driver, main_page, login_page):
    """
    Verify that the 'Forgot Password' link navigates to the reset page,
    enables the reset button after entering an email,
    and allows returning to the login page.
    """
    main_page.click_login_link()
    login_page.click_forgot_password()
    
    assert WebDriverWait(driver, 5).until(EC.url_to_be("https://app.socialclimb.com/forgot"))
    
    login_page.enter_email("test@example.com")

    assert login_page.is_send_reset_link_button_enabled()

    login_page.click_go_back_to_login()

    assert WebDriverWait(driver, 5).until(EC.url_to_be("https://app.socialclimb.com/login"))

    
    

