from behave import given, then, when

from pages.city_weather_page import CityWeatherPage
from pages.constants import MainPageNavigation
from pages.main_page import MainPage
from pages.weather_page import WeatherPage


@given('I open the url "{url}"')
def step_open_url(context, url):
    context.browser.open_url(url)


@when('I click the link with text "{text}"')
def step_click_navigation_link(context, text):
    main_page: MainPage = context.page_factory.get_page(MainPage)
    main_page.click_navigation_link(MainPageNavigation.from_label(text))


@when('I verify the page title contains "{text}"')
def step_verify_page_title(context, text):
    weather_page: WeatherPage = context.page_factory.get_page(WeatherPage)
    weather_page.wait_for_page_to_load()
    weather_page.check_page_title(text)

    title = weather_page.get_title()
    assert text in title, f"Page title '{title}' does not contain '{text}'"

    url_part = context.test_config["weather_url_part"]
    current_url = context.browser.get_current_url()
    assert url_part in current_url, \
        f"Weather section was not opened: '{current_url}' does not contain '{url_part}'"


@then('I clear the input')
def step_clear_input(context):
    weather_page: WeatherPage = context.page_factory.get_page(WeatherPage)
    weather_page.search_input.clear()


@then('I type "{text}" into the input')
def step_type_into_input(context, text):
    context.searched_city = text
    weather_page: WeatherPage = context.page_factory.get_page(WeatherPage)
    weather_page.search_input.click()
    weather_page.search_input.type_text(text)


@given('I wait {seconds:d} seconds for the dropdown to appear')
def step_wait_for_dropdown(context, seconds):
    weather_page: WeatherPage = context.page_factory.get_page(WeatherPage)
    weather_page.wait_for_dropdown_apear(seconds * 1000)


@when('I click element number {number:d} in the list')
def step_click_element_by_number(context, number):
    weather_page: WeatherPage = context.page_factory.get_page(WeatherPage)
    weather_page.click_element_by_number(number)


@when('the text of element contains "{expected}"')
def step_verify_element_text(context, expected):
    city_weather_page: CityWeatherPage = context.page_factory.get_page(CityWeatherPage)
    header_text = city_weather_page.get_page_header_text()

    assert expected in header_text, \
        f"Expected headline to contain '{expected}' but was '{header_text}'"
    assert expected == context.searched_city, \
        f"Headline city '{expected}' does not match the searched city '{context.searched_city}'"
