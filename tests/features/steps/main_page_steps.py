from behave import given
from pages.main_page import MainPage

@given('I open the "{link_name}" page')
def step_impl(context, link_name):
    main_page: MainPage = context.page_factory.get_page(MainPage)
    main_page.click_navigation_link(link_name)
