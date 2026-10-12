
"""Exact integer partition function p(n).

Uses Euler's generalized pentagonal-number recurrence with an
incrementally maintained cache. The iterative implementation avoids
Python recursion-depth limits.

This module computes exact integer values; it does not certify any
asymptotic theorem.
"""

from threading import Lock


_PARTITION_VALUES: list[int] = [1]
_PARTITION_LOCK = Lock()


def partition(n: int) -> int:
    """Return p(n), the number of integer partitions of n.

    By convention, p(0) = 1 and p(n) = 0 for n < 0.

    Known values:
        p(0) = 1
        p(1) = 1
        p(2) = 2
        p(3) = 3
        p(4) = 5
        p(5) = 7
        p(10) = 42
        p(50) = 204226
        p(100) = 190569292
        p(1000) = 24061467864032622473692149727991
    """
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
