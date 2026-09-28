# Assignment 3 — Selenium Page Object Model in Python Behave
## Scenario 3: Selenium Page Object Model in the Python Behave Framework

- **Objective:** Debug and optimize web application automation using the
  Behave framework and Gherkin language.
- **Tools:** Behave, Python (Selenium for browser driving, reused from
  Scenario 1).
- **Day-wise tasks:** Leverage the Behave framework for a **test-data-driven
  approach**, this time layered on top of the **Page Object Model (POM)**
  design pattern.

This builds directly on Scenario 1 (Selenium + Behave) and Scenario 2
(data-driven testing): here the UI locators/actions are refactored out of
the step definitions and into dedicated **Page Object** classes, which is
the standard way to make a Selenium+Behave suite maintainable and debuggable
at scale.

---

## 1. Project Structure

```
assignment3/
├── README.md
├── requirements.txt
├── behave.ini
├── pages/
│   ├── __init__.py
│   ├── base_page.py         # Common wait/click/type helpers, used by every page
│   ├── login_page.py        # Locators + actions for the Login page
│   └── dashboard_page.py    # Locators + actions for the Dashboard page
├── testdata/
│   └── login_data.json      # Data-driven login test cases
├── features/
│   ├── environment.py       # Driver setup/teardown + page object wiring
│   ├── login_pom.feature    # Data-driven scenarios calling into page objects
│   └── steps/
│       └── login_pom_steps.py  # Thin steps — all Selenium logic lives in pages/
```

---

## 2. Why Page Object Model?

Without POM, every step definition contains raw Selenium calls
(`context.driver.find_element(By.ID, "username")...`). That means:
- The same locator gets duplicated across many step files.
- A single UI change (e.g. an ID renamed) requires editing every step that
  touches that element.
- Step definitions become hard to read and hard to debug, since business
  logic and low-level Selenium mechanics are mixed together.

**With POM:**
- Each page of the application under test gets one class (`LoginPage`,
  `DashboardPage`, …) that owns its locators and exposes readable methods
  like `login_page.enter_credentials(user, pw)`.
- Step definitions become one-liners that read almost like the Gherkin
  itself: `login_page.enter_credentials(username, password)`.
- A UI change means editing **one page object**, not every step file.
- Debugging is easier: if a test fails, you know immediately whether the
  problem is in the *page object* (locator/interaction logic) or the *step
  definition* (test flow/assertions).

---

## 3. Tools & Platform Setup

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

PyCharm setup is the same as Scenario 1/2 (Gherkin plugin, interpreter
pointed at `venv`, run/debug via right-click on `features/`).

---

## 4. Day-wise Tasks: Data-Driven Approach on Top of POM

- **Day 1:** Extract all existing Selenium locators/actions out of step
  files into `pages/base_page.py` (shared helpers: `click`, `type_text`,
  `wait_for_element`) and page-specific classes (`login_page.py`,
  `dashboard_page.py`).
- **Day 2:** Rewrite step definitions to call page object methods instead of
  raw `driver.find_element(...)` calls — steps should contain *no* Selenium
  locator code at all.
- **Day 3:** Add the data-driven layer: convert the login scenario into a
  `Scenario Outline` with an `Examples` table (and/or load
  `testdata/login_data.json`, same pattern as Scenario 2), so one scenario
  definition covers many input combinations.
- **Day 4:** Debug and optimize:
  - Replace `time.sleep()` calls with explicit `WebDriverWait` (already done
    in `base_page.py`) to remove flakiness and speed up runs.
  - Add logging/screenshots on failure (`environment.py`'s `after_step`
    hook) so failures are diagnosable without re-running.
  - Run with `behave --no-capture` or PyCharm's debugger to step through a
    failing scenario line by line.

---

## 5. Sample Data-Driven POM Feature

`features/login_pom.feature`:
```gherkin
Feature: Login using Page Object Model
  As a QA engineer
  I want login scenarios driven by external test data
  So that the same steps validate many credential combinations

  Background:
    Given the user is on the login page

  Scenario Outline: Login attempt with various credentials
    When the user logs in with username "<username>" and password "<password>"
    Then the login result should be "<expected_result>"

    Examples: Login combinations
      | username | password    | expected_result |
      | testuser | Test@1234   | success          |
      | testuser | WrongPass   | failure          |
      |          | Test@1234   | failure          |
```

---

## 6. Debugging & Optimization Checklist (Day 4 focus)

- [ ] No hardcoded `time.sleep()` anywhere — use `WebDriverWait` (see
      `base_page.py`).
- [ ] Every locator lives in a page object, not in a step file.
- [ ] Failed scenarios auto-capture a screenshot (`environment.py`
      `after_step` hook, wired below).
- [ ] Run headless in CI (`HEADLESS=true behave`) but headed locally for
      debugging.
- [ ] Use `behave --tags=@smoke` to run a fast subset while debugging,
      rather than the full suite.

---

## 7. Running the Suite

```bash
behave                                 # run everything
behave features/login_pom.feature      # run one feature
HEADLESS=true behave                   # headless (e.g. CI)
behave --no-capture                    # see print/log output live while debugging
```
