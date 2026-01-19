'''
Rule-based data quality checks.

This module defines deterministic data quality rules that are
commonly used in data governance and analytics projects.

Each rule validates a specific expectation about the dataset
and reports how many rows violate this expectation.
'''

import pandas as pd
import re

# Regular expression for a basic email validation (name@domain.tld)
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

# Regular expression for ISO-2 country codes (e.g. DE, AT, CH)
ISO2_RE = re.compile(r"^[A-Z]{2}$")


def run_rules(csv: str) -> list[dict]:
    '''
    Execute data quality rules on a CSV dataset.

    Parameters
    ----------
    csv : str
        Path to the input CSV file.

    Returns
    -------
    list of dict
        Each dictionary represents a rule evaluation result with:
        - rule (str): human-readable rule description
        - failed (int): number of rows violating the rule
    '''

    # Load dataset
    df = pd.read_csv(csv)

    results = []

    # ------------------------------------------------------------------
    # Rule: customer_id must be unique
    #
    # Rationale:
    # Duplicate primary keys break joins, aggregations,
    # and downstream analytics.
    # ------------------------------------------------------------------
    if "customer_id" in df.columns:
        failed = int(df["customer_id"].duplicated().sum())
        results.append({
            "rule": "unique customer_id",
            "failed": failed
        })

    # ------------------------------------------------------------------
    # Rule: email must be valid
    #
    # Rationale:
    # Invalid email addresses reduce data usability for
    # communication, identity resolution, and customer analytics.
    # ------------------------------------------------------------------
    if "email" in df.columns:
        s = df["email"].astype(str)
        failed = int((~s.str.match(EMAIL_RE)).sum())
        results.append({
            "rule": "valid email",
            "failed": failed
        })

    # ------------------------------------------------------------------
    # Rule: country_code must follow ISO-2 standard
    #
    # Rationale:
    # Standardized country codes are required for
    # reporting, segmentation, and regulatory compliance.
    # ------------------------------------------------------------------
    if "country_code" in df.columns:
        s = df["country_code"].astype(str)
        failed = int((~s.str.match(ISO2_RE)).sum())
        results.append({
            "rule": "country ISO-2",
            "failed": failed
        })

    return results
