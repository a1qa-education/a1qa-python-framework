import pytest
from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from pages.main_page import MainPage
from pages.multiple_windows_pages.new_window_page import NewWindowPage
from pages.multiple_windows_pages.open_new_window_page import OpenNewWindowPage

NEW_WINDOW_TEXT = 'New Window'

class TestMultipleWindows:

    @pytest.mark.windows
    def test_interact_with_new_window(self, browser: Browser):
        browser.open_url(TEST_APP_URL)
        
        # Implement test case
