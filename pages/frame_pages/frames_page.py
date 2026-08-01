from playwright.sync_api import Page
from framework.ui.elements.button import Button
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage

class FramesPage(BasePage):
    def __init__(self, page: Page):
        unique_element = Label(page, page.get_by_role('heading', name='Frames'), 'Frames page unique element')
        super().__init__(page, unique_element, 'Frames Page')
        self._nested_frames_button = Button(page, page.get_by_role('link', name='Nested Frames'), 'Nested Frames button')

    def click_nested_frames_button(self):
        self._nested_frames_button.click()
