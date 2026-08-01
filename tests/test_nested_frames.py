import pytest
from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from pages.main_page import MainPage
from pages.frame_pages.frames_page import FramesPage
from pages.frame_pages.nested_frames_page import NestedFramesPage

LEFT_FRAME_TEXT = 'LEFT'
RIGHT_FRAME_TEXT = 'RIGHT'

class TestNestedFrames:

    @pytest.mark.frames
    def test_interact_with_text_in_nested_frame(self, browser: Browser):
        browser.open_url(TEST_APP_URL)
        
        main_page = MainPage(browser.page)
        main_page.click_navigation_link('Frames')

        frames_page = FramesPage(browser.page)
        frames_page.click_nested_frames_button()

        nested_frames_page = NestedFramesPage(browser.page)

        # Implement checks for left and right frame text
