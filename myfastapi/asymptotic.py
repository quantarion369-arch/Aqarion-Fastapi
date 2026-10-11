"""Hardy-Ramanujan asymptotic for p(n).

Leading term:

    p(n) ~ exp(a * sqrt(n)) / (4 * sqrt(3) * n)

with a = pi * sqrt(2/3). This is the leading order of the
PB-CORE-006 saddle analysis.
"""

import math


def hardy_ramanujan(n: int) -> float:
    """Leading-order Hardy-Ramanujan approximation to p(n)."""
    if n < 1:
        raise ValueError("n must be >= 1")
    a = math.pi * math.sqrt(2 / 3)
    return math.exp(a * math.sqrt(n)) / (4 * math.sqrt(3) * n)


def relative_error(n: int, exact: int) -> float:
    """Relative error |approx - exact| / exact for the leading term."""
    approx = hardy_ramanujan(n)
    return abs(approx - exact) / exact
