"""Integer partition function p(n).

Exact computation via Euler's pentagonal number theorem.
This is the primitive used in AQARION's PB-CORE-006 asymptotic work.
"""

from functools import lru_cache


@lru_cache(maxsize=None)
def partition(n: int) -> int:
    """Return p(n), the number of integer partitions of n.

    Known values: p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7,
    p(10)=42, p(50)=204226, p(100)=190569292.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1

    total = 0
    k = 1
    while True:
        g1 = k * (3 * k - 1) // 2
        if g1 > n:
            break
        sign = 1 if (k % 2) else -1
        total += sign * partition(n - g1)

        g2 = k * (3 * k + 1) // 2
        if g2 <= n:
            total += sign * partition(n - g2)
        k += 1
    return total
