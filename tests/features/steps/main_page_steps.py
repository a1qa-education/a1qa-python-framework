from behave import given, when
from pages.main_page import MainPage

@given('the main page is open')
def step_impl_main_page(context):
    main_page: MainPage = context.page_factory.get_page(MainPage)
    main_page.wait_for_page_to_load()
    assert main_page.is_page_open() is True

@when('I navigate to the "{link_name}" page')
def step_impl_navigate(context, link_name):
    main_page: MainPage = context.page_factory.get_page(MainPage)
    main_page.click_navigation_link(link_name)
