# Batch-correction — backend zoo

This zoo holds one tutorial per `ov.single.batch_correction(methods=...)`
backend. Every tutorial follows the same template — load → preprocess →
call → embedding plot → key params → related — so you can swap methods by
changing one line.

## CPU-friendly backends (rendered with executed outputs)

These four train on CPU in under a minute on the pbmc3k 2-batch demo, and
are shipped with **executed outputs** so you can read them online without
running anything locally.

| Method | Tutorial | Family | Strength |
|---|---|---|---|
| Harmony | [t_batch_harmony](t_batch_harmony.ipynb) ✅ rendered | embedding (iterative clustering) | Fast default; out-of-core; atlas-scale. |
| ComBat  | [t_batch_combat](t_batch_combat.ipynb) ✅ rendered  | empirical-Bayes (matrix-level) | Returns a corrected expression matrix. |
| Scanorama | [t_batch_scanorama](t_batch_scanorama.ipynb) ✅ rendered | MNN panorama-stitch | Differing compositions across batches. |
| Seurat-CCA | [t_batch_cca](t_batch_cca.ipynb) ✅ rendered | Canonical correlation analysis | Two-batch pairwise; Seurat parity, no R / rpy2. |

## GPU-recommended backends (deep-learning — execute locally)

These five train a neural-network on the corrected latent representation,
and are **strongly GPU-recommended** for non-trivial datasets. The code
path was validated end to end in the [omicverse#797 integration test
suite](https://github.com/omicverse/omicverse/pull/797) but the notebooks
ship as code-only — run them yourself on a CUDA / MPS-equipped host to
populate outputs.

| Method | Tutorial | Optional dep | Family | Why GPU |
|---|---|---|---|---|
| scVI | [t_batch_scvi](t_batch_scvi.ipynb) ⚠️ run on GPU | `scvi-tools` | Deep VAE | PyTorch Lightning training, 100+ epochs on atlas-scale. |
| scANVI | [t_batch_scanvi](t_batch_scanvi.ipynb) ⚠️ run on GPU | `scvi-tools` | Deep VAE + classifier head | Same as scVI + classifier-head training. |
| totalVI | [t_batch_totalvi](t_batch_totalvi.ipynb) ⚠️ run on GPU | `scvi-tools` | Joint RNA + protein VAE | Larger model than scVI (RNA + protein heads). |
| scPoli | [t_batch_scpoli](t_batch_scpoli.ipynb) ⚠️ run on GPU | `scarches` | Conditional VAE with per-condition prototypes | PyTorch training with pretraining + fine-tune stages. |
| Concord | [t_batch_concord](t_batch_concord.ipynb) ⚠️ run on GPU | `concord-sc` | Contrastive learning | Negative-pair contrastive training. |

Each of these notebooks has a banner cell at the top reminding you to
execute on GPU; the recipe is the same `jupyter nbconvert --execute` for
all five.

## Real-control-compartment backend (needs domain-specific setup)

| Method | Tutorial | Optional dep | Family | Why not auto-rendered |
|---|---|---|---|---|
| CellANOVA | [t_batch_cellanova](t_batch_cellanova.ipynb) ⚙️ needs setup | `cellanova` | Variance decomposition | Requires `adata.uns['control_dict']` mapping to a real control compartment; a synthetic 2-batch demo produces shape-mismatched outputs. |

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
