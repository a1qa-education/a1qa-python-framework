from behave import given, then, when

from pages.world_clock_page import WorldClockPage


@given('I navigate to the page "{url}"')
def step_navigate_to_page(context, url):
    context.browser.open_url(url)


@then('I press the link with name "{name}"')
def step_press_link_with_name(context, name):
    world_clock_page: WorldClockPage = context.page_factory.get_page(WorldClockPage)
    world_clock_page.personal_world_clock_button(name).click()


@then('I verify the modal with title "{title}" is opened')
def step_verify_modal_is_opened(context, title):
    world_clock_page: WorldClockPage = context.page_factory.get_page(WorldClockPage)
    world_clock_page.is_modal_opened(title)

    actual_title = world_clock_page.get_modal_title_text()
    assert actual_title == title, \
        f"Unexpected dialog was opened: expected '{title}' but was '{actual_title}'"

    city_input_value = world_clock_page.get_city_input_value()
    assert not city_input_value, f"City name field is not empty: '{city_input_value}'"


@when('I enter "{text}" into the input with id "{element_id}"')
def step_enter_city_name(context, text, element_id):
    context.added_city = text
    world_clock_page: WorldClockPage = context.page_factory.get_page(WorldClockPage)
    city_input = world_clock_page.modal_textbox(element_id)
    city_input.click()
    city_input.type_text(text)


@when('I wait {seconds:d} seconds until the suggestion list is shown')
def step_wait_for_suggestions(context, seconds):
    world_clock_page: WorldClockPage = context.page_factory.get_page(WorldClockPage)
    world_clock_page.wait_for_suggestions_displayed(seconds * 1000)


@when('I click suggestion number {number:d} in dropdown')
def step_click_suggestion(context, number):
    world_clock_page: WorldClockPage = context.page_factory.get_page(WorldClockPage)
    world_clock_page.click_suggestion_item(number)


@given('I press the modal button with text "{text}"')
def step_press_modal_button(context, text):
    world_clock_page: WorldClockPage = context.page_factory.get_page(WorldClockPage)
    world_clock_page.click_modal_button(text)


@given('word "{word}" is displayed')
def step_verify_word_is_displayed(context, word):
    world_clock_page: WorldClockPage = context.page_factory.get_page(WorldClockPage)
    assert world_clock_page.city_name_label(word).state.is_displayed(), \
        f"Word '{word}' was not displayed"

    displayed_city = world_clock_page.get_city_name_text(word)
    assert displayed_city == context.added_city, \
        f"Displayed city '{displayed_city}' does not match the added city '{context.added_city}'"
