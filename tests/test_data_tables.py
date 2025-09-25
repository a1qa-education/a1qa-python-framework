from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from pages.data_tables_page import DataTablesPage
from pages.main_page import MainPage

EXPECTED_DUE_VALUE = 251.00

class TestDataTables:

    def test_data_table(self, browser: Browser):
        browser.open_url(TEST_APP_URL)

        main_page = MainPage(browser.page)
        main_page.click_navigation_link("Sortable Data Tables")

        data_tables_page = DataTablesPage(browser.page)
        table1_content = data_tables_page.get_table1_content()

        total_due = data_tables_page.get_total_due_value(table1_content)
        assert total_due == EXPECTED_DUE_VALUE, f"Expected Due amount: {EXPECTED_DUE_VALUE}, Actual: {total_due}"
