
# PB-ASYM-001 — Random-Mapping Stable-Count Asymptotics

**Canonical claim ID:** `PB-ASYM-001`  
**Legacy directory:** `research/pb-core-006/`  
**Subject:** Asymptotic analysis of the aggregate stable-equivalence count  
**Status:** research candidate; proof and certification obligations remain open

The directory name is retained for compatibility with existing links and
scripts. It does not mean that this research line has the same claim ID as
the aggregate-enumeration theorem in the main AQARION repository.

## Relationship to PB-CORE-006

`PB-CORE-006` is the separate AQARION claim concerning the aggregate
enumeration of pullback-fixed equivalence relations.

`PB-ASYM-001` studies asymptotic consequences of the aggregate counting
problem. Its dependency on PB-CORE-006 must be stated explicitly, and
neither claim inherits the other's evidence status.

The aggregate counting formula, its exact definitions, and its proof
status must be read from the authoritative AQARION artifacts:

- [Theorem overview](https://github.com/quantarion369-arch/AQARION/blob/main/AQARION-QUANTARION-AI/DOCS/THEOREMS/PB-CORE-006.md)
- [Theorem artifact](https://github.com/quantarion369-arch/AQARION/blob/main/AQARION-QUANTARION-AI/verification/PB/PB-CORE/PB-CORE-006-THEOREM.md)
- [Verification receipt](https://github.com/quantarion369-arch/AQARION/blob/main/AQARION-QUANTARION-AI/verification/PB/PB-CORE/PB-CORE-006_RECEIPT.json)

## Research files

| File | Role |
|---|---|
| `01-L1-Partition-Input.md` | Partition-function input and remainder requirements |
| `02-L2-Saddle-Expansion.md` | Local saddle expansion |
| `03-L3-Global-Tail.md` | Global envelope and tail separation |
| `04-L4-Discrete-Laplace.md` | Discrete-Laplace and shifted-mesh analysis |
| `05-D-Derivation.md` | Second-order coefficient derivation |
| `06-Audit-Report.md` | Corrections, evidence status, and unresolved obligations |
| `pb006_check.py` | Historical numerical checking script |
| `pb006_extrapolate.py` | Historical extrapolation script |

The filenames are retained for compatibility. The scripts' names do not
define the canonical claim identity.

## Evidence status

The following items must remain distinct:

1. Exact partition values produced by integer arithmetic.
2. Numerical checks of the proposed asymptotic coefficients.
3. Analytic proofs of local expansions and uniform remainders.
4. Proofs of global tail estimates.
5. Certification of numerical intervals, when required.
6. Formalization and successful build evidence.
7. Reproduction from a pinned commit and recorded environment.

A successful numerical fit does not establish an asymptotic theorem.
A local expansion does not establish a global result without tail control.
A proved aggregate counting formula does not prove the asymptotic claims
built on top of it.

## Current audit target

The immediate target is to close the stated analytic obligations in the
correct order:

1. Make each local expansion and remainder estimate precise.
2. Prove uniformity on the saddle window.
3. Establish the global envelope and tail separation with explicit bounds.
4. Justify the discrete approximation, including shifted-mesh uniformity.
5. Derive the coefficients from those established estimates.
6. Certify any claimed numerical intervals.
7. Reproduce the checks against a pinned source revision.
8. Update the evidence ledger only when the corresponding obligation is met.

**Governance:** No promotion based solely on numerical agreement.
