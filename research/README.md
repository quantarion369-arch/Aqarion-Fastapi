
# AQARION Research Artifacts

This directory contains research notes, derivations, numerical checks, and
audit records associated with the AQARION research stack.

## Research claims

### PB-ASYM-001 — Random-mapping stable-count asymptotics

**Canonical claim ID:** `PB-ASYM-001`

**Research location:** `research/pb-core-006/`  
**Location status:** legacy directory name retained for link compatibility  
**Subject:** Asymptotic analysis of the aggregate stable-equivalence count.

This research line investigates asymptotic behavior derived from the
aggregate enumeration of pullback-fixed equivalence relations. Its
saddle expansion, tail estimates, discrete-Laplace analysis, and numerical
coefficient checks belong to this asymptotic claim.

The directory name `pb-core-006` is historical. It is not the canonical
identity of this asymptotic claim.

### Dependency: PB-CORE-006 — Aggregate enumeration

The authoritative aggregate-enumeration claim is maintained in the
separate repository:

- [PB-CORE-006 theorem overview](https://github.com/quantarion369-arch/AQARION/blob/main/AQARION-QUANTARION-AI/DOCS/THEOREMS/PB-CORE-006.md)
- [PB-CORE-006 theorem artifact](https://github.com/quantarion369-arch/AQARION/blob/main/AQARION-QUANTARION-AI/verification/PB/PB-CORE/PB-CORE-006-THEOREM.md)
- [PB-CORE-006 verification receipt](https://github.com/quantarion369-arch/AQARION/blob/main/AQARION-QUANTARION-AI/verification/PB/PB-CORE/PB-CORE-006_RECEIPT.json)

PB-ASYM-001 depends on the aggregate-counting formula and its definitions.
It does not inherit proof status, verification status, or publication
approval automatically.

A proved finite counting identity would not, by itself, prove an
asymptotic expansion. The latter additionally requires valid asymptotic
estimates, uniform remainder bounds, control of tails, and any necessary
coefficient or interval certification.

## Evidence boundary

The following are distinct forms of evidence:

- Exact integer computation of partition numbers.
- Numerical comparison with an asymptotic approximation.
- A formal or analytic proof of the aggregate counting identity.
- A proof of an asymptotic expansion with quantified remainders.
- Independent reproduction tied to an exact source revision.
- Lean formalization and successful build evidence.

No one item substitutes for the others.

In particular, a numerical fit for a second-order coefficient is not an
interval proof of that coefficient, and a passing numerical check does not
establish a global error bound.

## Current research status

The detailed status of the asymptotic components is recorded in
`pb-core-006/06-Audit-Report.md`. That record must be read as the status
of PB-ASYM-001, not as the status of the PB-CORE-006 aggregate theorem.

The historical directory and filenames are retained to avoid silently
breaking existing links. New documents, reports, and receipts should use
the canonical identifier `PB-ASYM-001`.

## Governance

FROZEN · ADVERSARIAL · NO FABRICATION · NO PROMOTION

Any status change must be supported by the corresponding proof,
reproducibility record, and review. Updating an identifier does not upgrade
the evidence supporting a mathematical claim.
