# Lemma 2 — Local saddle expansion

**Status:** ASSEMBLED · uniform remainder not written

## Falling-factorial expansion

    log((n)_k / n^k)
      = -k^2/(2n) + k/(2n) - k^3/(6n^2) + k^2/(4n^2) - k/(12n^2)
        - k^4/(12n^3) + k^3/(6n^3) - k^2/(12n^3) + R4

Remainder bound:

    0 >= R4 >= -Sigma4(k) / (4 n^4 (1 - k/n))

On the saddle scale: `R4 = O(t^-2)`.

## Local expansion

With `k = x* t^2 + y t^(3/2)`, `t = n^(1/3)`, `|y| <= sqrt(4 log t)`:

    A1(y) = -(x*^2 / 2) y + (1 / (8 x*)) y^3

    A2(y) = x*/2 - x*^4/12 - (x*/2) y^2 - (5 / (64 x*^2)) y^4

    B(y) = A2(y) + A1(y)^2 / 2 - (a/48 + 1/a)/sqrt(x*)

    S_{n,k} = e^(C t - x*^3/6) / (4 sqrt(3)) * e^(-3 y^2 / 4) *
              [ 1 + t^(-1/2) A1(y) + t^(-1) B(y) + O(t^(-3/2) (1 + |y|^6)) ]

## Gaussian moments

    E[Y^2] = 2/3
    E[Y^4] = 4/3
    E[Y^6] = 40/9

Odd terms integrate to zero. Even terms give:

    E[B(Y)] = x*/12 - 5/(72 x*^2) - (a/48 + 1/a)/sqrt(x*)
