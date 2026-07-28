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

- [Synthetic biology with `ov.synbio` — from metabolism to enzyme to DNA](t_synbio_01_intro.ipynb) — a single end-to-end tour of the metabolism/protein/DNA core on real data (`e_coli_core`, the GB1 domain, *E. coli* PfkA), closing with the A↔B coupling.
- [Circuits, CRISPR, assembly & pathway design](t_synbio_02_circuits_to_pathways.ipynb) — the rest of the design-build-test-learn cycle: genetic-circuit simulation (toggle / repressilator), regulatory-element strength, CRISPR guide design, Golden Gate assembly, pathway thermodynamics (MDF) & retrosynthesis, and library design.
- [CRISPR editing & directed-evolution libraries](t_synbio_03_crispr_library.ipynb) — guide-RNA design + off-target specificity (CFD), base editing & HDR knock-in, degenerate-codon / DMS libraries, and ESM model-guided variant design.
- [Advanced SOTA — mRNA design, de-novo binders, prime editing](t_synbio_04_advanced.ipynb) — the advanced state-of-the-art layer with baseline↔SOTA comparisons: mRNA therapeutics (**LinearDesign**), RNA / siRNA / antisense design, **prime editing** (PrimeDesign), CRISPRi/a & Cas13, dynamic FBA, minimal cut sets, retrobiosynthesis, and the full **de-novo binder** pipeline (**RFdiffusion → ProteinMPNN → Boltz-2**).

### Closing the gaps — reconstruction, omics coupling, and manufacturability

- [Building a strain from scratch — layer A end to end](t_synbio_05_strain_from_scratch.ipynb) — start where industrial work actually starts: an organism BiGG has no model for. Reconstruct by homology transfer, gap-fill, validate, constrain the model with a **real published *E. coli* protein-abundance table** (GIMME / iMAT / RIPTiDe), predict knockouts with MOMA and ROOM instead of FBA alone, derive OptForce MUST/FORCE sets, add thermodynamic and proteome-budget constraints, solve a two-member community, and hand the pathway to layer B via reaction→enzyme matching.
- [From a design to an order — manufacturability, kinetics, ancestors and DNA](t_synbio_06_design_to_order.ipynb) — the question that kills industrial enzyme projects: *can it be made?* Solubility, aggregation hotspots, signal peptides and localisation; K_M and k_cat/K_M and substrate scope; ancestral reconstruction for thermostability; then codon **harmonisation** (not optimisation), synthesis difficulty, Golden Gate overhang fidelity, terminator strength, truth-table→DNA compilation, biosecurity screening, and vector-backbone selection.

- [Design-Build-Test-Learn, on a loop that can be checked](t_synbio_07_dbtl_cycle.ipynb) — a DBTL cycle on a library where **every combination has already been measured** (Urtecho 2019, GEO GSE108535), so each step can be verified rather than asserted. A 64-run strength-2 orthogonal array replaces 512 combinations and recovers the full library's per-level effects at **r = 0.99 / 0.93 / 0.98**, identifying the best level of all three factors. Then the uncomfortable half: the additive model's recommended combination **ranks 77th of 512** because 30% of the variance is interaction, and the Gaussian process's predictions of its own proposals are **anti-correlated with measurement (r = -0.19)** — while the batch it chose still **found the global optimum**. Round 3 confirms it stops claiming improvement once the space is exhausted.
- [From a chosen design to files and instruments](t_synbio_08_build_and_order.ipynb) — the Build layer end to end, on the real 150-nt sequence of the winning promoter. Vector **first** (it fixes the sites the insert must avoid), then a codon-optimised CDS with the cloning enzymes excluded, a checked terminator, and a vendor-facing synthesis assessment. Fragments are prepared for both chemistries (`domesticate` for Golden Gate, `gibson_arms` for Gibson), assembled, annotated, and written as **GenBank and SBOL that are read back and compared**. Then a randomised edge-avoiding plate, equimolar volumes from ng/µL and length, an **Echo pick list that refuses to draw more than a source well holds**, an Opentrons protocol **verified with `opentrons_simulate`**, and a thermocycler program derived from the primers' Tm.

### Worked case studies

- [Case study I — an *E. coli* succinate cell factory](t_synbio_case01_succinate.ipynb) — a real metabolic-engineering project: diagnose, strain-design (FSEOF + OptKnock), verify, check thermodynamics (eQuilibrator + MDF), enzyme k_cat, and build.
- [Case study II — engineering a more thermostable DHFR](t_synbio_case02_dhfr_engineering.ipynb) — a real protein-engineering campaign on *E. coli* DHFR: CLEAN function, ESMFold, ESM fitness + ThermoMPNN stability landscapes, stabilised-variant design, and build.
- [Case study III — evaluating a protein design (does it get *better*?)](t_synbio_case03_dhfr_evaluation.ipynb) — score a DHFR variant with an in-silico metric panel (`evaluate_design`): a 3D WT-vs-variant structural overlay (`view_superposition` + self-consistency `structure_rmsd`), plus foldability / EC-retention / ΔΔG / ESM-fitness / kcat — each tagged with its **reliability**, and an honest read of what the numbers do and don't prove.

## Installation

```bash
pip install 'omicverse[synbio]'
```

The GPU protein models reuse omicverse's existing PyTorch dependency and
download weights on first use to `~/.omicverse/synbio_weights` (override with
`OMICOS_SYNBIO_WEIGHTS`). All backends are optional and gated behind actionable
errors, so `import omicverse` never requires them.
