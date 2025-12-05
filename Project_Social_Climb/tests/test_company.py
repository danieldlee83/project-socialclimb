
def test_links_visible(main_page, company_page):
    """
    Verify that all key 'Company' section links are visible
    after navigating from the main page.
    """
    main_page.click_company_link()
    assert company_page.is_link_visible("about")
    assert company_page.is_link_visible("careers")
    assert company_page.is_link_visible("leadership")
    assert company_page.is_link_visible("mentions")