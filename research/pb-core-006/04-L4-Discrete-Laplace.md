# Lemma 4 — Discrete Laplace

**Status:** STATED · shifted-mesh uniformity asserted

Mesh: `h = t^(-3/2)`.

Poisson summation for Gaussian times polynomial:

    h * sum_{m in Z} P(m h) e^(-3 (m h)^2 / 4)
      = integral_R P(y) e^(-3 y^2 / 4) dy + O_P(e^(-c n))

Uniform in mesh shift `theta in [0,1)`: the Fourier transform of a
Gaussian times polynomial is again Gaussian times polynomial, so the
shift enters only through `e^(2 pi i l theta)` which is bounded by 1.

Truncation to `|y| <= L(t) = sqrt(4 log t)`:

    integral_{|y| > L} e^(-3 y^2 / 4) dy = O(e^(-3 L^2 / 4) / L) = O(t^-3)

Open: state shifted-mesh uniformity as a standalone lemma with explicit
constant.
