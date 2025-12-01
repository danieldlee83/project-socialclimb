
def test_contact_form_fields(main_page, contact_page):
    """
    Verify that the contact form fields can be filled out correctly.
    Submission is disabled to avoid sending real data.
    """
    main_page.click_contact_link()
    contact_page.switch_to_iframe()
    contact_page.enter_first_name("Daniel")
    contact_page.enter_last_name("Lee")
    contact_page.enter_email("dlee@socialclimb.com")
    contact_page.enter_phone("18001234567")
    contact_page.enter_company_url("socialclimb.com")
    contact_page.enter_referral_source("LinkedIn")
    contact_page.driver.switch_to.default_content()
    
    # Temporarily disabled to avoid sending real submissions in test environment
    #contact_page.click_submit_button()
    #assert contact_page.is_success_message_displayed() is True




