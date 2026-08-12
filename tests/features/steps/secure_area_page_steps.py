from behave import when, then
from pages.secure_area_page import SecureAreaPage

@then('the success message is displayed')
def step_impl(context):
    secure_area_page: SecureAreaPage = context.page_factory.get_page(SecureAreaPage)
    secure_area_page.wait_for_page_to_load()
    assert secure_area_page.is_page_open() is True
    
    message = secure_area_page.get_message_text()
    assert message == context.test_config.get("login_success_message")

@when('I log out')
def step_impl(context):
    secure_area_page: SecureAreaPage = context.page_factory.get_page(SecureAreaPage)
    secure_area_page.click_logout_button()
