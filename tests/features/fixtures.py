import shutil
from pathlib import Path

from behave import fixture

from framework.utils.config_parser import get_config_value

PROJECT_ROOT_DIR = Path(__file__).parent.parent.parent.resolve()


def get_download_dir(test_config: dict) -> Path:
    download_dir = get_config_value(test_config, "download_dir", default="downloads")
    return PROJECT_ROOT_DIR.joinpath(download_dir).resolve()


def get_file_for_upload(test_config: dict) -> Path:
    file_name = get_config_value(test_config, "file_for_upload")
    resource_dir = get_config_value(test_config, "source_dir", default="tests/resources")
    file_path = PROJECT_ROOT_DIR.joinpath(resource_dir, file_name).resolve()
    if not file_path.is_file():
        raise FileNotFoundError(f"File for upload not found: {file_path}")
    return file_path


@fixture
def register_dialog_handler(context):
    context.browser.dialog.register_dialog_handler(context.browser.dialog.accept)
    yield


@fixture
def cleanup_download_dir(context, **kwargs):
    download_dir = get_download_dir(context.test_config)
    shutil.rmtree(download_dir, ignore_errors=True)
    context.download_dir = download_dir
    yield download_dir
    shutil.rmtree(download_dir, ignore_errors=True)
