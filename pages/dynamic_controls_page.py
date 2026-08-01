from playwright.sync_api import Page

from framework.ui.constants.elements import LocatorTemplates
from framework.ui.elements.button import Button
from framework.ui.elements.input import Input
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage


class DynamicControlPage(BasePage):

    def __init__(self, page: Page):
        unique_element = Label(page, page.get_by_text("Dynamic Controls", exact=True), "Dynamic Controls Page Header")
        super().__init__(page, unique_element, "Dynamic Controls page")

        self._enable_btn = Button(page, page.get_by_role("button", name="Enable"), "Enable button")
        self._input_field = Input(page, page.get_by_role("textbox"), "Input field")

    # Implement all DynamicControlPage methods:
