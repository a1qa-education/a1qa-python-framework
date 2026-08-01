from pathlib import Path

from playwright.sync_api import Page

from framework.ui.decorators.decorators import step
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage


class FileDownloadPage(BasePage):

    def __init__(self, page: Page):
        unique_element = Label(page, page.get_by_text("File Downloader", exact=True), "File Downloader Page Header")
        super().__init__(page, unique_element, "File Downloader page")

    def get_file_link(self, file_name: str) -> Label:
        return Label(self.page, self.page.get_by_text(file_name), f"Download link for '{file_name}'")

    @step("Check if download link for file is displayed")
    def is_file_enabled(self, file_name: str) -> bool:
        file_link = self.get_file_link(file_name)
        return file_link.state.is_enabled()

    @step("Download file")
    def download_file(self, file_name: str, download_dir: Path) -> Path:
        file_link = self.get_file_link(file_name)

        with self.page.expect_download() as download_info:
            file_link.click()
        download = download_info.value

        downloaded_file_path = download_dir.joinpath(file_name)
        download.save_as(downloaded_file_path)

        return downloaded_file_path
