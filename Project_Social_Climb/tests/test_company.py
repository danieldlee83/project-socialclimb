
def test_links_visible(main_page, company_page):
    """
    Verify that all key 'Company' section links are visible
    after navigating from the main page.
    """
    main_page.click_company_link()
    
    assert company_page.is_link_displayed(company_page.links["about"]) is True
    assert company_page.is_link_displayed(company_page.links["careers"]) is True
    assert company_page.is_link_displayed(company_page.links["leadership"]) is True
    assert company_page.is_link_displayed(company_page.links["mentions"]) is True