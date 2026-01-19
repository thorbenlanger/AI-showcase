# AI Data Quality Copilot

A portfolio-ready project demonstrating how **Data Quality** and **Data Governance**
can be operationalized with **Python** using an explainable, rule-based approach.

The goal of this project is not to build a black-box system, but to show how
data quality issues can be **measured, explained, and communicated** in a way
that is useful for both engineers and stakeholders.

---
## Why "AI" in AI Data Quality Copilot?

This project follows an **applied AI** approach.

Rather than training machine learning models, it focuses on:
- automated reasoning over data quality signals
- heuristic and rule-based evaluation
- explainable scoring and prioritization
- decision support instead of autonomous decisions

This reflects how AI is commonly applied in
data governance, quality management, and risk systems,
where transparency and explainability are critical.
---

## Key Features

- **Data profiling**
  - Row count
  - Duplicate rate
  - Null value rate per column
- **Rule-based data quality checks**
  - Uniqueness (primary keys)
  - Validity (email format, ISO country codes)
- **Explainable Data Quality score**
  - Transparent scoring logic
  - Score range: 0–100
- **Automated reporting**
  - Human-readable Markdown report
- **Synthetic demo data**
  - No real personal or sensitive data
  - Intentionally includes quality issues

---

## Project Structure (Simplified)

```
ai-data-quality-copilot/
├── src/dqcopilot/        # Core application logic
├── data/synthetic/      # Synthetic demo data generator
├── reports/             # Generated data quality reports
├── pyproject.toml       # Project & dependency definition
├── Makefile             # Task automation
└── README.md
```

---

## Makefile Usage (Optional)

This project includes a simple `Makefile` to standardize common workflows.
The Makefile acts as a thin automation layer on top of Python commands.

It is **not required**, but helps to:
- reduce repetitive command typing
- make demo runs reproducible
- provide a single entry point for common tasks

### Available Targets

- `make data`  
  Generates synthetic demo data used for testing and demonstration.

- `make demo`  
  Runs the full data quality pipeline:
  profiling → rules → scoring → report generation.

### Platform Note

`make` is commonly available on Linux and macOS systems.
On Windows, the Python commands can be executed directly instead
(see Quickstart section below).

---

## pyproject.toml Explained

This project uses a modern `pyproject.toml` file to define:
- project metadata
- Python version requirements
- runtime dependencies
- optional development dependencies
- CLI entry points

Using `pyproject.toml` replaces older approaches such as `setup.py`
and is the recommended standard for modern Python projects.

Key aspects in this project:

- **Dependencies**  
  All required libraries (e.g. pandas) are defined centrally and installed via:
  ```bash
  pip install -e .
  ```

- **Editable installation (`-e`)**  
  Installs the project in development mode, so code changes take effect immediately
  without reinstalling.

- **CLI definition**  
  The `dqcopilot` command is registered via:
  ```toml
  [project.scripts]
  dqcopilot = "dqcopilot.cli:main"
  ```

This setup reflects how Python projects are structured in real-world
data engineering and backend environments.

---

## Quickstart

### Requirements
- Python 3.10+
- `pip`
- (Optional) `make` for Unix-based systems

---

### Setup (All Platforms)

```bash
python -m venv .venv
```

Activate the virtual environment:

- **Windows (PowerShell)**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

- **Linux / macOS**
  ```bash
  source .venv/bin/activate
  ```

Install the project in editable mode:

```bash
pip install -e .
```

---

### Generate Demo Data

```bash
python data/synthetic/generate_data.py --out data/synthetic/customers.csv --rows 2000
```

---

### Run Data Quality Analysis

```bash
python -m dqcopilot.cli data/synthetic/customers.csv --out reports
```

The generated report will be written to:

```
reports/summary.md
```

---

### Optional: Using `make` (Linux / macOS)

If `make` is available on your system:

```bash
make data
make demo
```

---

## Output Example

The generated `summary.md` report includes:

- Overall Data Quality score
- Dataset-level statistics
- Column-level null rates
- Rule violations with failed row counts

This makes data quality issues **explicit, measurable, and explainable**.

---

## Design Principles

- **Explainability over complexity**
- **Deterministic rules instead of black-box models**
- **Governance-first thinking**
- **Clear separation of concerns**
  - Profiling
  - Rules
  - Scoring
  - Reporting

---

## Disclaimer

All data used in this project is **synthetic** and created solely for demonstration
purposes.  
No real personal or sensitive data is processed.

---

## Possible Extensions

- Severity levels per rule (HIGH / MEDIUM / LOW)
- Policy and rule identifiers (e.g. DQ-001)
- HTML reporting and dashboards
- PII detection and masking
- Historical data quality trends
