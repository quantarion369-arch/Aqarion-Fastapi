# Lemma 3 — Global tail

**Status:** CLOSED in outline

Define:

    f(x) = a sqrt(x) - x^2 / 2

Global envelope:

    S_{n,k} <= K * exp(t * f(k/t^2))

Saddle:

    f'(x) = a / (2 sqrt(x)) - x
    x* = (a/2)^(2/3)
    f(x*) = C = (3/2) x*^2
    f''(x*) = -3/2

Fixed-delta separation:

    sup_{|x - x*| >= delta} f(x) <= C - eta_delta
    => sum_{|k/t^2 - x*| >= delta} S_{n,k} = O(n e^((C - eta) t))

Moderate region:

    |x - x*| <= delta, |y| > L
    => S <= K e^(C t - c0 y^2 / 2)
    => tail <= t^(3/2) e^(-c0 L^2 / 2)

Choose `L(t) = sqrt(4 log t)`:

    e^(-c0 L^2 / 2) = t^(-2 c0) = o(t^-1)

Small-k and k ~ n covered by the same envelope.
