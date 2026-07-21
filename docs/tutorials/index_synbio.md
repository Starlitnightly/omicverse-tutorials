# Synthetic Biology

Tutorials for the `omicverse.synbio` module — a self-contained **three-layer
design stack** that bridges **metabolism**, **protein / enzyme engineering**,
and **DNA**.

A synthetic-biology project rarely lives in one layer. You reason about a
pathway's *yield* (metabolism), the *enzymes* that carry its flux (protein),
and the *genes* you will actually build (DNA). `ov.synbio` puts all three in one
place — and, crucially, wires them together. Its signature is the **A↔B hinge**:
predict a turnover number from an enzyme's *sequence*, push it into a
genome-scale metabolic model as an enzyme-capacity constraint, and re-solve the
attainable *yield*. **Edit the enzyme → the metabolic network re-solves.**

| Layer | Functions |
|---|---|
| **A — metabolic** (COBRApy) | `load_gem`, `fba`, `pfba`, `fva`, `single_gene_deletion`, `double_gene_deletion`, `strain_design`, `production_envelope`, `ec_model`, `apply_kcat` |
| **B — protein/enzyme** (ESM / ProteinMPNN) | `predict_structure`, `inverse_design`, `denovo_backbone`, `variant_effect`, `stability_ddg`, `enzyme_kcat`, `enzyme_function`, `protein_embed` |
| **C — DNA** (DNAchisel / primer3) | `codon_optimize`, `design_primers` |

The introductory notebook runs all three layers on real data — the
`e_coli_core` genome-scale model, the 56-residue GB1 domain, and *E. coli*
phosphofructokinase — and closes with the A↔B coupling.

```{toctree}
:maxdepth: 1

../Tutorials-synbio/t_synbio_01_intro
```

## Installation

```bash
pip install 'omicverse[synbio]'
```

The metabolic and DNA layers are CPU-only (COBRApy with the free GLPK solver,
DNAchisel, primer3). The protein layer uses a GPU automatically when available
and reuses omicverse's existing PyTorch dependency; ESM / ESMFold / ProteinMPNN
weights download on first use to `~/.omicverse/synbio_weights` (override with
`OMICOS_SYNBIO_WEIGHTS`). Every backend is optional and gated behind an
actionable error — `import omicverse` never requires any of them.
