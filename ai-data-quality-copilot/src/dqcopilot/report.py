'''
Report rendering module.

This module is responsible for transforming profiling results,
rule violations, and the calculated data quality score into a
human-readable Markdown report.

The report is intended for:
- Stakeholders (high-level overview)
- Engineers (rule violations and metrics)
- Documentation / portfolio usage
'''

from pathlib import Path
import json


def render(out: Path, profile, rules, score):
    '''
    Render a Data Quality report as a Markdown file.

    Parameters
    ----------
    out : Path
        Output directory where the report will be written.
    profile : dict
        Profiling metrics (rows, duplicate rate, null rates).
    rules : list of dict
        List of rule evaluation results.
    score : float
        Overall data quality score (0–100).
    '''

    # ------------------------------------------------------------------
    # Ensure output directory exists
    # ------------------------------------------------------------------
    out.mkdir(parents=True, exist_ok=True)

    lines = []

    # ------------------------------------------------------------------
    # Report header
    # ------------------------------------------------------------------
    lines.append("# Data Quality Summary\n\n")

    # ------------------------------------------------------------------
    # Overall Data Quality Score
    # ------------------------------------------------------------------
    lines.append("## Overall Score\n")
    lines.append(f"**{score}/100**\n\n")

    # ------------------------------------------------------------------
    # Dataset-level information
    # ------------------------------------------------------------------
    lines.append("## Dataset\n")
    lines.append(f"- Rows: {profile.get('rows')}\n")
    lines.append(f"- Duplicate rate: {profile.get('duplicate_rate', 0):.2%}\n\n")

    # ------------------------------------------------------------------
    # Null value statistics
    # ------------------------------------------------------------------
    lines.append("## Null rates\n")
    lines.append("```json\n")
    lines.append(json.dumps(profile.get("null_rate", {}), indent=2))
    lines.append("\n```\n\n")

    # ------------------------------------------------------------------
    # Rule violations
    # ------------------------------------------------------------------
    lines.append("## Rule violations\n")
    for r in rules:
        lines.append(
            f"- {r.get('rule')}: {r.get('failed')} failed rows\n"
        )

    # ------------------------------------------------------------------
    # Write Markdown report to disk
    # ------------------------------------------------------------------
    (out / "summary.md").write_text("".join(lines), encoding="utf-8")
