from selenium.webdriver.common.by import By
from Project_Social_Climb.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.solution_link = (By.LINK_TEXT, "Solutions")
        self.features_link = (By.LINK_TEXT, "Features")
        self.resources_link = (By.LINK_TEXT, "Resources")
        self.company_link = (By.LINK_TEXT, "Company")
        self.contact_link = (By.LINK_TEXT, "Contact")
        self.blog_link = (By.LINK_TEXT, "Blog")
        self.login_link = (By.LINK_TEXT, "Login")

    def click_solutions_link(self): 
        self.click(self.solution_link)

    def click_features_link(self): 
        self.click(self.features_link)

    def click_resources_link(self): 
        self.click(self.resources_link)

    def click_company_link(self): 
        self.click(self.company_link)

    def click_contact_link(self): 
        self.click(self.contact_link)

    def click_blog_link(self): 
        self.click(self.blog_link)

    def click_login_link(self): 
        self.click(self.login_link)


