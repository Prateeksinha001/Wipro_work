# Assignment 2 — Data-Driven API Automation with Python Behave
## Scenario 2: Use of Test Data Driven Automation in Python Behave Framework

- **Objective:** Perform Python automation using the Python Behave framework, driven by external test data.
- **Tools:** Python, Behave, PyCharm Community.
- **Day-wise tasks (Day 1–4):** Adapt the Python BDD framework for **API automation** (instead of UI/Selenium as in Scenario 1), using data-driven test cases.

---

## 1. Project Structure

```
assignment2/
├── README.md
├── requirements.txt
├── behave.ini
├── testdata/
│   └── users.json              # External test data (data-driven source)
├── features/
│   ├── environment.py          # Session/config setup for API calls
│   ├── api_users.feature       # Data-driven scenarios (Scenario Outline + JSON data)
│   └── steps/
│       └── api_steps.py        # Step definitions using `requests`
```

---

## 2. What "Data-Driven" Means Here

Instead of hardcoding values in the feature file, test inputs (and expected
results) live in **`testdata/users.json`**. There are two complementary
data-driven techniques shown in this project, and either satisfies the
assignment — use whichever your scenario needs:

1. **Gherkin `Scenario Outline` + `Examples` table** — data lives inline in
   the `.feature` file, one row per test case. Good for a handful of cases
   you want reviewers to see at a glance.
2. **External JSON file loaded by the step definitions** — data lives
   outside the feature file entirely (`testdata/users.json`), and the
   scenario iterates over it. Good for larger datasets, or data that's
   shared across multiple features, or generated separately (e.g. exported
   from a spreadsheet).

`api_users.feature` demonstrates approach (1); `api_steps.py` also shows how
to pull rows from approach (2) so you can adapt whichever your instructor
expects.

---

## 3. Tools & Platform Setup

### 3.1 Install dependencies
```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

`requirements.txt`:
- `behave` — BDD framework
- `requests` — HTTP client for API automation
- `jsonschema` — optional, for validating API response shape

### 3.2 PyCharm Community setup
1. Open `assignment2/` as a PyCharm project.
2. Settings → Project → Python Interpreter → select the `venv` created above.
3. Install the **Gherkin** plugin (Settings → Plugins) for `.feature` syntax
   highlighting and step navigation.
4. Run via right-click on `features/` → **Run 'behave'**, or from the
   terminal: `behave`.
5. Debug: set a breakpoint in `api_steps.py`, then **Run → Debug 'behave'**.

---

## 4. Day-wise Tasks: Adapting the BDD Framework for API Automation

This assignment reuses the Behave skeleton from Scenario 1 but swaps the
**driver layer**: instead of Selenium's `webdriver` driving a browser, the
steps use the `requests` library to call a REST API directly. Everything
else in the BDD structure (feature files, Gherkin syntax, step decorators,
`environment.py` hooks) stays conceptually the same.

- **Day 1:** Set up the base framework — install `requests`, define
  `context.base_url` and a `context.session` (a `requests.Session()`) in
  `environment.py` so every step reuses the same connection/headers/auth.
- **Day 2:** Convert your existing UI-style steps into API steps: `Given`
  steps prepare request payloads/headers, `When` steps call
  `context.session.get/post/put/delete(...)`, `Then` steps assert on
  `response.status_code` and `response.json()`.
- **Day 3:** Introduce the test data layer — parameterize scenarios with a
  `Scenario Outline` + `Examples` table, and/or load `testdata/users.json`
  so the same steps run once per data row.
- **Day 4:** Add response validation and reporting — assert on JSON schema/
  field values, and generate a report (`behave -f allure_behave.formatter...`
  or Behave's built-in JUnit output: `behave --junit`).

---

## 5. Sample Data-Driven Feature

`features/api_users.feature`:
```gherkin
Feature: User API data-driven tests
  As a QA engineer
  I want to validate the Users API against multiple data sets
  So that I can confirm it behaves correctly for each input

  Scenario Outline: Create a user via API with different payloads
    Given the API endpoint "/users"
    When the user sends a POST request with name "<name>" and job "<job>"
    Then the response status code should be <status_code>
    And the response should contain name "<name>"

    Examples: Valid users
      | name    | job          | status_code |
      | Alice   | Engineer     | 201         |
      | Bob     | QA Analyst   | 201         |
      | Charlie | Product Mgr  | 201         |
```

This uses the public `reqres.in` test API as a placeholder target — swap
`context.base_url` in `environment.py` for your real API under test.

---

## 6. Running the Suite

```bash
behave                              # run everything
behave features/api_users.feature   # run one feature
behave --junit                      # generate JUnit XML reports
```
