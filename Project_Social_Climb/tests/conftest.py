import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.main_page import MainPage
from pages.solutions_page import SolutionsPage
from pages.company_page import CompanyPage
from pages.contact_page import ContactPage
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(service=Service())
    driver.maximize_window()
    driver.get("https://socialclimb.com/")
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver): 
    return MainPage(driver)

@pytest.fixture
def solutions_page(driver):
    return SolutionsPage(driver)

@pytest.fixture
def company_page(driver):
    return CompanyPage(driver)

@pytest.fixture
def contact_page(driver):
    return ContactPage(driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)