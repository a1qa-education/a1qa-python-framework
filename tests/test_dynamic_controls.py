from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from framework.utils import string_utils
from pages.dynamic_controls_page import DynamicControlPage
from pages.main_page import MainPage


class TestDynamicControls:

    def test_check_state_of_dynamic_control(self, browser: Browser):
        browser.open_url(TEST_APP_URL)

        main_page = MainPage(browser.page)
        main_page.click_navigation_link("Dynamic Controls")

        dynamic_controls_page = DynamicControlPage(browser.page)

        # dynamic_controls_page.click_enable_button()
        # assert dynamic_controls_page.is_input_field_enabled() is True

        # random_text = string_utils.generate_random_string()
        # dynamic_controls_page.input_text_into_input_field(random_text)

        # input_value = dynamic_controls_page.get_value_from_input_field()
        # assert input_value == random_text, f"Expected '{random_text}', but got '{input_value}'"
