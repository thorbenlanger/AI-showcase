'''
Command Line Interface (CLI) for the AI Data Quality Copilot.

This script orchestrates the full data quality workflow:
- Load a CSV file
- Run data profiling
- Execute data quality rules
- Calculate a data quality score
- Generate a Markdown report

It is designed to be run from the project root directory.
'''

import argparse
from pathlib import Path
import os

from dqcopilot.profiling import profile
from dqcopilot.rules import run_rules
from dqcopilot.score import score as score_fn
from dqcopilot.report import render


def main():
    '''
    Main entry point for the dqcopilot CLI.

    Steps:
    1. Parse command-line arguments
    2. Prepare the output directory
    3. Run profiling, rules, and scoring
    4. Render the final report
    '''

    # ------------------------------------------------------------------
    # Parse CLI arguments
    # ------------------------------------------------------------------
    ap = argparse.ArgumentParser(prog="dqcopilot")
    ap.add_argument("csv", help="Path to the input CSV file")
    ap.add_argument("--out", default="reports", help="Output directory for generated reports")
    ap.add_argument("--debug", action="store_true", help="Print debug information")
    args = ap.parse_args()

    # ------------------------------------------------------------------
    # Prepare output directory
    # ------------------------------------------------------------------
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # Optional debug output to help troubleshooting
    # ------------------------------------------------------------------
    if args.debug:
        print("Current working directory:", os.getcwd())
        print("CSV path:", args.csv)
        print("CSV exists:", Path(args.csv).exists())
        print("Output directory:", str(out.resolve()))

    # ------------------------------------------------------------------
    # Run data quality pipeline
    # ------------------------------------------------------------------
    profiling = profile(args.csv)           # Basic dataset statistics
    rules = run_rules(args.csv)             # Rule-based data quality checks
    dq_score = score_fn(profiling, rules)   # Aggregate quality score

    # ------------------------------------------------------------------
    # Render final report
    # ------------------------------------------------------------------
    render(out, profiling, rules, dq_score)

    # ------------------------------------------------------------------
    # Final debug output
    # ------------------------------------------------------------------
    if args.debug:
        print("Report written to:", str((out / "summary.md").resolve()))

    print(f"Done. Report written to: {out / 'summary.md'}")


if __name__ == "__main__":
    main()
