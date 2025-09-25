from playwright.sync_api import Page

from framework.ui.constants.elements import LocatorTemplates
from framework.ui.elements.button import Button
from framework.ui.elements.input import Input
from framework.ui.pages.base_page import BasePage


class DynamicControlPage(BasePage):

    def __init__(self, page: Page):
        header_locator = page.locator('h4:has-text("Dynamic Controls")')
        super().__init__(page, header_locator, "Dynamic Controls page")

        self._enable_btn = Button(page, LocatorTemplates.BUTTON_BY_TEXT.format(text="Enable"), "Enable button")
        self._input_field = Input(page, "#input-example input", "Input field")

    # Implement all DynamicControlPage methods:
