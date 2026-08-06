import os
import pytest
from framework.ui.browser.browser import Browser
from framework.utils import file_utils
from pages.wikipedia_main_page import WikipediaMainPage
from pages.article_page import ArticlePage
from pages.download_as_pdf_page import DownloadAsPdfPage

class TestDownloadPdf:

    @pytest.mark.demo
    def test_download_pdf(self, browser: Browser):
        browser.page.goto("https://www.wikipedia.org/")

        main_page = WikipediaMainPage(browser.page)
        main_page.select_english_language()
        main_page.type_search_request('Albert Einstein')
        main_page.search_click()

        article_page = ArticlePage(browser.page)
        article_page.click_tools_menu_button()
        article_page.click_download_as_pdf_button()

        download_as_pdf_page = DownloadAsPdfPage(browser.page)
        file_name = download_as_pdf_page.get_file_name()
        
        # Download file using Playwright natively, keeping broken pattern in test
        with browser.page.expect_download() as download_info:
            browser.page.locator('//button[@class="oo-ui-inputWidget-input oo-ui-buttonElement-button"]').click()
        download = download_info.value
        
        os.makedirs('downloads', exist_ok=True)
        file_path = f"downloads/{file_name}"
        download.save_as(file_path)
        
        assert file_utils.is_file_exist(file_path) is True
