# Tutorials of Synthetic Biology

Tutorials for the `omicverse.synbio` module — a self-contained **three-layer
design stack** that bridges metabolism, protein/enzyme engineering, and DNA:

- **Layer A — metabolic networks** (CPU, COBRApy): load genome-scale models,
  FBA / FVA / pFBA, gene-deletion scans, strain design (FSEOF + growth-coupled
  knockouts), and enzyme-constrained (GECKO-light) models.
- **Layer B — proteins & enzymes** (GPU, ESM / ProteinMPNN): ESMFold structure
  prediction, ESM-2 embeddings, zero-shot variant effect (in-silico directed
  evolution), ProteinMPNN inverse design, thermostability ΔΔG, and k_cat /
  EC-number prediction.
- **Layer C — DNA** (CPU, DNAchisel / primer3): codon optimization and PCR
  primer design.

The differentiator is the **A↔B hinge** — predict a turnover number from an
enzyme's sequence, push it into a genome-scale model as an enzyme-capacity
constraint, and re-solve the achievable yield. *Edit the enzyme → the metabolic
network re-solves its yield.*

## Getting started

- [Synthetic biology with `ov.synbio` — from metabolism to enzyme to DNA](t_synbio_01_intro.ipynb) — a single end-to-end tour of all three layers on real data (`e_coli_core`, the GB1 domain, *E. coli* PfkA), closing with the A↔B coupling.

## Installation

```bash
pip install 'omicverse[synbio]'
```

The GPU protein models reuse omicverse's existing PyTorch dependency and
download weights on first use to `~/.omicverse/synbio_weights` (override with
`OMICOS_SYNBIO_WEIGHTS`). All backends are optional and gated behind actionable
errors, so `import omicverse` never requires them.
