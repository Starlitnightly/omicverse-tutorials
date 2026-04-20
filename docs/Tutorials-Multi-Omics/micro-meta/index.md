# Microbe ↔ Metabolite paired integration

Tutorials that fuse `ov.micro` (16S / amplicon counts) with `ov.metabol`
(targeted or untargeted LC-MS) on shared sample sets — the minimum
requirement is that both AnnDatas share `obs_names`.

## Tutorials

- [Paired microbe ↔ metabolite integration (MMvec-style)](t_micro_metabol_paired.ipynb)
  — Spearman on CLR, Canonical Correlation Analysis, and a minimal
  PyTorch implementation of MMvec's bilinear log-conditional model.
