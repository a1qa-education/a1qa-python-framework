# Automated Testing Project

This project is designed for automated testing using Playwright and Pytest frameworks. It is architecturally aligned with the JS Playwright and Aquality frameworks.

## Project Structure

```
├── configs/                # Configuration files (settings.py, test_data.json)
├── framework/              # Core framework components
│   ├── logger/             # Custom logging implementation
│   ├── ui/                 # UI components
│   │   ├── browser/        # Browser and Window management
│   │   ├── constants/      # Timeouts, element states, etc.
│   │   ├── decorators/     # @step and @action decorators
│   │   ├── elements/       # UI element wrappers (Button, TextBox, etc.)
│   │   └── pages/          # BasePage class
│   └── utils/              # Utilities (EnvProvider, ConfigParser)
├── pages/                  # Application-specific Page Objects
├── tests/                  # Application-specific Test Scripts
├── conftest.py             # Pytest fixtures and browser initialization
└── pytest.ini              # Pytest configuration and markers
```

## Installing Dependencies

Requirements: Python 3.10+ and Chrome/Chromium (installed by Playwright).

```sh
pip install -r requirements.txt
playwright install chromium
```

## Running Tests with Markers

You can run tests using markers with the `-m` flag. For example, to run the Unit 4 suite:

```sh
pytest -m unit_4
```

For more details of running tests with Pytest, see [Running Tests with Pytest](https://docs.pytest.org/en/latest/how-to/usage.html).

## Running Tests with different options

To run tests with different configurations, such as specific browsers or in headless mode, use the `--browser` and `--headless` flags. By default, headless mode is disabled (False):

```sh
pytest --browser=firefox --headless
```

## Useful Links

- [Pytest Documentation](https://docs.pytest.org/en/latest/)
- [Running Tests with Pytest](https://docs.pytest.org/en/latest/how-to/usage.html)

## Unit 4 Practice Task

The starter suite has no reporter. Add Allure yourself as part of the task.

Run the Unit 4 suite in Chromium:

```sh
pytest -m unit_4 --browser=chromium
```

Run it in headless mode:

```sh
pytest -m unit_4 --browser=chromium --headless
```
