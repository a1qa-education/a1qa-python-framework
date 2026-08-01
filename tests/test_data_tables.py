from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from pages.data_tables_page import DataTablesPage
from pages.main_page import MainPage

EXPECTED_SUM = 251.0
CURRENCY_SIGN = "$"

class TestDataTables:

    def test_sum_of_due_values_should_be_correct(self, browser: Browser):
        browser.open_url(TEST_APP_URL)

        main_page = MainPage(browser.page)
        main_page.click_navigation_link("Sortable Data Tables")

        data_tables_page = DataTablesPage(browser.page)
        
        # due_values = data_tables_page.get_due_column_values()

        # Calculate sum of elements (actual_sum) from due_values

        # assert actual_sum == EXPECTED_SUM
