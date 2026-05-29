# Batch-correction — backend zoo

This zoo holds one tutorial per `ov.single.batch_correction(methods=...)`
backend. Every tutorial follows the same template — load → preprocess →
call → embedding plot → key params → related — so you can swap methods by
changing one line.

All ten notebooks ship with **executed outputs** rendered against real
data — there is no code-only mode. Demos run on a ~6 000-cell subsample
of the NeurIPS 2021 multi-batch hematopoiesis dataset (3 real donors,
pre-annotated `cell_type`), except totalVI which uses
`scvi.data.pbmcs_10x_cite_seq` because it needs real protein counts.

## CPU-friendly backends

Train on CPU in under a minute on the demo dataset.

| Method | Tutorial | Family | Strength |
|---|---|---|---|
| Harmony | [t_batch_harmony](t_batch_harmony.ipynb) ✅ | embedding (iterative clustering) | Fast default; out-of-core; atlas-scale. |
| ComBat  | [t_batch_combat](t_batch_combat.ipynb) ✅  | empirical-Bayes (matrix-level) | Returns a corrected expression matrix. |
| Scanorama | [t_batch_scanorama](t_batch_scanorama.ipynb) ✅ | MNN panorama-stitch | Differing compositions across batches. |
| Seurat-CCA | [t_batch_cca](t_batch_cca.ipynb) ✅ | Canonical correlation analysis | Two-batch pairwise; Seurat parity, no R / rpy2. |

## Deep-learning backends (GPU-recommended)

Train a neural network on the corrected latent representation. The
rendered outputs were produced on an H100 in 1.5–5 min per notebook with
each library's default `max_epochs` (scvi-tools auto-derives ≈400 epochs
for ~6 k cells; scPoli defaults to 100). For larger datasets a GPU is
strongly recommended; on CPU expect 10–30× longer.

| Method | Tutorial | Optional dep | Family | Notes |
|---|---|---|---|---|
| scVI | [t_batch_scvi](t_batch_scvi.ipynb) ✅ | `scvi-tools` | Deep VAE | Standard generative scRNA model with batch as covariate. |
| scANVI | [t_batch_scanvi](t_batch_scanvi.ipynb) ✅ | `scvi-tools` | Deep VAE + classifier head | Semi-supervised; requires `labels_key=`. |
| totalVI | [t_batch_totalvi](t_batch_totalvi.ipynb) ✅ | `scvi-tools` | Joint RNA + protein VAE | Needs raw protein counts in `obsm[...]`. |
| scPoli | [t_batch_scpoli](t_batch_scpoli.ipynb) ✅ | `scarches` | Conditional VAE with per-condition prototypes | Two-stage pretraining + fine-tune. |
| Concord | [t_batch_concord](t_batch_concord.ipynb) ✅ | `concord-sc` | Contrastive learning | Negative-pair contrastive training. |

## Variance-decomposition backend

| Method | Tutorial | Optional dep | Family | Notes |
|---|---|---|---|---|
| CellANOVA | [t_batch_cellanova](t_batch_cellanova.ipynb) ✅ | `cellanova` | Variance decomposition | Requires `control_dict={pool_name: [batch_labels]}` mapping cells expected to be biologically homogeneous across batches. |

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
