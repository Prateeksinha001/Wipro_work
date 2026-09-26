# Selenium Python Automation Framework

## 📌 Overview

This project is a **Selenium automation testing framework developed using Python**.

It is designed for automating web application test scenarios using Selenium WebDriver and Python-based testing tools.

The project demonstrates the use of structured automation practices for creating, executing, and maintaining Selenium test cases.

---

## 🛠️ Technologies Used

* **Python**
* **Selenium WebDriver**
* **Pytest**
* **Page Object Model (POM)**
* **Git**
* **GitHub**
* **Visual Studio Code**

---

## 📂 Project Structure

The project structure is maintained as provided in the original framework.

```text
Selenium_Python_Automation_Framework/
│
├── [Project folders and files]
│
├── requirements.txt
├── README.md
└── .gitignore
```

The individual folders contain the framework's automation scripts, test cases, page-related implementations, utilities, and supporting files as provided in the project.

---

## ⚙️ Prerequisites

Before running the project, install:

* Python
* Google Chrome
* Visual Studio Code
* Git

Verify Python installation:

```bash
python --version
```

Verify Git installation:

```bash
git --version
```

---

## 🚀 Setup

### 1. Clone the Repository

Clone this repository using:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate to the project:

```bash
cd Selenium_Python_Automation_Framework
```

---

### 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

---

### 3. Activate the Virtual Environment

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

---

### 4. Install Dependencies

Install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🧪 Running the Tests

Run the test suite using:

```bash
pytest
```

For detailed test execution output:

```bash
pytest -v
```

To execute a specific test:

```bash
pytest <test_file_path> -v
```

Replace `<test_file_path>` with the appropriate test file from the project.

---

## 📊 Test Reports

If HTML reporting is configured in the framework, tests can be executed using the corresponding Pytest reporting command.

For example:

```bash
pytest -v --html=report.html
```

The generated report can be opened in a web browser.

---

## 🏗️ Framework Approach

The framework follows a structured Selenium automation approach.

The project separates automation components to make the test code easier to maintain and reuse.

The framework includes components for:

* Web browser automation
* Test execution
* Web element interaction
* Test validation
* Reusable automation functionality

---

## 🔐 Security

Do not commit sensitive information to GitHub.

The following should not be uploaded:

* Passwords
* API keys
* Access tokens
* Personal credentials
* Private configuration
* Other confidential information

Sensitive information should be stored locally or through environment variables.

---

## 📦 Dependencies

Project dependencies are maintained in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Author

**Prateek Sinha**

B.Tech – Computer Science & Engineering
Specialization: Artificial Intelligence

---

## 📚 Purpose

This project is maintained for **learning, practice, and demonstration of Selenium Python automation testing concepts**.
