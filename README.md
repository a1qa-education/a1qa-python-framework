# Python BDD Automation Framework

A BDD UI test automation framework built with **Python, Playwright, Behave and Allure**,
targeting [timeanddate.com](https://www.timeanddate.com).

This is the Python counterpart of the same final task implemented in
[Java](https://github.com/a1qa-education/java_unit_bdd/tree/task/unit_5_final_task),
[C#](https://github.com/a1qa-education/csharp_unit_bdd/tree/unit_5_final_task) and
[JavaScript](https://github.com/a1qa-education/a1qa-js-playwright-framework/tree/unit_5_final_task).

## 🛠️ Tech Stack

- ![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)
- ![Behave](https://img.shields.io/badge/Behave-1.2.6-green?style=flat-square)
- ![Playwright](https://img.shields.io/badge/Playwright-1.48.0-yellow?style=flat-square&logo=playwright)
- ![Allure](https://img.shields.io/badge/Allure-2.8.0-orange?style=flat-square&logo=qameta)

## Prerequisites

- **Python 3.9+** (developed and verified on 3.12)
- **Chromium** installed via Playwright
- **Allure commandline** (optional, for viewing reports)

```bash
python -m venv .venv
```

```bash
pip install -r requirements.txt
```

```bash
playwright install chromium
```

## Project Structure

```text
a1qa-python-framework/
├── .env.example                  # Template for environment variables (secrets)
├── behave.ini                    # Behave runner + Allure formatter configuration
├── configs/
│   ├── settings.py               # Base URL, default paths, viewport
│   └── test_data/
│       └── configuration.json    # Non-sensitive test data
├── framework/                    # Reusable technical core
│   ├── logger/                   # Logging setup
│   ├── ui/
│   │   ├── browser/              # Browser wrapper, dialogs, windows
│   │   ├── constants/            # Timeouts, element types, locator templates
│   │   ├── decorators/           # @step and @action decorators
│   │   ├── elements/             # Element wrappers (Button, Input, Label, ElementsList, …)
│   │   └── pages/                # BasePage
│   └── utils/                    # EnvProvider, config/file/string helpers
├── pages/                        # Application Page Objects
│   ├── constants.py              # MainPageNavigation enum, shared locator templates
│   ├── main_page.py
│   ├── weather_page.py
│   ├── city_weather_page.py
│   └── world_clock_page.py
└── tests/
    └── features/
        ├── environment.py        # Behave hooks (browser lifecycle, Allure screenshots)
        ├── fixtures.py           # Tag-driven fixtures
        ├── search_city_weather.feature
        ├── personal_world_clock.feature
        └── steps/                # Step definitions
```

### Page Objects

| Class | Page |
|-------|------|
| `MainPage` | timeanddate.com home |
| `WeatherPage` | "Weather Around The World" search page |
| `CityWeatherPage` | Weather page of a single city |
| `WorldClockPage` | Personal World Clock |

## Running the Tests

```bash
behave
```

### Running a single scenario

```bash
behave --tags=@scenario1
```

Available tags: `@scenario1`, `@scenario2`.

### Running a specific feature file

```bash
behave tests/features/search_city_weather.feature
```

### Running with parameters

```bash
behave -D browser=firefox
```

> ⚠️ **Run headed.** `timeanddate.com` serves a Cloudflare bot check to headless Chromium,
> so the site does not render there. Headed mode is the default — do not pass
> `-D headless=true` for these scenarios.

### Allure report

```bash
allure serve allure-results
```

Results are written to `allure-results/`. A screenshot is automatically attached to any
failing step.

## Configuration

| What | Where |
|------|-------|
| Host URL | `configs/settings.py` (`TEST_APP_URL`) |
| Test data | `configs/test_data/configuration.json` |
| Browser, headless flag, Allure directory | behave userdata (`-D key=value`) and `behave.ini` |
| Timeouts | `framework/ui/constants/timeouts.py` |
| Secrets | `.env` (see `.env.example`) |

`before_scenario` launches a fresh browser and navigates to `TEST_APP_URL`; `after_scenario`
closes the page and the browser, so every scenario runs in an isolated context.

## Implemented Test Cases

### Scenario 1 — Search City Weather

**Feature:** `tests/features/search_city_weather.feature`
**Steps:** `tests/features/steps/search_city_weather_steps.py`
**Tag:** `@scenario1`

Verifies that a user can find the weather forecast for a city through the site's search.

| Step | Action |
|------|--------|
| 1 | Open the timeanddate.com main page |
| 2 | Navigate to the **Weather** section |
| 3 | Verify the page title confirms the Weather section is open |
| 4 | Clear the city search field |
| 5 | Search for **"New York"** |
| 6 | Wait for the autocomplete suggestions to appear |
| 7 | Select the **second** suggestion |

**Expected result:** the City Weather page opens and its headline contains "New York".

### Scenario 2 — Add City to Personal World Clock

**Feature:** `tests/features/personal_world_clock.feature`
**Steps:** `tests/features/steps/personal_world_clock_steps.py`
**Tag:** `@scenario2`

Verifies that a user can add a city to their Personal World Clock.

| Step | Action |
|------|--------|
| 1 | Open the Personal World Clock page |
| 2 | Open the **Add City** dialog |
| 3 | Verify the **"Search for a city"** dialog is open and its field is empty |
| 4 | Enter **"Minsk"** into the city name field |
| 5 | Wait for the autocomplete suggestions to appear |
| 6 | Select the first suggestion |
| 7 | Save the dialog |

**Expected result:** "Minsk" appears in the list of clocks.

## 📜 Strict Page Object Rules

1. **Selector isolation:** locators live only in Page classes. Step definitions must never
   contain `page.locator()` or `page.get_by_*`.
2. **Inheritance:** every page class inherits from `BasePage`.
3. **Unique page elements:** a `BaseElement` instance is passed to `super().__init__()` and used
   by `is_page_open()` for a fast, non-blocking state check.
4. **Encapsulated locators:** locators are wrapped in element classes (`Button`, `Input`, `Label`, …).
5. **Action-oriented methods:** pages expose user actions, not raw element access.
6. **No page chaining:** page methods never return another page; navigation is driven by steps.
7. **No assertions in pages:** pages return values, step definitions assert on them.
8. **Explicit waits for text:** text getters wait for the element to be visible before reading.
