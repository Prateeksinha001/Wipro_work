# Assignment 4 — Robot Framework: Syntax, Data-Driven Testing, Custom Keywords, Assertions, Setup/Teardown, Tags, and Reporting

---

## 1. What is Robot Framework, and what's it used for?

Robot Framework is a **keyword-driven test automation tool**. Instead of writing
test logic as raw Python function calls, you write test steps in `.robot` files
using **keywords** — short, readable phrases like `Open Browser`, `Input Text`,
`Click Button`, `Should Be Equal`. Each keyword is backed by a real Python
function, either from a pre-built library (like `SeleniumLibrary` for web
browsers, or `RequestsLibrary` for APIs) or one you write yourself.

**Use case:** it's chosen over "plain" Selenium+Python (or even Behave) when a
team wants test cases that are extremely readable — often readable even by
non-programmers (manual QA, business analysts) — while still being backed by
real, extensible Python code underneath. It's widely used in industry for both
web UI testing and API testing.

This assignment's 7 sections are a tour of Robot Framework's core building
blocks. This project implements all of them as runnable examples.

---

## 2. Project Structure

```
assignment4/
├── README.md
├── requirements.txt
├── resources/
│   └── common.robot            # Shared variables + reusable keywords (login/logout)
├── libraries/
│   └── CustomLibrary.py        # Our own custom Python keyword library
├── testdata/
│   └── login_data.csv          # External data file for data-driven tests
├── tests/
│   ├── 01_basic_syntax.robot            # Section 1
│   ├── 02_variables_datadriven.robot    # Section 2
│   ├── 03_custom_keywords.robot         # Section 3
│   ├── 04_assertions_api.robot          # Section 4
│   └── 05_setup_teardown_tags.robot     # Sections 5 & 6
```

(Section 7 — Reports and Logs — isn't a separate file; it's something Robot
Framework produces automatically every time you run any of the suites above.
See §6.)

---

## 3. Setup — What You Actually Do With These Folders

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

This installs:
- `robotframework` — the core test runner
- `robotframework-seleniumlibrary` — adds browser keywords (`Open Browser`, `Input Text`, etc.)
- `robotframework-requests` — adds API keywords (`GET On Session`, etc.)
- `robotframework-pabot` — lets you run tests in parallel (Section 6)

**VS Code:** install the **"Robot Framework Language Server"** extension for
`.robot` syntax highlighting, autocomplete, and "go to keyword definition."
Same idea as the Gherkin plugin from the earlier assignments.

**Chrome:** modern Selenium (4.6+, which SeleniumLibrary depends on)
auto-downloads the matching ChromeDriver the first time you run a test — you
don't need to install it manually.

**Important — same as before:** `tests/` point at the real
`tutorialsninja.com/demo` site. For the "successful login" tests to actually
pass, register an account there first and put those real credentials into
`resources/common.robot` (`${VALID_USERNAME}` / `${VALID_PASSWORD}`) and
`testdata/login_data.csv`.

---

## 4. Section-by-Section: What Each File Does and Why

### Section 1 — `01_basic_syntax.robot`
The absolute basics: open a browser, go to a URL, type into a field
(`Input Text`), and confirm an element exists (`Page Should Contain Element`).
This is the Robot Framework equivalent of your very first Selenium script.

### Section 2 — `02_variables_datadriven.robot`
- `${USERNAME}` / `${PASSWORD}` show **variables**: instead of typing
  credentials directly into a step, they're defined once and reused.
- The second test shows **data-driven testing**: our custom keyword
  `Get Test Data From Csv` reads `testdata/login_data.csv`, and a `FOR` loop
  repeats the same login steps once per row — exactly like the
  `Scenario Outline` you used in the Behave assignments, just Robot's way of
  doing it.

### Section 3 — `03_custom_keywords.robot`
- `Add Two Numbers` is a **custom keyword** — Robot doesn't ship this, we
  wrote it ourselves in `libraries/CustomLibrary.py`. Any plain Python
  function in a file imported as a `Library` becomes a usable keyword
  automatically.
- The second test uses **`BuiltIn`**, Robot's own always-available library,
  for string operations (`Catenate`, `Convert To Upper Case`) and math
  (`Evaluate`).

### Section 4 — `04_assertions_api.robot`
- First test: perform an action (load a page), then assert the outcome
  (`Should Be Equal As Strings` on the page title) — the fundamental
  "act, then assert" pattern of any test.
- Second test: calls a real API (`https://reqres.in`) using
  `RequestsLibrary`, and verifies a field in the JSON response with
  `Should Be Equal As Strings`.

### Sections 5 & 6 — `05_setup_teardown_tags.robot`
- `Test Setup    Open Application And Login` runs **before every test** in
  this file — so each test starts already logged in, without repeating that
  code.
- `Test Teardown    Logout And Close` runs **after every test** — logs out
  and closes the browser, even if the test failed, so nothing leaks into the
  next test.
- `[Tags]    smoke    login` / `[Tags]    regression    login` show how to
  label tests so you can run subsets of your suite selectively (see §5).

---

## 5. Running Tests, Tags, and Parallel Execution (Section 6)

Run everything:
```bash
robot tests/
```

Run only tests tagged `smoke`:
```bash
robot --include smoke tests/
```

Run everything **except** tests tagged `regression`:
```bash
robot --exclude regression tests/
```

Run in parallel (requires `pabot`, already in `requirements.txt`):
```bash
pabot --processes 4 tests/
```
> Note: `--processes` is a `pabot` option, not built into plain `robot` — the
> standard `robot` runner always executes suites one at a time. `pabot` is a
> separate, widely-used tool that runs multiple Robot suites concurrently.

---

## 6. Reports and Logs (Section 7)

Every time you run `robot` (or `pabot`), three files are generated
automatically in the current directory (no extra code needed):

- **`report.html`** — a high-level pass/fail summary of the whole run.
- **`log.html`** — a detailed, clickable log of every keyword executed,
  including screenshots on Selenium failures.
- **`output.xml`** — the raw machine-readable result data (used if you want
  to combine multiple runs, e.g. after a `pabot` parallel run).

Open `report.html` in any browser after a run to see the results visually.

To send your own messages to the log for debugging, use the `Log` keyword
(already used in `02_variables_datadriven.robot` and
`05_setup_teardown_tags.robot`):
```
Log    Trying login with: ${row}[email]    console=True
```
`console=True` also prints the message directly in your terminal while the
run is happening, not just inside `log.html`.

To keep reports organized per run, output to a dedicated folder:
```bash
robot --outputdir results tests/
```

---

## 7. Quick Reference — Running Individual Pieces

```bash
robot tests/01_basic_syntax.robot              # just Section 1
robot tests/02_variables_datadriven.robot      # just Section 2
robot --include custom-keyword tests/          # any test tagged custom-keyword
robot --include api tests/                     # just the API assertion test
```
