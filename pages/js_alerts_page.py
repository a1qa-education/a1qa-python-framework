from playwright.sync_api import Page

from framework.ui.decorators.decorators import step
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage


class JavaScriptAlertsPage(BasePage):

    def __init__(self, page: Page):
        unique_element = Label(page, page.get_by_text("JavaScript Alerts", exact=True), "JavaScript Alerts Page Header")
        super().__init__(page, unique_element, "JavaScript Alerts Page")

        # Add elements to interact with:

    @step("Click the JS Alert button")
    def click_for_js_alert_button(self):
        self._js_alert_button.click()

    @step("Get displayed result message")
    def get_result_text(self) -> str:
        self._result_message_lbl.state.wait_for_displayed()
        return self._result_message_lbl.get_text()
