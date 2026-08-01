from typing import Dict, List

from playwright.sync_api import Page

from framework.ui.decorators.decorators import step
from framework.ui.elements.label import Label
from framework.ui.elements.table import Table
from framework.ui.pages.base_page import BasePage


CURRENCY_SYMBOL = "$"


class DataTablesPage(BasePage):

    def __init__(self, page: Page):
        # Change call of super() constructor to appropriate one:
        unique_element = Label(page, page.get_by_text("Data Tables", exact=True), "Data Tables Header")
        super().__init__(page, unique_element, "Data Tables Page")

        self._table_1 = Table(page, page.locator("table#table1"), "Table 1")

    @step("Get Due column values")
    def get_due_column_values(self) -> List[str]:
        # Return list of values in Due column from the table:
        pass
