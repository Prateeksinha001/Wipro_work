# Assignment 1 — Selenium + Python BDD (Behave) Framework
## Scenario 1: Implementation of Selenium Python and Behave BDD

This project is a complete, runnable skeleton that satisfies the assignment brief:

- **Objective:** Set up a Python BDD framework and debug/run an automation framework for end‑to‑end scenarios.
- **Tools:** Behave (BDD framework for Python), Selenium, PyCharm as IDE.
- **Day‑wise tasks:** QEMU-based embedded platform simulation (Day 1) + running the scenario tasks against that simulated environment instead of real hardware (Days 2–4).

---

## 1. Project Structure

```
assignment1/
├── README.md                      # This file — full write-up
├── requirements.txt                # Python dependencies
├── behave.ini                      # Behave configuration
├── features/
│   ├── environment.py              # Behave hooks (setup/teardown, driver mgmt)
│   ├── login.feature               # Sample BDD scenario (Gherkin)
│   └── steps/
│       └── login_steps.py          # Step definitions for login.feature
└── docs/
    └── QEMU_Eclipse_Setup.md       # Day 1: QEMU + Eclipse/GDB setup guide
```

---

## 2. Tools & Platform Setup

### 2.1 Install Python & dependencies
```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

`requirements.txt` includes:
- `behave` — BDD framework for Python (Gherkin → step definitions)
- `selenium` — browser automation
- `webdriver-manager` — auto-downloads the correct browser driver

### 2.2 PyCharm as IDE
1. Open the `assignment1/` folder as a PyCharm project.
2. **File → Settings → Project → Python Interpreter** → point it at the `venv` you created above.
3. Install the **Gherkin/Cucumber+ plugin** (Settings → Plugins → search "Gherkin") so `.feature` files get syntax highlighting and you can jump from a step in the feature file straight to its Python implementation.
4. Right-click `features/` → **Run 'behave'** (or run `behave` from the PyCharm terminal) to execute the suite.
5. To debug: set a breakpoint inside a step definition in `login_steps.py`, then run Behave in **Debug mode** from PyCharm (Run → Debug 'behave'). PyCharm will stop at the breakpoint just like a normal Python debug session.

---

## 3. Day-wise Tasks

### Day 1 — QEMU + Eclipse/GDB setup (embedded platform simulation)
Since real embedded hardware isn't available, Day 1 sets up a **software-simulated target**:
- **QEMU** emulates the target embedded board/CPU so the firmware/app under test can run on your PC instead of physical hardware.
- **Eclipse + GDB** connects to QEMU's built-in GDB server for source-level debugging of the code running inside the emulator.

Full step-by-step instructions are in **`docs/QEMU_Eclipse_Setup.md`**.

### Day 2–4 — Run the original scenario tasks against the simulated environment
Once QEMU is up (serving your embedded target on a local port/interface instead of a real device), you point your Selenium/Behave automation at whatever interface the simulated system exposes (e.g., a web UI served by the emulated device, or a REST/serial interface QEMU forwards to the host) instead of pointing it at physical hardware. The BDD scenario structure itself doesn't change — only the **target endpoint** does.

Example flow:
1. Start QEMU with your embedded image (`docs/QEMU_Eclipse_Setup.md`, Step 3).
2. QEMU forwards the emulated device's web/service port to a localhost port on your PC.
3. Update your `.feature` file's target URL (or a config value in `environment.py`) to point at `http://localhost:<forwarded-port>` instead of a real device IP.
4. Run `behave` — your existing scenarios execute unchanged, just against the emulator.

This is exactly what `features/environment.py` in this project is set up to do — it reads a `BASE_URL` that you can flip between "real device" and "QEMU-simulated device" without touching your feature files or step code.

---

## 4. Sample BDD Scenario

`features/login.feature`:
```gherkin
Feature: User login
  As a registered user
  I want to log into the application
  So that I can access my dashboard

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters username "testuser" and password "Test@1234"
    And the user clicks the login button
    Then the user should see the dashboard page
```

This is intentionally generic — replace the feature/steps with your actual end-to-end scenario once you know what UI/interface the simulated embedded target exposes.

---

## 5. Running the Suite

```bash
behave                          # run everything
behave features/login.feature   # run one feature
behave --tags=@smoke            # run tagged scenarios
```

Reports:
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/ features
```
(add `allure-behave` to `requirements.txt` if you want Allure HTML reports)

---

## 6. Debugging the Automation Framework Itself
- **PyCharm debugger**: breakpoints in step files, run Behave in Debug mode (see §2.2).
- **Selenium-side debugging**: run with a visible (non-headless) browser first (`environment.py` defaults to headed mode) so you can watch what the automation does.
- **Target-side debugging (the embedded app under test)**: use Eclipse + GDB attached to QEMU's GDB stub — see `docs/QEMU_Eclipse_Setup.md`, Step 4. This lets you step through the *target's* code while Selenium/Behave drives it externally.
