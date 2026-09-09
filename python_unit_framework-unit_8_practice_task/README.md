# Steam Store E2E Automation Framework

## Project Overview

This project contains an automated End-to-End test for Steam Store search and filtering functionality.

The original test (`SteamLegacyTest`) was implemented as a single monolithic script containing:

- Hardcoded test data
- Long procedural flows
- Fragile XPath locators
- Manual synchronization logic
- Duplicated code
- Poor maintainability

The objective of this project was to modernize the automation solution while preserving the original business validation logic.

---

# Test Case

### STEAM-TC-001

**Title:** Filtering by platform/mode and validating ascending price sorting (Lowest Price)

**Priority:** High

### Preconditions

- Browser launched in Incognito mode
- Navigate to https://store.steampowered.com/
- Interface language is English

### Test Steps

| Step | Action | Expected Result |
|------|---------|----------------|
| 1 | Enter "Action" into the main search bar and press Enter. | Search results page opens. Game list is not empty. |
| 2 | In the right sidebar (Narrow by OS), check the Windows checkbox. | Checkbox is checked. Results update dynamically. |
| 3 | In the right sidebar (Narrow by number of players), check the Co-op checkbox. | Checkbox is checked. Results update with both filters applied. |
| 4 | Click Sort by dropdown and select "Lowest Price". | List updates. Games are ordered cheapest to most expensive. |
| 5 | Extract Game Title + Final Price for the first 10 items. | Data extracted. Free games read as 0.00. Discounted games use final price only. |
| 6 | Verify the collected array of 10 prices is sorted in ascending order. | Each price is ≥ the previous one. |

### Expected Result

The collected list of prices is sorted from the lowest price to the highest price.

---

---

## Assignment Goals

### Phase 1: AI Code Audit

Perform an AI-assisted review of the legacy implementation and identify:

- Architectural issues
- Anti-patterns
- Code smells
- Flaky synchronization
- Brittle locators
- Maintainability concerns

All findings must be documented in:

```text
PROMPTS.md
```

### Phase 2: Decoupling & Architecture

Refactor the monolithic implementation using Page Object Model.

Requirements:

- Separate page interactions into Page Objects
- Move test data outside test logic
- Extract reusable utilities
- Preserve existing business validations

### Phase 3: Stabilization & Refactoring

Address all issues identified during the audit:

- Replace unstable locators
- Remove hardcoded waits
- Simplify data extraction logic
- Refactor custom sorting logic
- Improve readability and maintainability

---

## Deliverables

### 1. Modernized Project Structure

- Tests
- Page Objects
- Utils
- Test Data

### 2. Stable Automated Test

The refactored test must reliably validate:

- Search functionality
- OS filtering
- Player-count filtering
- Price sorting

### 3. PROMPTS.md

Must contain:

- AI audit prompts
- Audit results
- Refactoring prompts
- Architecture recommendations
- Stabilization notes

---

## Definition of Done

- Original STEAM-TC-001 business scenario preserved
- Test successfully refactored into POM architecture
- Test data extracted from test logic
- Utilities separated into reusable modules
- Hardcoded waits removed
- Stable locators implemented
- Sorting validation preserved
- AI review documented in PROMPTS.md
- Test executes reliably and consistently

---

## Technologies

- Python 3.10+
- Pytest
- Playwright
