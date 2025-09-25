import pytest

from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from pages.main_page import MainPage

SUCCESS_AUTH_MSG = "Congratulations! You must have the proper credentials"


@pytest.mark.basic_auth
@pytest.mark.usefixtures("set_basic_auth")
class TestBasicAuth:

    def test_basic_auth(self, browser: Browser):
        browser.open_url(TEST_APP_URL)

        main_page = MainPage(browser.page)
        main_page.click_navigation_link("Basic Auth")

        # Get auth message and assert expected result:
