# Second-order coefficient D

**Status:** CONDITIONAL · numeric to 6 digits

Expansion:

    R_n = K sqrt(n) e^(C t) (1 + D/t + O(t^-2))

Coefficients:

    D = x*/12 - 5/(72 x*^2) - (a/48 + 1/a)/sqrt(x*)
      = -0.35946517750585334143...

    E_log = (2 x*^9 - 75 x*^3 - 550) / (2160 x*^4)
          = -0.15842456538091719412...

Cross-check (Termux, 40 dps, exact partition table):

    D fit      = -0.3594656        (6 digits)
    E_log fit  = -0.1584248089     (7 digits)

No interval certification. No Lean proof.
