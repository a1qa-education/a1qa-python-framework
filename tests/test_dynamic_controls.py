from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from framework.utils import string_utils
from pages.dynamic_controls_page import DynamicControlPage
from pages.main_page import MainPage


class TestDynamicControls:

    def test_dynamic_controls(self, browser: Browser):
        browser.open_url(TEST_APP_URL)

        main_page = MainPage(browser.page)
        main_page.click_navigation_link("Dynamic Controls")

        dynamic_controls_page = DynamicControlPage(browser.page)

        dynamic_controls_page.enable_input_field()
        assert dynamic_controls_page.is_input_enabled(), "Input field is not enabled"

        random_text = string_utils.generate_random_string()
        dynamic_controls_page.enter_text_into_input(random_text)

        input_value = dynamic_controls_page.get_input_value()
        assert input_value == random_text, f"Expected '{random_text}', but got '{input_value}'"
