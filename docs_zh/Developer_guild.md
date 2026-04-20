# 开发者指南

!!! Note
    为了更好地理解以下指南，您可以先阅读我们的 [论文](https://doi.org/10.1101/2023.06.06.543913)，了解总体思路。

以下将介绍框架的主要组件以及如何扩展现有实现。

## 框架结构

omicverse 的代码存放在 GitHub 仓库的 [omicverse 文件夹](https://github.com/Starlitnightly/omicverse/tree/master/omicverse) 中，
`__init__.py` 文件负责处理库函数的导入。

omicverse 框架主要由 5 个组件构成：

- `utils`：通用函数，包括数据处理、绘图等。
- `pp`：预处理，包括质量控制、归一化等。
- `bulk`：用于分析 bulk 组学测序数据，如 RNA-seq 或 Proper-seq。
- `single`：用于分析单细胞组学测序数据，如 scRNA-seq 或 scATAC-seq。
- `space`：用于分析空间 RNA-seq 数据。
- `bulk2single`：用于整合 bulk RNA-seq 与单细胞 RNA-seq。
- `external`：包含更多相关模块，避免安装冲突。

`__init__.py` 文件负责导入各文件夹内的函数入口，所有函数均使用以 `_*.py` 开头的文件进行编写。


## 面向开发者

### external 模块

在大多数情况下，我们意识到编写模块函数是比较困难的。因此，我们引入了 `external` 模块。
我们可以直接从 GitHub 克隆整个包，然后将整个文件夹移动到 `external` 文件夹中。
在此过程中，需要注意许可证是否允许，以及是否与 OmicVerse 的 GPL 许可证存在冲突。
随后，我们需要修改 `import` 内容，将不属于 OmicVerse 依赖的包从顶层导入改为函数级导入。

````shell
.
├── omicverse
├───── external
├──────── STT
├─────────── __init__.py
├─────────── pl
├─────────── tl
````

所有导入都需确保不存在冲突。

以下是一个错误示例，因为该包不在 OmicVerse 默认的 requirements.txt 中：

```python

import dgl

def calculate():
    dgl.run()
    pass

```

正确的导入方式为：

```python

def calculate():
    import dgl
    dgl.run()
    pass

```

我们推荐使用 `try` 捕获导入错误，从而引导用户访问正确的安装页面。


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

### 主模块

如果您想为 omicverse 提交 Pull Request，需要明确所开发功能归属于哪个模块。
例如，`TOSICA` 属于单细胞领域的算法，即需要在 `omicverse` 的 `single` 文件夹内添加 `_tosica.py` 文件，
并在 `_init__.py` 中添加 `from . _tosica import pyTOSICA`，使 omicverse 加入新功能。

````shell
.
├── omicverse
├───── single
├──────── __init__.py
├──────── _tosica.py
````

所有函数均需按以下格式提供参数说明：

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

### 为 OmicVerse 智能体注册函数

希望被智能体发现的函数必须使用 `@register_function` 进行装饰。
该装饰器位于 `omicverse.utils.registry` 中，
记录别名、类别和可读描述等关键元数据。
这些元数据会在意图检测和代码生成期间提供给智能体，因此请勿遗漏任何必填字段。

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

请确保至少提供一个别名、非空描述和类别；注册表验证会强制执行这些要求。
提供文档字符串和代表性示例可显著提升智能体建议和自动生成代码的质量。

### 让 dispatcher 出现在 `ov.report.from_anndata` 报告中

`ov.report.from_anndata(adata)` 会渲染一份 HTML 管线摘要：用户跑过的每一个 `ov.*` 公开调用对应一节，包含参数、代码块、耗时和若干诊断图。整个报告**完全由** `adata.uns['_ov_provenance']` 里的 provenance 日志驱动 —— 没有被 tracked dispatcher 记录过的步骤不会出现在报告里。scanner 不再去猜 `.obsm` / `.var` / `.uns` 里藏着哪些遗迹。

想让你新加的公开 dispatcher 出现在报告中，用 `@tracked(name, function)` 装饰它，并在分支里用 `note(...)` 声明运行时决定的元数据：

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

**`@tracked` 替你管的基础设施：**

- 壁钟计时。
- 原始 kwargs 抓取（不帮你补 default —— 报告忠实反映用户写的代码）。
- thread-local 嵌套栈：若此 dispatcher 被**另一个** `@tracked` dispatcher 内部调用，只有最外层的调用会生成 provenance 条目。这就是为什么 `ov.pp.qc(doublets_method='scrublet')` 只留一条 `qc` 记录，即便 qc 内部调用了 `ov.pp.scrublet`。
- 仅在成功时记录：若函数抛异常，暂存的条目会被丢弃。

**`note(**fields)` 用来补运行时决定的元数据：**

- `backend=<str>`：人类可读的 backend 标签。**在真正跑的那个分支里** resolve 它，让报告能忠实区分 scanpy / RAPIDS / torch 等 —— 不要试图在装饰器参数里塞一个静态字符串，因为多 backend dispatcher（`qc` / `neighbors` / `umap` / ...）在 dispatch 之前根本不知道走哪条分支。
- `viz=[{'function': 'ov.pl.<fn>', 'kwargs': {...}}, ...]`：一个或多个 `ov.pl.*` 调用，报告会照实执行它们作为该步骤的诊断图。每个 viz dict 会以跑完之后的 `adata` 为输入被逐字调用。优先复用现有的 `ov.pl.*` helper；如果没有合适的，先往 `omicverse/pl/` 里加一个再来 `note`。
- 用 `note(...)` 设置的任何字段都会被合并进 provenance 条目（例如 `note(summary=f'{n_doublets} doublets flagged')`）。

**经验规则：**

- `@tracked` 只用在**公开、面向用户**的 dispatcher 上 —— 也就是用户会在自己代码里写的那些名字。内部 helper（`omicverse.pp._neighbors.neighbors`、`omicverse.pp._umap.umap` 等）**不要**加 tracked；它们是实现细节，而且嵌套栈本来就会把它们静音。
- viz spec 尽量贴近实际计算处声明。如果你的 dispatcher 在两个算法之间选择，两条分支的诊断图不同（比如 `leiden` 在 `X_umap` 存在时顺手画个 embedding），就在 body 里 inline 分支：`note(viz=[..., *([...] if 'X_umap' in adata.obsm else [])])`。
- 单算法、没什么好画的步骤，只加 `@tracked(...)` 就够了 —— 报告里照样有参数、耗时和一个 "no diagnostic plot" 占位。
- 若 dispatcher 返回**副本**（`copy=True` 语义），装饰器会把条目写在返回的 AnnData 上而不是输入上；你不需要额外处理。
- 已经 `@tracked` 的 body 里不要直接调 `record_step` —— 装饰器负责 emit。

可参考 `omicverse/pp/_preprocess.py`（`umap` / `neighbors` / `leiden` / `pca` …）和 `omicverse/pp/_qc.py`（`qc`）的实现。这些 dispatcher 在真正的计算代码之外，每个分支只多了 2-4 行 `note(...)`，没有手动 `time.time()`、没有 `record_step(...)` 样板、也没有深度守卫簿记。

## Pull Request

1. 首先需要 `fork` omicverse，然后从您的仓库 git clone 您的 fork。
2. 完成相关功能开发后，发起 Pull Request 并等待审核与合并。

