"""Exact integer partition function p(n).

Uses an iterative, incrementally cached pentagonal recurrence.
This computation does not certify an asymptotic theorem.
"""

from threading import Lock

_PARTITION_VALUES: list[int] = [1]
_PARTITION_LOCK = Lock()


def partition(n: int) -> int:
    """Return p(n), with p(0) = 1 and p(n) = 0 for n < 0."""
    if n < 0:
        return 0

    with _PARTITION_LOCK:
        while len(_PARTITION_VALUES) <= n:
            m = len(_PARTITION_VALUES)
            total = 0
            k = 1

            while True:
                g1 = k * (3 * k - 1) // 2
                if g1 > m:
                    break

                sign = 1 if k % 2 else -1
                total += sign * _PARTITION_VALUES[m - g1]

                g2 = k * (3 * k + 1) // 2
                if g2 <= m:
                    total += sign * _PARTITION_VALUES[m - g2]

                k += 1

            _PARTITION_VALUES.append(total)

        return _PARTITION_VALUES[n]
