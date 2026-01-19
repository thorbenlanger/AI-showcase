'''
Data Quality scoring module.

This module converts profiling metrics and rule violations
into a single, interpretable Data Quality Score.

The score is intentionally simple and explainable:
- 100 represents perfect data quality
- Penalties are applied for duplicates, missing values,
  and rule violations
- The final score is clamped to the range 0–100
'''


def score(profile: dict, rules: list[dict]) -> float:
    '''
    Calculate an overall Data Quality score.

    Parameters
    ----------
    profile : dict
        Profiling metrics (duplicate rate, null rates, etc.).
    rules : list of dict
        Rule evaluation results with counts of failed rows.

    Returns
    -------
    float
        Data Quality score between 0.0 and 100.0.
    '''

    penalty = 0.0

    # ------------------------------------------------------------------
    # Penalty for duplicate rows
    #
    # High duplicate rates indicate unreliable primary keys
    # and broken data model assumptions.
    # ------------------------------------------------------------------
    penalty += profile.get("duplicate_rate", 0) * 30.0

    # ------------------------------------------------------------------
    # Penalty for missing values
    #
    # Missing values reduce data completeness and usability.
    # Null rates are summed across all columns.
    # ------------------------------------------------------------------
    penalty += sum(profile.get("null_rate", {}).values()) * 20.0

    # ------------------------------------------------------------------
    # Penalty for rule violations
    #
    # Each failed row contributes a small penalty.
    # Values are clamped to avoid negative effects.
    # ------------------------------------------------------------------
    penalty += sum(
        max(0, r.get("failed", 0)) for r in rules
    ) * 0.01

    # ------------------------------------------------------------------
    # Final score calculation and clamping
    # ------------------------------------------------------------------
    s = 100.0 - penalty
    s = max(0.0, min(100.0, s))

    return round(s, 1)
