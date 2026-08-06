# a1qa Python Playwright Framework

This repository contains a test automation framework built with **Playwright** and **Python (Pytest)**. It is designed for scalability, stability, and strict test isolation, architecturally aligned with the JS Playwright and Aquality frameworks, utilizing a custom **Browser Wrapper** and a rigorous implementation of the **Page Object Model (POM)**.

---

## 🚀 Features

* **Playwright Native:** Fast, reliable execution using the official Playwright Python bindings.
* **Strict Page Object Model:** Enforces absolute encapsulation of locators and state.
* **Element Wrappers:** Custom classes (`Button`, `Input`, `Label`, `Table`) that encapsulate **Playwright native locators**, reliable waits, and strict-mode error handling.
* **Smart Isolation:** Uses **Pytest Fixtures** (via `conftest.py`) to guarantee every test runs in a clean environment.
* **Secure Secrets Management:** Centralized environment variable validation via `EnvProvider` prevents hardcoded credentials and silent failures.
* **Robust Configuration:** Safe test data is loaded via `ConfigParser` and configuration JSONs.

---

## 🏗️ Project Structure

The project strictly separates the reusable technical core (`framework/`) from the business logic and tests (`tests/`).

```text
a1qa-python-framework/
├── configs/                 # Configuration files (settings.py, test_data.json)
├── framework/               # Core Technical Framework
│   ├── logger/              # Custom logging implementation
│   ├── ui/
│   │   ├── browser/         # Browser wrapper (Single state manager)
│   │   ├── constants/       # ElementType, Timeouts
│   │   ├── decorators/      # @step and @action logging decorators
│   │   ├── elements/        # UI Element wrappers (Button, Input, Label, Table, etc.)
│   │   └── pages/           # BasePage class
│   └── utils/               # ConfigParser, EnvProvider, file utils
├── pages/                   # Application-Specific Page Objects
├── tests/                   # Application-Specific Test Scripts
├── conftest.py              # Pytest fixtures and browser initialization
├── pytest.ini               # Pytest configuration and markers
├── .env.example             # Template for required environment variables
└── requirements.txt         # Project dependencies
```

---

## 🔒 Environment Setup (Secrets Management)

This framework strictly prohibits committing sensitive passwords or credentials to the repository. Instead, it relies on local environment variables.

Before running the tests for the first time, every developer/student must configure their local environment:

1. Locate the `.env.example` file in the root directory.
2. Duplicate this file and rename the copy to `.env` (this file is ignored by Git and will remain safely on your local machine).
3. Open your new `.env` file and populate it with the actual credentials required for the test environments:

```env
TEST_USER=test
TEST_PASSWORD=test

BASIC_AUTH_USER=test
BASIC_AUTH_PASSWORD=test
```

If you forget to set this up or miss a variable, the framework's `EnvProvider` will explicitly halt test execution and warn you to check your `.env` file.

---

## 📜 Strict Page Object Rules

This framework mandates a strict, classic approach to the Page Object pattern to ensure maximum stability and zero "flakiness". All contributors must adhere to the following rules:

1. **Selector Isolation:** All interactions with locators and selectors must happen exclusively inside Page classes. Tests must never contain `page.locator()` or `page.get_by...`.
2. **Inheritance:** Every application page class must inherit directly from `BasePage`.
3. **Unique Page Elements:** A unique element (`BaseElement` instance, usually a `Label`) must be passed to the `super().__init__()` constructor of every Page class. This element is used internally by `is_page_open()` to robustly verify the page state.
4. **Encapsulated Locators:** Locators must never be exposed directly as class properties. They must be wrapped inside custom Element classes (e.g., `self._login_btn = Button(...)`) and kept private by using a leading underscore (`_`).
5. **Action-Oriented Methods:** Page classes should expose methods that represent user actions (e.g., `type_username(name)`, `click_login()`).
6. **No Assertions in Pages:** Page methods must never contain test assertions (`assert` inside Page classes). All assertions belong in the test file.

---

## 📚 Developer Guide

### 1. Creating a Page Object
Follow the strict rules above when creating a new page.

```python
from playwright.sync_api import Page
from framework.ui.elements.button import Button
from framework.ui.elements.input import Input
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        # Rule 3: Pass a unique wrapped element to super()
        unique_element = Label(page, page.get_by_role('heading', name='Login'), 'Unique header')
        super().__init__(page, unique_element, 'Login Page')

        # Rule 1 & 4: Keep locators isolated and encapsulated
        self._username_input = Input(page, page.get_by_label('Username'), 'Username input')
        self._login_button = Button(page, page.get_by_role('button', name='Login'), 'Login button')
        self._error_message = Label(page, page.locator('.error'), 'Error message')

    # Rule 5: Methods represent clear user actions
    def login(self, username: str, password: str):
        self._username_input.type_text(username)
        # Password logic...
        self._login_button.click()

    # Rule 6: No assertions (assert) here. We only return the value.
    def get_error_text(self) -> str:
        self._error_message.state.wait_for_displayed()
        return self._error_message.get_text()
```

### 2. Writing a Test
Tests manage the flow and hold all assertions.

```python
import pytest
from framework.ui.browser.browser import Browser
from pages.login_page import LoginPage
from framework.utils.env_provider import EnvProvider

class TestLogin:

    @pytest.mark.demo
    def test_user_can_see_error_on_invalid_login(self, browser: Browser):
        # Rule 1: No locators here. We interact only with the Page Object.
        login_page = LoginPage(browser.page)

        # Verify page is open
        login_page.wait_for_page_to_load()
        assert login_page.is_page_open() is True

        # Use EnvProvider for sensitive data injected from .env
        login_page.login(EnvProvider.get_test_user(), EnvProvider.get_test_password())

        # Assertions are kept in the test
        error_text = login_page.get_error_text()
        assert error_text == "Invalid credentials!"
```

### 3. Working with iFrames
To interact with nested frames, you can chain native Playwright `frame_locator()` calls to target your element, and then wrap that locator in a standard Element wrapper inside your Page Object.

```python
from playwright.sync_api import Page
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage

class NestedFramesPage(BasePage):
    def __init__(self, page: Page):
        # ... super call ...
        
        # Target an element deeply nested in frames using frame_locator chaining
        self._left_frame_label = Label(
            page, 
            page.frame_locator('frame[name="frame-top"]').frame_locator('frame[name="frame-left"]').locator('body'), 
            'Left Frame label'
        )
```

---

## ⚙️ Test Execution

**Install requirements and activate environment:**
```sh
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

**Run all tests:**
```sh
pytest
```

**Run tests using markers (e.g. demo, frames, windows):**
```sh
pytest -m demo
```

**Run tests with different configurations (e.g. headless, specific browser):**
By default, tests run in headed mode. To run in headless or change the browser, use the custom flags defined in `conftest.py`:
```sh
pytest --browser=firefox --headless
```

## Useful Links

- [Pytest Documentation](https://docs.pytest.org/en/latest/)
- [Playwright Python Documentation](https://playwright.dev/python/docs/intro)