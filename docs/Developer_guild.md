# Developer guild

!!! Note
    To better understand the following guide, you may check out our [publication](https://doi.org/10.1101/2023.06.06.543913) first to learn about the general idea.

Below we describe main components of the framework, and how to extend the existing implementations.

## Framework

The omicverse code is stored in the [omicverse folder](https://github.com/Starlitnightly/omicverse/tree/master/omicverse) in the github repository, with the `__init__.py` file taking care of the import of the library functions.

A omicverse framework is primarily composed of 5 components.

- `utils`: Functions, including data, plotting, etc.
- `pp`: preprocess, including quantity control, normalize, etc.
- `bulk`: to analysis the bulk omic-seq like RNA-seq or Proper-seq.
- `single`: to analysis the single cell omic-seq like scRNA-seq or scATAC-seq
- `space`: to analysis the spatial RNA-seq
- `bulk2single`: to integrate the bulk RNA-seq and single cell RNA-seq
- `external`: more related module included RNA-seq avoided installation and confliction

The `__init__.py` file is responsible for importing function entries within each folder, and all function functions use a file starting with `_*.py` for function writing.


## For Developer

### external module

In most cases, we realize that writing a module function is difficult. Therefore, we introduced the `external` module. We can directly clone the entire package from GitHub and then move the entire folder to the `external` folder. During this process, we need to pay attention to whether the License allows it and whether there is a conflict with OmicVerse's GPL license. Subsequently, we need to modify the `import` content. We need to change the packages that are not dependencies of OmicVerse from top-level imports to function-level imports.

````shell
.
├── omicverse               
├───── external
├──────── STT
├─────────── __init__.py 
├─────────── pl
├─────────── tl
````

All imports need to ensure that there are no conflicts.

This is an error because this package is not included in the default requirements.txt of OmicVerse.

```python

import dgl 

def calculate():
    dgl.run()
    pass

```

The correct import is

```python

def calculate():
    import dgl 
    dgl.run()
    pass

```

We recommend using `try` to detect import errors, which can then guide the user to the correct installation page.


```python

def calculate():
    try:
        import dgl 
    except ImportError:
        raise ImportError(
            'Please install the dgl from https://www.dgl.ai/pages/start.html'
        )
    dgl.run()
    pass

```

### Main module

If you want to provide pull request for omicverse, you need to be clear about which module the functionality you are developing is subordinate to, e.g. `TOSICA` belongs to the algorithms of the single-cell domain, i.e., you need to add the `_tosica.py` file inside the `single` folder of `omicverse` and `_init__.py` inside the `from . _tosica import pyTOSICA` to make the omicverse add the new functionality

````shell
.
├── omicverse               
├───── single
├──────── __init__.py 
├──────── _tosica.py 
````

All functions require parameter descriptions in the following format:

```python

def preprocess(adata:anndata.AnnData, mode:str='scanpy', target_sum:int=50*1e4, n_HVGs:int=2000,
    organism:str='human', no_cc:bool=False)->anndata.AnnData:
    """
    Preprocesses the AnnData object adata using either a scanpy or a pearson residuals workflow for size normalization
    and highly variable genes (HVGs) selection, and calculates signature scores if necessary. 

    Arguments:
        adata: The data matrix.
        mode: The mode for size normalization and HVGs selection. It can be either 'scanpy' or 'pearson'. If 'scanpy', performs size normalization using scanpy's normalize_total() function and selects HVGs 
            using pegasus' highly_variable_features() function with batch correction. If 'pearson', selects HVGs 
            using scanpy's experimental.pp.highly_variable_genes() function with pearson residuals method and performs 
            size normalization using scanpy's experimental.pp.normalize_pearson_residuals() function. 
        target_sum: The target total count after normalization.
        n_HVGs: the number of HVGs to select.
        organism: The organism of the data. It can be either 'human' or 'mouse'. 
        no_cc: Whether to remove cc-correlated genes from HVGs.

    Returns:
        adata: The preprocessed data matrix. 
    """

```

### Registering functions for the OmicVerse Smart Agent

Functions that should be discoverable by the Smart Agent must be decorated with `@register_function`. The decorator lives in `omicverse.utils.registry` and records critical metadata such as aliases, category, and a human-readable description. This metadata is surfaced to the agent during intent detection and code generation, so omit none of the required fields.

```python
from omicverse.utils.registry import register_function


@register_function(
    aliases=["质控", "qc", "quality_control"],
    category="preprocessing",
    description="Perform standard single-cell quality control filtering",
    examples=["ov.pp.qc(adata, tresh={'mito_perc': 0.15, 'nUMIs': 500, 'detected_genes': 250})"],
)
def qc(adata, tresh=None):
    """Run OmicVerse QC on the provided AnnData."""
    ...
```

Be sure to provide at least one alias, a non-empty description, and a category; the registry validation enforces these requirements. Including docstrings and representative examples significantly improves the quality of agent suggestions and auto-generated code.

### Making a dispatcher appear in `ov.report.from_anndata`

`ov.report.from_anndata(adata)` renders a per-step HTML summary of the pipeline that produced the AnnData: for every public `ov.*` call the user ran, one section with parameters, a code block, timing, and one or more diagnostic plots. The report is driven **entirely** by a provenance log at `adata.uns['_ov_provenance']` — steps that didn't go through a tracked dispatcher simply do not appear. There is no heuristic sniffing of `.obsm` / `.var` / `.uns`.

If you're adding a new public dispatcher and you want it to show up in the report, decorate it with `@tracked(name, function)` and annotate branch-dependent metadata with `note(...)`:

```python
from omicverse.report._provenance import tracked, note, pick_color_key


@tracked('umap', 'ov.pp.umap')
def umap(adata, **kwargs):
    if settings.mode == 'cpu':
        _umap(adata, **kwargs)
        note(backend=f'omicverse({settings.mode}) · scanpy')
    elif settings.mode == 'cpu-gpu-mixed':
        _umap(adata, method='pumap', **kwargs)
        note(backend=f'omicverse({settings.mode}) · pumap')
    else:
        ...
        note(backend=f'omicverse({settings.mode}) · rapids')

    note(viz=[{
        'function': 'ov.pl.embedding',
        'kwargs':   {'basis': 'X_umap',
                     'color': pick_color_key(adata),
                     'frameon': 'small'},
    }])
```

**What `@tracked` does for you (infrastructure):**

- Wall-clock timing.
- Raw kwargs capture (no defaults filled in — the report records exactly what the user typed).
- A thread-local nesting stack: if this dispatcher is invoked from *another* `@tracked` dispatcher, only the outermost call emits a provenance entry. This is how e.g. `ov.pp.qc(doublets_method='scrublet')` produces a single `qc` entry even though it internally invokes `ov.pp.scrublet`.
- Success-only recording: on exception, the staged entry is discarded.

**What `note(**fields)` is for (runtime-decided metadata):**

- `backend=<str>`: a human-readable backend label. Resolve it *inside* the branch that actually ran, so the report faithfully distinguishes scanpy / RAPIDS / torch / etc. — don't try to pick a single string in a wrapping decorator call, because multi-backend dispatchers (`qc` / `neighbors` / `umap` / ...) can't know which branch will run until the dispatch is done.
- `viz=[{'function': 'ov.pl.<fn>', 'kwargs': {...}}, ...]`: one or more `ov.pl.*` calls the report should render as diagnostic plots for this step. Each viz dict is executed verbatim against the post-run `adata`. Prefer existing `ov.pl.*` helpers; add a new helper to `omicverse/pl/` first if none fits.
- Any other field you set with `note(...)` is merged into the provenance entry (e.g. `note(summary=f'{n_doublets} doublets flagged')`).

**Rules of thumb:**

- `@tracked` goes on **public, user-facing** dispatchers — the ones whose names a user types. Internal helpers (`omicverse.pp._neighbors.neighbors`, `omicverse.pp._umap.umap`, etc.) should **not** be tracked; they're implementation detail and the nesting stack would silence them anyway.
- Declare `viz` specs as close to the actual computation as possible. If your dispatcher picks between two algorithms with different diagnostic plots (e.g. `leiden` optionally plotting an embedding when `X_umap` exists), branch on it inline: `note(viz=[..., *([...] if 'X_umap' in adata.obsm else [])])`.
- For a single-algorithm step with no interesting plot, just `@tracked(...)` is fine — the report will show parameters, timing, and a "no diagnostic plot" placeholder.
- If the dispatcher returns a **copy** (`copy=True` semantics), the decorator writes the entry on the returned AnnData rather than the input; you don't need to do anything special for this.
- Never call `record_step` directly from a body you've already decorated with `@tracked` — the decorator owns the emit.

For a reference, see `omicverse/pp/_preprocess.py` (`umap`, `neighbors`, `leiden`, `pca` …) and `omicverse/pp/_qc.py` (`qc`). These dispatchers are ~2-4 lines of `note(...)` per branch beyond the actual computation, with no manual `time.time()`, no `record_step(...)` boilerplate, and no depth-guard bookkeeping.

## Pull request

1. You need to `fork` omicverse at first, and git clone your fork from your repository.
2. When you updated the related function development, open a pull request and waited reviewed and merged.

