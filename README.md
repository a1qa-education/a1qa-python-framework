# Python BDD Automation Framework

A framework for test automation using the Behavior Driven Development (BDD) approach.

## Project Structure

```
├── .env.example            # Template for environment variables (secrets)
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
```

## 🛠️ Technologies

- ![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
- ![Behave](https://img.shields.io/badge/Behave-1.2.6-green?style=flat-square)
- ![Playwright](https://img.shields.io/badge/Playwright-1.48.0-yellow?style=flat-square&logo=playwright)
- ![Allure](https://img.shields.io/badge/Allure-2.8.0-orange?style=flat-square&logo=qameta)

## 🚀 Running Tests

### Basic Run of All Tests

```bash
# Run all tests
behave
```

### Running a Specific Feature File

```bash
# Run specific feature
behave tests/features/your_test_feature.feature
```

## Environment Setup (Secrets Management)

Before running the tests for the first time, you must configure your local environment:
1. Locate the `.env.example` file in the root directory.
2. Duplicate this file and rename the copy to `.env` (this file is ignored by Git).
3. Open your new `.env` file and populate it with the actual credentials.

If you forget to set this up, the framework's `EnvProvider` will explicitly halt test execution and warn you.
```

### Running Tests by Tags

```bash
# Run tests with a specific tag
behave --tags=@smoke

# Exclude tests with a specific tag
behave --tags=~@skip

# Run tests with multiple tags (AND condition)
behave --tags=@smoke --tags=@critical

# Run tests with multiple tags (OR condition)
behave --tags=@smoke,@critical
```

### Running with Parameters

```bash
# Run with a specific browser
behave -D browser=firefox

# Run in headless mode
behave -D headless=true

# Combined run
behave -D browser=webkit -D headless=true tests/features
```

### Generating Allure Reports

```bash
# Display allure report
allure serve allure-results