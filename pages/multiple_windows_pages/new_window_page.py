from playwright.sync_api import Page
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage

class NewWindowPage(BasePage):
    def __init__(self, page: Page):
        unique_element = Label(page, page.get_by_role("heading", name="New Window"), "New Window page unique element")
        super().__init__(page, unique_element, "New Window Page")
        self._new_window_text_lbl = Label(page, page.get_by_role("heading", name="New Window"), "New Window Text Label")
        
    def get_new_window_label_text(self) -> str:
        return self._new_window_text_lbl.get_text()
