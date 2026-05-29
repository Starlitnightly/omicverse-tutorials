# Batch correction and data integration

When you concatenate single-cell data from multiple experiments — different
donors, sequencing runs, protocols, sites — every downstream analysis you
care about (clustering, trajectory, CCC) is contaminated by **batch
effect**: technical variation that pretends to be biology. omicverse exposes
a single entry point — `ov.single.batch_correction` — that dispatches to
**ten** backends spanning the methods compared in the
[scIB benchmark](https://www.nature.com/articles/s41592-021-01336-8)
(Luecken et al., 2022, *Nat Methods*) and the recent
[scIB-E deep-learning extension](https://www.biorxiv.org/content/10.1101/2024.12.09.627450)
(2024).

This section has three layers:

| Layer | Tutorial | When |
|---|---|---|
| **1. Recommended workflow** | [t_single_batch](t_single_batch.ipynb) | Day-one user. Side-by-side run of Harmony / ComBat / Scanorama / scVI / scANVI / totalVI / scPoli / CellANOVA / Concord / CCA on the NeurIPS 2021 multi-batch dataset, with `scib-metrics` benchmarking at the end. |
| **2. Backend zoo** | [zoo/index](zoo/index.md) | You want one focused tutorial per backend — same template (load → preprocess → call → embedding) with method-specific notes on inputs, key params, and traps. 10 tutorials, one per backend. |
| **3. Just the API** | [api/reference/omicverse.single.batch_correction](../../api/reference/omicverse.single.batch_correction.rst) | You already know the method you want and just need the signature. |

## Recommendation tree

```
              Do you have raw counts in adata.layers['counts']?
                            │
                ┌───────────yes───────────┐                no
                │                          │                │
       Atlas-scale (>200 k cells)?   Small / medium    ComBat (no counts needed)
        │                                │             or Seurat-CCA (pairwise)
   harmony (PCA-only)              Want deep-learning?
   or scanorama (MNN)                │
                            ┌────────┴────────┐
                            yes               no
                            │                 │
                Have partial labels?     Harmony / Scanorama
                  │                      (still strong defaults)
        ┌─────────┴─────────┐
        yes                 no
        │                    │
   scANVI (semi-           scVI (pure)
   supervised + label      or scPoli (conditional)
   transfer)
        │
   Have paired ADT counts?
        │
   ┌────┴────┐
   yes       no
   │          │
 totalVI    scANVI / scVI / scPoli
 (joint
  RNA+ADT)
```

## The ten backends

| `methods=` | Family | Touches expression? | Optional dep | When to reach for it |
|---|---|---|---|---|
| `'harmony'`    | Embedding (iterative clustering) | no | — | Fast default, atlas-scale, out-of-core. |
| `'combat'`     | Linear, empirical-Bayes | yes (matrix) | — | When you need a *corrected expression matrix*. |
| `'scanorama'`  | MNN panorama-stitch | yes (matrix) | scanorama | Differing compositions across batches. |
| `'scVI'`       | Deep VAE | only via latent | scvi-tools | Atlases with strong technical drift; many batches. |
| `'scANVI'` / `'SCANVI'` | Deep VAE + semi-supervised classifier | only via latent | scvi-tools | Have partial labels → batch-correct + label-transfer in one. |
| `'totalVI'` / `'TOTALVI'` | Deep VAE, joint RNA + ADT | only via latent | scvi-tools | CITE-seq / Total-seq, joint protein + RNA correction. |
| `'scPoli'` / `'SCPOLI'` | Conditional VAE with per-condition prototypes | only via latent | scArches | Reference building + query mapping; multi-condition. |
| `'CellANOVA'`  | Variance decomposition | yes (denoised) | cellanova | You can designate a control compartment. |
| `'Concord'`    | Contrastive learning | only via latent | concord-sc | GPU available; contrastive batch removal. |
| `'cca'` / `'seurat_cca'` / `'CCA'` | Canonical Correlation Analysis | yes (matrix) | pyccasc | Two-batch pairwise integration; Seurat parity, no R. |

## Unified output schema

Every backend writes its corrected representation to a stable obsm slot
(`adata.obsm['X_<method>']`) — `harmony` → `X_pca_harmony`, `combat` →
`X_combat`, `scVI` → `X_scVI`, etc. Downstream tools (cluster, UMAP, CCC)
consume any backend's output via this schema — no `if method == ...`
branching in your downstream code.

The mapping lives in `omicverse.single._batch._BATCH_OBSM` and drives the
`tracked` decorator's diagnostic-viz auto-attachment.

## Kwarg routing for the scvi-tools family

`scVI` / `scANVI` / `totalVI` / `scPoli` take many tunable parameters, split
between **architecture** (model `__init__`) and **optimisation** (model
`.train()`). The wrapper introspects each destination's signature and
routes your `**kwargs` automatically:

```python
ov.single.batch_correction(
    adata, batch_key="batch", methods="scVI",
    # Architecture params land in SCVI.__init__:
    n_latent=20, n_hidden=128, dropout_rate=0.1, gene_likelihood="zinb",
    # Optimisation params land in SCVI.train:
    max_epochs=200, batch_size=128, early_stopping=True, accelerator="cuda",
)
```

Unknown kwargs warn (and route to whichever destination has `**kwargs` for
forward-compatibility) rather than silently breaking. The same routing
applies to scANVI / totalVI / scPoli.

## References

- Luecken MD, Büttner M, Chaichoompu K, et al. *Benchmarking atlas-level
  data integration in single-cell genomics.* **Nat Methods** 19, 41–50
  (2022). [doi:10.1038/s41592-021-01336-8](https://doi.org/10.1038/s41592-021-01336-8)
- Yi C, et al. *Benchmarking deep learning methods for biologically conserved
  single-cell integration.* **biorXiv** 2024.
  [doi:10.1101/2024.12.09.627450](https://doi.org/10.1101/2024.12.09.627450)
- Korsunsky I, et al. *Fast, sensitive and accurate integration of
  single-cell data with Harmony.* **Nat Methods** 16, 1289–1296 (2019).
- Lopez R, et al. *Deep generative modeling for single-cell transcriptomics.*
  **Nat Methods** 15, 1053–1058 (2018).
- Xu C, et al. *Probabilistic harmonization and annotation of single-cell
  transcriptomics data with deep generative models.* **Mol Syst Biol** 17,
  e9620 (2021).
- Gayoso A, et al. *Joint probabilistic modeling of single-cell multi-omic
  data with totalVI.* **Nat Methods** 18, 272–282 (2021).
- De Donno C, et al. *Population-level integration of single-cell datasets
  enables multi-scale analysis across samples.* **Nat Methods** 20, 1683–1692
  (2023).
- Zhang T, et al. *CellANOVA: principled cell-type-aware analysis of
  variance for single-cell genomics.* **Nat Biotechnol** (2024).

```{toctree}
:maxdepth: 1
:hidden:

t_single_batch
zoo/index
```
