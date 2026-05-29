# Batch-correction — backend zoo

This zoo holds one tutorial per `ov.single.batch_correction(methods=...)`
backend. Every tutorial follows the same template — load → preprocess →
call → embedding plot → key params → related — so you can swap methods by
changing one line.

## Vendored backends (ship with omicverse)

| Method | Tutorial | Family | Strength |
|---|---|---|---|
| Harmony | [t_batch_harmony](t_batch_harmony.ipynb) | embedding (iterative clustering) | Fast default; out-of-core; atlas-scale. |
| ComBat  | [t_batch_combat](t_batch_combat.ipynb)   | empirical-Bayes (matrix-level) | Returns a corrected expression matrix. |

## Optional-dependency backends

| Method | Tutorial | Optional dep | Family | When to reach for it |
|---|---|---|---|---|
| Scanorama | [t_batch_scanorama](t_batch_scanorama.ipynb) | `scanorama` | MNN panorama-stitch | Differing compositions across batches. |
| scVI | [t_batch_scvi](t_batch_scvi.ipynb) | `scvi-tools` | Deep VAE | Atlases with heavy technical drift. |
| scANVI | [t_batch_scanvi](t_batch_scanvi.ipynb) | `scvi-tools` | Deep VAE + classifier head | Semi-supervised: batch-correct + label-transfer in one. |
| totalVI | [t_batch_totalvi](t_batch_totalvi.ipynb) | `scvi-tools` | Joint RNA + protein VAE | CITE-seq / Total-seq paired correction. |
| scPoli | [t_batch_scpoli](t_batch_scpoli.ipynb) | `scarches` | Conditional VAE with per-condition prototypes | Reference + query mapping. |
| CellANOVA | [t_batch_cellanova](t_batch_cellanova.ipynb) | `cellanova` | Variance decomposition | When you have a control compartment. |
| Concord | [t_batch_concord](t_batch_concord.ipynb) | `concord-sc` | Contrastive learning | GPU available; contrastive batch removal. |
| Seurat-CCA | [t_batch_cca](t_batch_cca.ipynb) | `pyccasc` | Canonical correlation analysis | Two-batch pairwise; Seurat parity, no R / rpy2. |

For the side-by-side comparison of every backend on the same dataset with
`scib-metrics` scoring at the end, see [../t_single_batch](../t_single_batch.ipynb).

## Architecture

Every backend writes its corrected representation to a stable obsm slot:

```
adata.obsm['X_pca_harmony']    # methods='harmony'
adata.obsm['X_combat']         # methods='combat'
adata.obsm['X_scanorama']      # methods='scanorama'
adata.obsm['X_scVI']           # methods='scVI'
adata.obsm['X_scANVI']         # methods='scANVI'
adata.obsm['X_totalVI']        # methods='totalVI'
adata.obsm['X_scPoli']         # methods='scPoli'
adata.obsm['X_cellanova']      # methods='CellANOVA'
adata.obsm['X_concord']        # methods='Concord'
adata.obsm['X_cca']            # methods='cca' / 'seurat_cca'
```

The mapping lives in `omicverse.single._batch._BATCH_OBSM` and drives both
the per-method tutorials and the `tracked` decorator's diagnostic-viz
auto-attachment. Downstream tools (cluster, UMAP, CCC) consume any
backend's output via this schema — no `if method == ...` branching in your
downstream code.

```{toctree}
:maxdepth: 1
:hidden:

t_batch_harmony
t_batch_combat
t_batch_scanorama
t_batch_scvi
t_batch_scanvi
t_batch_totalvi
t_batch_scpoli
t_batch_cellanova
t_batch_concord
t_batch_cca
```
