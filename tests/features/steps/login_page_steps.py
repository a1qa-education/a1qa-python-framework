from behave import when, then
from pages.login_page import LoginPage
from framework.utils.env_provider import EnvProvider

@when('I log in with valid credentials')
def step_impl(context):
    login_page: LoginPage = context.page_factory.get_page(LoginPage)
    login_page.wait_for_page_to_load()
    login_page.type_username(EnvProvider.test_user())
    login_page.type_password(EnvProvider.test_password())
    login_page.click_login_button()

@then("the 'Form Authentication' page is open")
def step_impl(context):
    login_page: LoginPage = context.page_factory.get_page(LoginPage)
    login_page.wait_for_page_to_load()
    assert login_page.is_page_open() is True
