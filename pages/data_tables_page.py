from typing import Dict, List

from playwright.sync_api import Page

from framework.ui.decorators.decorators import step
from framework.ui.elements.table import Table
from framework.ui.pages.base_page import BasePage


CURRENCY_SYMBOL = "$"


class DataTablesPage(BasePage):

    def __init__(self, page: Page):
        # Change call of super() constructor to appropriate one:
        super().__init__()

        self._table_1 = Table(page, "table#table1", "Table 1")

    @step("Wait for table 1 to be visible and parse its content")
    def get_table1_content(self) -> List[Dict[str, str]]:
        self._table_1.state.wait_for_displayed()

        # Return list of table contents:


    @step("Calculate the total value in the Due column")
    def get_total_due_value(self, content: List[Dict[str, str]]) -> float:
        # Calculate and return sum of values in Due column from the table content:
        pass
