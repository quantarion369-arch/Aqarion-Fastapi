# Audit report

**Status:** maintained

## Corrections applied

1. Gaussian moment:

       integral y^2 e^(-3 y^2 / 4) dy = 4 sqrt(pi) / (3 sqrt(3))

   Was incorrectly stated as `2 pi / 3 * sqrt(pi / 3)`.

2. Falling-factorial expansion:

   `+ k^2 / (4 n^2)` restored. Order `t^-2` on saddle scale; does not
   change D, but must be present past first order.

3. Partition prefactor:

   `N = k - 1/24` shift contributes `-a/(48 sqrt(k))` to relative
   expansion. Without it, `D_raw = -0.31028` (ruled out).

## Status ledger

| Component               | Status              |
|-------------------------|---------------------|
| Leading C               | proof candidate     |
| Leading K               | proof candidate     |
| D                       | conditional         |
| E_log                   | conditional         |
| L1 partition lemma      | stated              |
| L2 saddle expansion     | assembled           |
| L3 global tail          | closed in outline   |
| L4 discrete Laplace     | stated              |
| Interval certification  | OPEN                |
| Lean formalization      | OPEN                |
| Novelty                 | OPEN                |
| C4 / Publication        | BLOCKED             |
