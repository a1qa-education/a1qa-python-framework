from playwright.sync_api import Page
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage

class DownloadAsPdfPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, Label(page, page.get_by_role('heading', name='Download as PDF'), 'Download as PDF page unique element'), 'Download as PDF Page')
        self.file_name_label = Label(page, page.locator('//div[@class="mw-electronpdfservice-selection-label-desc"]'), 'File name label')

    def get_file_name(self) -> str:
        return self.file_name_label.get_text()
