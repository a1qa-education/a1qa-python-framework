from pathlib import Path

import pytest

from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from framework.utils import file_utils
from pages.file_download_page import FileDownloadPage
from pages.main_page import MainPage


@pytest.mark.file_download
@pytest.mark.usefixtures("cleanup_download_dir")
class TestFileDownload:

    def test_check_that_file_downloaded(self, browser: Browser, test_file_name: str, download_dir: Path):
        # Implement test case:
        pass
