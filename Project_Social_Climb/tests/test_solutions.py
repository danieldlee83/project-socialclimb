import pytest

@pytest.mark.parametrize("link_method, text_method, learn_more_method, expected_text", [
    ("click_solutions_link", "get_pe_funded_practices_text", "click_pe_funded_practices_link", "PE-Funded Practices"),
    ("click_hospital_groups_link", "get_hospital_groups_text", "click_learn_more_hospital_groups_link", "Hospital Groups"),
    ("click_independent_practices_link", "get_independent_practices_text", "click_learn_more_independent_practices_link", "Independent Practices"),
    ("click_fqhc_practices_link", "get_fqhc_practices_text", "click_learn_more_fqhc_practices_link", "FQHC Practices"),
    ("click_marketing_agencies_link", "get_marketing_agencies_text", "click_learn_more_marketing_agencies_link", "Marketing Agencies"),
])
def test_valid_solutions(main_page, solutions_page, link_method, text_method, learn_more_method, expected_text):
    main_page.click_solutions_link()
    getattr(solutions_page, link_method)()
    assert getattr(solutions_page, text_method)() == expected_text
    getattr(solutions_page, learn_more_method)()
    assert solutions_page.is_schedule_a_demo_visible()

# def test_valid_solutions_pe_funded_practices(main_page, solutions_page):
#     """
#     Verify that the 'PE-Funded Practices' solution is displayed,
#     and that clicking 'Learn More' shows the 'Schedule a Demo' option.
#     """
#     main_page.click_solutions_link()

#     assert solutions_page.get_pe_funded_practices_text() == "PE-Funded Practices"
    
#     solutions_page.click_pe_funded_practices_link()
   
#     assert solutions_page.is_schedule_a_demo_visible()


# def test_valid_solutions_hospital_groups(main_page, solutions_page):
#     """
#     Verify that the 'Hospital Groups' solution is displayed,
#     and that clicking 'Learn More' shows the 'Schedule a Demo' option.
#     """
#     main_page.click_solutions_link()
#     solutions_page.click_hospital_groups_link()

#     assert solutions_page.get_hospital_groups_text() == "Hospital Groups"

#     solutions_page.click_learn_more_hospital_group_link()
    
#     assert solutions_page.is_schedule_a_demo_visible()


# def test_valid_solutions_independent_practices(main_page, solutions_page):
#     """
#     Verify that the 'Independent Practices' solution is displayed,
#     and that clicking 'Learn More' shows the 'Schedule a Demo' option.
#     """
#     main_page.click_solutions_link()
#     solutions_page.click_independent_practices_link()

#     assert solutions_page.get_independent_practices_text() == "Independent Practices"

#     solutions_page.click_learn_more_independent_practices_link()

#     assert solutions_page.is_schedule_a_demo_visible()


# def test_valid_solutions_fqhc_practices(main_page, solutions_page):
#     """
#     Verify that the 'FQHC Practices' solution is displayed,
#     and that clicking 'Learn More' shows the 'Schedule a Demo' option.
#     """
#     main_page.click_solutions_link()
#     solutions_page.click_fqhc_practices_link()

#     assert solutions_page.get_fqhc_practices_text() == "FQHC Practices"

#     solutions_page.click_learn_more_fqhc_practices_link()
    
#     assert solutions_page.is_schedule_a_demo_visible()


# def test_valid_solutions_marketing_agencies(main_page, solutions_page):
#     """
#     Verify that the 'Marketing Agencies' solution is displayed,
#     and that clicking 'Learn More' shows the 'Schedule a Demo' option.
#     """
#     main_page.click_solutions_link()
#     solutions_page.click_marketing_agencies_link()
    
#     assert solutions_page.get_marketing_agencies_text() == "Marketing Agencies"

#     solutions_page.click_learn_more_marketing_agencies_link()

#     assert solutions_page.is_schedule_a_demo_visible()