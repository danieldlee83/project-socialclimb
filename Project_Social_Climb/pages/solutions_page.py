from selenium.webdriver.common.by import By
from Project_Social_Climb.pages.base_page import BasePage

class SolutionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.pe_funded_practices_link = (By.CSS_SELECTOR, "a[href='https://socialclimb.com/marketing-software-pe-funded/']")
        self.hospital_groups_link = (By.CSS_SELECTOR, "a[href='https://socialclimb.com/marketing-software-hospital-groups/']")
        self.independent_practices_link = (By.CSS_SELECTOR, "a[href='https://socialclimb.com/marketing-software-independent-practices/']")
        self.fqhc_practices_link = (By.CSS_SELECTOR, "a[href='https://socialclimb.com/marketing-software-fqhc/']")
        self.marketing_agencies_link = (By.CSS_SELECTOR,"a[href='https://socialclimb.com/marketing-software-agencies/']")
        self.pe_funded_practices_label = (By.CSS_SELECTOR, "#mega-menu-item-maxmegamenu_reusable_block-2 span:first-child")
        self.hospital_groups_label = (By.CSS_SELECTOR, "#mega-menu-item-maxmegamenu_reusable_block-3 span:first-child")
        self.independent_practices_label = (By.CSS_SELECTOR, "#mega-menu-item-maxmegamenu_reusable_block-4 span:first-child")
        self.fqhc_practices_label = (By.CSS_SELECTOR, "#mega-menu-item-maxmegamenu_reusable_block-5 span:first-child")
        self.marketing_agencies_label = (By.CSS_SELECTOR, "#mega-menu-item-maxmegamenu_reusable_block-6 span:first-child")
        self.learn_more_pe_funded_practices_link = (By.CSS_SELECTOR, "a[aria-label='Learn more about PE funded marketing software']")
        self.learn_more_hospital_groups_link = (By.CSS_SELECTOR, "a[aria-label='Learn more about hospital groups marketing software']")
        self.learn_more_independent_practices_link = (By.CSS_SELECTOR, "a[aria-label='Learn more about independent practices marketing software']")
        self.learn_more_fqhc_practices_link = (By.CSS_SELECTOR, "a[aria-label='Learn more about FQHC marketing software']")
        self.learn_more_marketing_agencies_link = (By.CSS_SELECTOR, "a[aria-label='Learn more about marketing software agencies']")
        self.schedule_a_demo_link = (By.CSS_SELECTOR,".btn.btn-lg.btn-warning.mt-0.mt-lg-5, .btn.btn-lg.btn-warning")
        self.solution_link = (By.LINK_TEXT, "Solutions")

    def click_pe_funded_practices_link(self): 
        self.robust_click(self.pe_funded_practices_link)

    def click_hospital_groups_link(self): 
        self.robust_click(self.hospital_groups_link)

    def click_independent_practices_link(self): 
        self.robust_click(self.independent_practices_link)

    def click_fqhc_practices_link(self): 
        self.robust_click(self.fqhc_practices_link)

    def click_marketing_agencies_link(self): 
        self.robust_click(self.marketing_agencies_link)
    
    def click_solutions_link(self): 
        """Click the 'Solutions' link on the main page."""
        self.click(self.solution_link)

    def get_pe_funded_practices_text(self):
        return self.get_text(self.pe_funded_practices_label)

    def get_hospital_groups_text(self):
        return self.get_text(self.hospital_groups_label)

    def get_independent_practices_text(self):
        return self.get_text(self.independent_practices_label)

    def get_fqhc_practices_text(self):
        return self.get_text(self.fqhc_practices_label)

    def get_marketing_agencies_text(self):
        return self.get_text(self.marketing_agencies_label)

    def click_learn_more_pe_funded_practices_link(self): 
        self.robust_click(self.learn_more_pe_funded_practices_link)

    def click_learn_more_hospital_groups_link(self): 
        self.robust_click(self.learn_more_hospital_groups_link)

    def click_learn_more_independent_practices_link(self): 
        self.click(self.learn_more_independent_practices_link)

    def click_learn_more_fqhc_practices_link(self): 
        self.robust_click(self.learn_more_fqhc_practices_link)

    def click_learn_more_marketing_agencies_link(self): 
        self.robust_click(self.learn_more_marketing_agencies_link)

    def is_schedule_a_demo_visible(self):
        return self.is_link_displayed(self.schedule_a_demo_link)