# Lemma 1 — Uniform partition input

**Status:** STATED · conditional on Nemes 2024 constants

## Setup

    a = pi * sqrt(2/3)
    x* = (a/2)^(2/3)
    t = n^(1/3)
    k = x* t^2 + y t^(3/2),  |y| <= sqrt(4 log t)

## Statement

    k p(k) = e^(a sqrt(k)) / (4 sqrt(3)) * [ 1 - (a/48 + 1/a)/sqrt(k) + R(k) ]

with

    |R(k)| <= K1/k + K2 * e^(-a sqrt(k)/2)

uniformly on the window. Consequence: `R(k) = O(t^-2)`.

## Derivation

Rademacher q=1 term with `N = k - 1/24`:

    p(k) = 1/(pi sqrt(2)) * d/dk [ sinh(a sqrt(N))/sqrt(N) ] + (q >= 2 tail)

Differentiate the dominant branch:

    p(k) = e^(a sqrt(N)) / (4 sqrt(3) N) * (1 - 1/(a sqrt(N))) + smaller terms

Multiply by k:

    k p(k) = (k/N) * e^(a sqrt(N)) / (4 sqrt(3)) * (1 - 1/(a sqrt(N))) + tail

Shift expansion:

    sqrt(N)   = sqrt(k) - 1/(48 sqrt(k)) + O(k^(-3/2))
    e^(a sqrt(N)) = e^(a sqrt(k)) * [1 - a/(48 sqrt(k)) + O(1/k)]
    1/(a sqrt(N)) = 1/(a sqrt(k)) + O(k^(-3/2))
    k/N = 1 + O(1/k)

Combining:

    k p(k) = e^(a sqrt(k)) / (4 sqrt(3)) * [ 1 - (a/48 + 1/a)/sqrt(k) + O(1/k) ]

## Source

Rademacher q=1 term; Lehmer remainder; Nemes 2024 Thm 1.1.
