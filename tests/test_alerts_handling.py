import pytest

from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from pages.js_alerts_page import JavaScriptAlertsPage
from pages.main_page import MainPage


SUCCESS_ALERT_MSG = "You successfully clicked an alert"


@pytest.mark.alerts
class TestAlertsHandling:

    def test_alerts_handling(self, browser: Browser):
        browser.dialog.register_dialog_handler(browser.dialog.accept)

        browser.open_url(TEST_APP_URL)

        # Navigate to 'JavaScript Alerts':

        js_alerts_page = JavaScriptAlertsPage(browser.page)
        js_alerts_page.trigger_js_alert()

        # Add assertion to check successful message:
