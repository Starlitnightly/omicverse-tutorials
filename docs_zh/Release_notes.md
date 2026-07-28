# 版本发布说明

## v 1.0.0
- 首次公开发布。

## v 1.1.7
### bulk 模块：
- 新增 Deseq2，包含 `pyDEseq` 函数：`deseq2_normalize`、`estimateSizeFactors`、`estimateDispersions`、`Matrix_ID_mapping`。
- 集成 TCGA，提供 `TCGA` 功能。
- 引入富集分析，包含函数 `geneset_enrichment`、`geneset_plot`。

### single 模块：
- 集成 scdrug，提供函数 `autoResolution`、`writeGEP`、`Drug_Response`。
- 新增 cpdb，提供函数 `cpdb_network_cal`、`cpdb_plot_network`、`cpdb_plot_interaction`、`cpdb_interaction_filtered`。
- 集成 scgsea，提供函数 `geneset_aucell`、`pathway_aucell`、`pathway_aucell_enrichment`、`pathway_enrichment`、`pathway_enrichment_plot`。

## v 1.1.8
### single 模块：
- 修复 cpdb 中的错误，包括 `cpdb_plot_network` 的导入错误和颜色问题。
- 在 cpdb 中引入 `cpdb_submeans_exacted`，便于提取子网络。

## v 1.1.9
### bulk2single 模块：
- 新增 `bulk2single` 模块。
- 修复来自 bulk2space 的模型加载错误。
- 解决来自 bulk2space 的早停问题。
- 提供更友好的输入方式和可视化功能。
- 新增损失历史可视化。

### utils 模块：
- 在 plot 模块中引入 `pyomic_palette`。

## v 1.1.10
- 更新所有代码引用。

### single 模块：
- 修复 `single.mofa.mofa_run` 函数中的无效参数。
- 在 `single.scanpy_lazy` 函数中新增原始计数层。
- 引入 `utils.plot_boxplot`，用于绘制带抖动点的箱线图。
- 新增 `bulk.pyDEseq.plot_boxplot`，用于绘制特定基因的带抖动点箱线图。

## v 1.2.0
### bulk 模块：
- 修复 `bulk.geneset_enrichment` 中无效的 `cutoff` 参数。
- 新增模块：`pyPPI`、`pyGSEA`、`pyWGCNA`、`pyTCGA`、`pyDEG`。

### bulk2single 模块：
- 引入 `bulk2single.save`，用于手动保存模型。

## v 1.2.1-4
### single 模块：
- 新增 `pySCSA` 模块，包含函数：`cell_anno`、`cell_anno_print`、`cell_auto_anno`、`get_model_tissue`。
- 在 `single.scanpy_lazy` 中实现双细胞过滤。
- 新增 `single.scanpy_cellanno_from_dict`，简化注释流程。
- 将 SCSA 数据库更新至 [CellMarker2.0](http://bio-bigdata.hrbmu.edu.cn/CellMarker/)。
- 修复 SCSA 数据库键名错误：`Ensembl_HGNC` 和 `Ensembl_Mouse`。

## v 1.2.5
### single 模块：
- 新增 `pyVIA` 模块，包含函数：`run`、`plot_piechart_graph`、`plot_stream`、`plot_trajectory_gams`、`plot_lineage_probability`、`plot_gene_trend`、`plot_gene_trend_heatmap`、`plot_clustergraph`。
- 修复 `utils.pyomic_plot_set` 中的警告错误。
- 更新依赖项，包括 `pybind11`、`hnswlib`、`termcolor`、`pygam`、`pillow`、`gdown`。

## v 1.2.6
### single 模块：
- 新增 `pyVIA.get_piechart_dict` 和 `pyVIA.get_pseudotime`。

## v 1.2.7
### bulk2single 模块：
- 新增 `Single2Spatial` 模块，包含函数：`load`、`save`、`train`、`spot_assess`。
- 修复 pip 中的包安装错误。

## v 1.2.8
- 修复 pip 安装错误。

### bulk2single 模块：
- 将 `Single2Spatial` 中的 `deep-forest` 替换为 `Neuron Network` 用于分类任务。
- 通过修改 `predicted_size` 设置，使用 GPU 和批次级估算加速整个 Single2Spatial 推理过程。

## v 1.2.9
### bulk 模块：
- 修复 `Matrix_ID_mapping` 中的重复索引映射问题。
- 解决 `pyWGCNA.plot_sub_network` 中的 hub 基因绘图问题。
- 修复 `pyGSEA.geneset_enrichment` 中的备用基因，以支持稀有物种。
- 在 `pyWGCNA.plot_matrix` 中新增矩阵绘图模块。

### single 模块：
- 在 `pySCSA` 中新增 `rank_genes_groups` 检查。

### bulk2single 模块：
- 修复 `deepforest` 的导入错误。

## v 1.2.10
- 将包重命名为 `omicverse`。

### single 模块：
- 修复 `pySCSA` 中的参数错误。

### bulk2single 模块：
- 更新 `bulk2single` 中的绘图参数。

## v 1.2.11
### bulk 模块：
- 修复 `pyDEG.deg_analysis` 中的 `wilcoxon` 方法。
- 在 `pyDEG.plot_boxplot` 中新增处理组和对照组名称的参数设置。
- 修复 `pyWGCNA.plot_matrix` 中的图形显示问题。
- 修复 `pyWGCNA.analysis_meta_correlation` 中因独热编码导致的类别相关性失败问题。
- 修复 `pyWGCNA.plot_sub_network` 中的网络显示问题，并更新 `utils.plot_network` 以避免错误。

## v 1.3.0
### bulk 模块：
- 在 `pyDEG.deg_analysis` 中新增 `DEseq2` 方法。
- 在 `bulk` 中引入 `pyGSEA` 模块。
- 将原始 `pyGSEA` 重命名为 `bulk` 中的 `pyGSE`。
- 在 `utils` 中新增 `get_gene_annotation`，用于基因名称转换。

## v 1.3.1
### single 模块：
- 新增 `get_celltype_marker` 方法。

### single 模块：
- 新增 `GLUE_pair`、`pyMOFA`、`pyMOFAART` 模块。
- 新增 `Multi omics analysis by MOFA and GLUE` 教程。
- 更新 `Multi omics analysis by MOFA` 教程。

## v 1.4.0
### bulk2single 模块：
- 新增 `BulkTrajBlend` 方法。

### single 模块：
- 修复 `scnocd` 模型中的错误。
- 在 `scnocd` 模型中新增 `save`、`load` 和 `get_pair_dict`。

### utils 模块：
- 新增 `mde` 方法。
- 在 `utils.read` 中新增 `gz` 格式支持。

## v 1.4.1
### preprocess 模块：
- 新增 `pp`（预处理）模块，包含 `qc`（质量控制）、`hvg`（高变基因）、`pca`。
- 从 [Cellula](https://github.com/andrecossa5/Cellula/) 和 [pegasus](https://github.com/lilab-bcb/pegasus/) 引入用于细胞周期计算的 `data_files`。

## v 1.4.3
### preprocess 模块：
- 修复 `pp` 中的稀疏预处理错误。
- 修复 `via` 中的轨迹导入错误。
- 新增轨迹基因相关性分析。

## v 1.4.4
### single 模块：
- 在 `pySCSA` 模块中新增 `panglaodb` 数据库。
- 修复 `pySCSA.cell_auto_anno` 在某些细胞类型未在聚类中找到时的错误。
- 修复 `pySCSA.cell_anno` 在 `rank_genes_groups` 与聚类不一致时的错误。
- 在 single 中新增 `pySIMBA` 模块，用于批次校正。

### preprocess 模块：
- 在 `ov.utils` 中新增 `store_layers` 和 `retrieve_layers`。
- 在 `ov.utils` 中新增 `plot_embedding_celltype` 和 `plot_cellproportion`。

## v 1.4.5
### single 模块：
- 新增 `MetaTiME` 模块，用于在 TME 中自动执行细胞类型注释。

## v 1.4.12
- 更新 `conda install omicverse -c conda-forge`。

### single 模块：
- 新增 `pyTOSICA` 模块，使用 Transformer 模型从参考 scRNA-seq 中执行细胞类型迁移。
- 新增 `atac_concat_get_index`、`atac_concat_inner`、`atac_concat_outer` 函数，用于合并/拼接 scATAC 数据。
- 修复 `MetaTime.predicted` 在出现未知细胞类型时的问题。

### preprocess 模块：
- 在 `ov.utils` 中新增 `plot_embedding`，使用特定颜色字典绘制 UMAP。

## v 1.4.13
### bulk 模块：
- 在 `ov.bulk.pyWGCNA` 模块中新增 `mad_filtered`，用于在计算网络时过滤鲁棒基因。
- 修复 `ov.bulk.pyPPI` 中的 `string_interaction`，适配 string-db 更新。

### preprocess 模块：
- 修改 `pp.preprocess` 的 `mode` 参数以控制预处理步骤。
- 新增 `ov.utils.embedding`、`ov.utils.neighbors` 和 `ov.utils.stacking_vol`。

## v 1.4.14
### preprocess 模块：
- 在 `pp.preprocess` 和 `pp.qc` 中新增 `batch_key`。

### utils 模块：
- 新增 `plot_ConvexHull`，用于可视化聚类边界。
- 新增 `weighted_knn_trainer` 和 `weighted_knn_transfer`，用于多 adata 整合。

### single 模块：
- 修复 `mofa` 中的导入错误。

## v 1.4.17
### bulk 模块：
- 修复与 `pydeseq2` 版本 `0.4.0` 的兼容性问题。
- 新增 `bulk.batch_correction`，用于多 bulk RNA-seq/芯片样本的批次校正。

### single 模块：
- 新增 `single.batch_correction`，用于多单细胞数据集的批次校正。

### preprocess 模块：
- 在 `pp.scale` 中新增 `layers_add` 参数。

## v 1.5.0
### single 模块：
- 新增 `cellfategenie`，用于计算时间相关基因/基因集。
- 修复 `atac_concat_outer` 中的名称错误。
- 为 `batch_correction` 新增更多 kwargs。

### utils 模块：
- 新增 `plot_heatmap`，用于可视化伪时间热图。
- 修复 `embedding` 在 `mpl` 版本大于 `3.7.0` 时的问题。
- 新增 `geneset_wordcloud`，用于可视化伪时间基因集热图。

## v 1.5.1
### single 模块：
- 新增 `scLTNN`，用于推断细胞轨迹。

### bulk2single 模块：
- 使用 `TAPE` 更新 bulk2single 中的细胞比例预测。
- 修复 bulk2single 中的分组和归一化问题。

### utils 模块：
- 新增 `Ro/e` 计算（作者：Haihao Zhang）。
- 新增 `cal_paga` 和 `plot_paga`，用于可视化状态转移矩阵。
- 修复 `read` 函数。

## v 1.5.2
### bulk2single 模块：
- 解决基因符号不唯一时发生的矩阵错误。
- 修复 `BulkTrajBlend` 在目标细胞不存在时的 `interpolation` 问题。
- 修正 `BulkTrajBlend` 中的 `generate` 函数。
- 修正 `BulkTrajBlend` 中 `cell_target_num` 设置为 None 时 `vae_configure` 的参数错误。
- 引入 `max_single_cells` 参数，用于 `BulkTrajBlend` 的输入配置。
- bulk RNA-seq 去卷积默认使用 `scaden`。

### single 模块：
- 修复 `pyVIA` 在 root 设置为 None 时的错误。
- 新增 `TrajInfer` 模块，用于推断细胞轨迹。
- 将 `Palantir` 和 `Diffusion_map` 集成到 `TrajInfer` 模块。
- 修正 `batch_correction` 中的参数错误。

### utils 模块：
- 引入 `plot_pca_variance_ratio`，用于可视化 PCA 方差比例。
- 新增 `cluster` 和 `filtered` 模块，用于细胞聚类。
- 集成 `MiRA`，用于计算 LDA 主题。

## v 1.5.3
### single 模块：
- 新增 `scVI` 和 `MIRA`，用于去除批次效应。

### space 模块：
- 新增 `STAGATE`，用于空间 RNA-seq 的聚类与去噪。

### pp 模块：
- 在 `ov.pp.qc` 中新增 `doublets` 参数，用于控制双细胞检测（默认值为 True）。

## v 1.5.4
### bulk 模块：
- 修复 `pyDEG.deg_analysis` 在 `pyDeseq2(v0.4.3)` 中无法设置 `n_cpus` 时的错误。

### single 模块：
- 修复 `single.batch_correction` 中 combat 的参数错误。

### utils 模块：
- 新增 `venn4` 图，用于可视化。
- 修复 `plot_network` 的标签可视化问题。
- 在 `LDA_topic` 中新增 `ondisk` 参数。

### space 模块：
- 新增 `Tangram`，用于将 scRNA-seq 映射到 stRNA-seq。

## v 1.5.5
### pp 模块：
- 新增 `max_cells_ratio` 和 `max_genes_ratio`，用于控制 scRNA-seq 质控中的最大阈值。

### single 模块：
- 新增 `SEACells` 模型，用于从 scRNA-seq 计算元细胞。

### space 模块：
- 新增 `STAligner`，用于整合多个 stRNA-seq 数据集。

## v 1.5.6
### pp 模块
- 新增 `mt_startswith` 参数，用于控制小鼠或其他物种的 `qc`。

### utils 模块
- 新增 `schist` 方法，用于单细胞 RNA-seq 聚类。

### single 模块
- 修复 SEACells 中 `palantir` 的导入错误。
- 新增 `CEFCON` 模型，用于识别细胞命运决定的驱动调控因子。

### bulk2single 模块
- 在 nocd 配置中新增 `use_rep` 和 `neighbor_rep` 参数。

### space 模块
- 新增 `SpaceFlow`，用于识别伪空间图谱。

## v 1.5.8

### pp 模块
- 新增 `score_genes_cell_cycle` 函数，用于计算细胞周期。

### bulk 模块
- 修复 `adjustText` 版本大于 `0.9` 时 `dds.plot_volcano` 文本绘制错误。

### single 模块
- 优化 `MetaCell.load` 模型加载逻辑。
- 修复使用 `MetaCell.load` 加载模型时的错误。
- 新增 `Metacells` 教程。

### pl 模块

将 `pl` 作为下一版本统一绘图前缀，用于替代原 utils 中的绘图功能，同时保留原有 utils 中的绘图接口。

- 新增 `embedding`，使用 `ov.pl.embedding` 绘制 scRNA-seq 嵌入图。
- 新增 `optim_palette`，提供空间约束方法，为各种场景下的单细胞空间数据可视化生成具有区分度的颜色分配。
- 新增 `cellproportion`，绘制 scRNA-seq 堆叠条形比例图。
- 新增 `embedding_celltype`，同时绘制细胞类型比例和嵌入图。
- 新增 `ConvexHull`，在目标细胞周围绘制凸包。
- 新增 `embedding_adjust`，调整嵌入图中细胞类型图例的文字。
- 新增 `embedding_density`，绘制细胞中的类别密度。
- 新增 `bardotplot`，绘制不同组间的条点图。
- 新增 `add_palue`，绘制不同组间的 p 值阈值。
- 新增 `embedding_multi`，支持 `mudata` 对象。
- 新增 `purple_color`，用于紫色调色板可视化。
- 新增 `venn`，支持从 2 到 4 个集合的韦恩图。
- 新增 `boxplot`，用于可视化箱点图。
- 新增 `volcano`，用于可视化差异表达基因结果。

## v 1.5.9

### single 模块

- 在 `single.TrajInfer` 中新增 `slingshot`。
- 修复 `scLTNN` 的若干错误。
- 新增 `GPU` 模式，用于 GPU 加速数据预处理。
- 新增 `cNMF`，用于计算 NMF。

### space 模块

- 新增 `Spatrio`，用于将 scRNA-seq 映射到 stRNA-seq。

## v 1.6.0

将 `CEFCON`、`GNTD`、`mofapy2`、`spaceflow`、`spatrio`、`STAligner`、`tosica` 从根模块移至 external 模块。

### space 模块

- 在 `omicverse.space` 中新增 `STT`，用于计算空间转移张量。
- 在 `omicverse.external` 中新增 `scSLAT`，用于不同空间切片的对齐。
- 在 `omicverse.external` 中新增 `PROST`，在 `omicverse.space` 中新增 `svg`，用于识别空间可变基因和空间域。

### single 模块

- 在 `omicverse.single.cNMF` 中新增 `get_results_rfc`，用于预测复杂 scRNA-seq/stRNA-seq 中的精确聚类。
- 在 `omicverse.utils.LDA_topic` 中新增 `get_results_rfc`，用于预测复杂 scRNA-seq/stRNA-seq 中的精确聚类。
- 在 `omicverse.single` 中新增 `gptcelltype`，使用大语言模型进行细胞类型注释（#82）。

### pl 模块

- 在 `omicverse.pl` 中新增 `plot_spatial`，用于可视化去卷积时的 spot 细胞比例。

## v 1.6.2

支持原生 Windows 平台。

- 在 `omicverse.pp` 中新增 `mde`，用于加速 UMAP 计算。

## v 1.6.3

- 新增 `ov.setting.cpu_init`，用于将环境切换到 CPU 模式。
- 将 `tape`、`SEACells` 和 `palantir` 模块移至 `external`。

### Single 模块
- 新增 `CytoTrace2`，用于从单细胞 RNA 测序数据预测细胞潜能类别和绝对发育潜力。
- 新增 `cpdb_exact_target` 和 `cpdb_exact_source`，用于提取特定配体/受体的均值。
- 新增 `gptcelltype_local`，使用本地 LLM 识别细胞类型（#96 #99）。

### Bulk 模块
- 在 dds.result 中新增 `MaxBaseMean` 列，帮助用户忽略空样本。

### Space 模块
- 在 `STT.compute_pathway` 中新增 `**kwargs`。
- 新增 `GraphST`，用于识别空间域。

### pl 模块
- 新增 `cpdb_network`、`cpdb_chord`、`cpdb_heatmap`、`cpdb_interacting_network`、`cpdb_interacting_heatmap` 和 `cpdb_group_heatmap`，用于可视化 CellPhoneDB 结果。

### utils 模块
- 新增 `mclust_py`，用于识别高斯混合聚类。
- 在 `cluster` 函数中新增 `mclust` 方法。

## v 1.6.4

### Bulk 模块

- 优化 pyGSEA 的 `geneset_plot` 坐标效果可视化。
- 修复 `pyTCGA.survival_analysis` 在矩阵稀疏时的错误（#62、#68、#95）。
- 添加 tqdm，用于可视化 `pyTCGA.survial_analysis_all` 的处理进度。
- 修复 `data_drop_duplicates_index` 删除重复索引时仅保留表达量最高基因的错误（#45）。
- 在 `ov.bulk` 中新增 `geneset_plot_multi`，用于可视化多个富集结果（#103）。

### Single 模块

- 新增 `mellon_density`，用于计算细胞密度（#103）。

### PP 模块
- 修复 `ov.pp.pca` 在主成分数小于 13 时的错误（#102）。
- 在 `ov.pp.qc` 的方法中新增 `COMPOSITE`，用于预测双细胞（#103）。
- 在 `score_genes_cell_cycle` 中新增 `species` 参数，无需手动输入基因即可计算细胞周期。

## v 1.6.6

### Pl 模块

- 修复 `ov.pl.cpdb_group_heatmap` 中的 `celltype_key` 错误（#109）。
- 修复 `ov.utils.roe` 在某些期望频率低于期望值时的错误。
- 新增 `cellstackarea`，用于可视化样本中细胞类型的百分比堆积面积图。

### Single 模块
- 修复 `ov.single.cytotrace2` 在 adata.X 非稀疏数据时的 bug（#115、#116）。
- 修复 SEACells 的 `ov.single.get_obs_value` 中的 groupby 错误。
- 修复 cNMF 的错误（#107、#85）。
- 修复 `Pycomplexheatmap` 版本大于 1.7 时的绘图错误（#136）。


### Bulk 模块

- 修复 `ov.bulk.Matrix_ID_mapping` 中的键值错误。
- 在 `ov.bulk` 中新增 `enrichment_multi_concat`，用于拼接富集结果。
- 修复 gseapy 中的 pandas 版本错误（#137）。

### Bulk2Single 模块

- 新增 `adata.var_names_make_unique()`，避免基因不唯一时的矩阵形状错误（#100）。

### Space 模块

- 修复 `ov.space.STT` 中 `construct_landscape` 的错误。
- 修复 `ov.space.svg` 中 `get_image_idx_1D` 的错误（#117）。
- 新增 `COMMOT`，用于计算空间 RNA-seq 的细胞-细胞相互作用。
- 新增 `starfysh`，用于无 scRNA-seq 参考的空间转录组去卷积（#108）。

### PP 模块

- 更新 ov.pp.mde 的约束错误（#129）。
- 修复 `float128` 类型错误（#134）。


## v 1.6.7

### Space 模块

- 新增 `n_jobs` 参数，用于调整 `extenel.STT.pl.plot_tensor_single` 的线程数。
- 修复 `extenel.STT.tl.construct_landscape` 中的错误。
- 更新 `COMMOT` 和 `Flowsig` 的教程。


### Pl 模块

- 新增 `legend_awargs`，用于调整 `pl.cellstackarea` 和 `pl.cellproportion` 中的图例设置。

### Single 模块

- 修复 `cNMF` 模块中 `get_results` 和 `get_results_rfc` 的错误（#143、#139）。
- 新增 `sccaf`，用于获取最佳聚类。
- 修复 cytotrace2 中的 `.str` 错误（#146）。

### Bulk 模块

- 修复 `bulk.geneset_enrichment` 中 `gseapy` 的导入错误。
- 优化离线富集分析的代码逻辑，新增 background 参数。
- 新增 `pyWGCNA` 包，替代原始的 pyWGCNA 计算（#162）。

### Bulk2Single 模块

- 在 `bulk2single_data_prepare` 中移除 `_stat_axis`，使用 `index` 代替（#160）。

### PP 模块

- 修复 `pp.regress_and_scale` 中的返回值 bug（#156）。
- 修复使用 `ov.pp.pca` 时的 scanpy 版本错误（#154）。

## v 1.6.8

### Bulk 模块

- 修复 gsea_obj.enrichment 中 log_init 的错误（#184）。
- 为 `geneset_plot` 新增 `ax` 参数。

### Space 模块

- 新增 CAST，用于整合多个切片。
- 在 `omicverse.tl` 中新增 `crop_space_visium`，用于裁剪空间数据的子区域。

### Pl 模块

- 为 `cpdb_heatmap` 新增 `legend` 参数。
- 为 `cellstackarea` 新增 `text_show` 参数。
- 新增 `ForbiddenCity` 颜色系统。

## v 1.6.9

### PP 模块

- 新增 `recover_counts`，用于在 `ov.pp.preprocess` 后恢复原始计数。
- 移除 `ov.pp.pca` 中添加的 lognorm 层。

### Single 模块

- 新增 `MultiMap` 模块，用于整合多物种数据。
- 新增 `CellVote`，用于投票选出最优细胞。
- 新增 `CellANOVA`，用于整合样本并校正批次效应。
- 新增 `StaVia`，用于计算伪时间和推断轨迹。

### Space 模块

- 新增 `ov.space.cluster`，用于识别空间域。
- 新增 `Binary`，用于空间聚类。
- 新增 `Spateo`，用于计算空间可变基因。

## v 1.7.0

新增 `cpu-gpu-mixed` 模式，使用 GPU 加速 scRNA-seq 分析。
将 Omicverse 的 Logo 展示方式改为 `ov.plot_set`。

### Bulk 模块
- 在差异表达基因分析中新增 `limma`、`edgeR`（#238）。
- 修复 `DEseq2` 分析的版本错误。

### Single 模块
- 新增 `lazy` 函数，一键计算 scRNA-seq 的所有分析流程（#291）。
- 新增 `generate_scRNA_report` 和 `generate_reference_table`，用于生成报告和参考（#291、#292）。
- 修复 `geneset_prepare` 无法读取非 `\t\t` 分隔的 gmt 文件的问题（#235、#238）。
- 新增 `geneset_aucell_tmp`、`pathway_aucell_tmp`、`pathway_aucell_enrichment_tmp`，用于测试 chunk_size（#238）。
- 新增 `Fate` 的数据增强。
- 在 VIA 中新增 `plot_atlas_view_ov`。
- 修复矩阵过大时 `recover_counts` 中的错误。
- 新增 `forceatlas2`，用于计算 `X_force_directed`。
- 新增 `milo` 和 `scCODA`，用于分析不同细胞类型丰度。
- 新增 `memento`，用于分析差异基因表达。

### Space 模块
- 新增 `GASTON`，用于从空间分辨转录组学（SRT）数据中学习组织切片的地形图（#238）。
- 在 STT 的 `plot_tensor_single` 中新增超级 kwargs。
- 使用 GPU 加速更新 `COMMOT`。

### Plot 模块
- 新增 `dotplot_doublegroup`，用于可视化双组基因。
- 在 `cpdb_interacting_heatmap` 中新增 `transpose` 参数，用于转置图形。
- 新增 `calculate_gene_density`，用于绘制基因密度。


## v 1.7.1

### Single 模块
- 修复 `ov.single.lazy` 的若干错误。
- 修复 `ov.single.generate_scRNA_report` 的格式问题。
- 更新 `palantir` 的若干函数。
- 新增 `CellOntologyMapper`，用于映射细胞名称。


## v 1.7.2

### Pl 模块
- 优化 `ov.pl.box_plot` 的绘图效果。
- 优化 `ov.pl.volcano` 的绘图效果。
- 优化 `ov.pl.violin` 的绘图效果。
- 新增比 scanpy 更美观的点图（#318）。
- 新增与 CellChat 类似的可视化功能（#313）。

### Space 模块
- 在 `COMMOT` 中新增 3D 细胞-细胞相互作用分析（#315）。

### Single 模块
- 修复 pathway_enrichment 的错误（#184）。
- 新增支持 GPU 加速的 SCENIC 模块（#331）。

### utils 模块
- 新增 scICE，用于计算最佳聚类（#329）。

## v 1.7.6

### LLM 模块
- 新增 `GeneFromer`、`scGPT`、`scFoundation`、`UCE`、`CellPLM`，可在 OmicVerse 中直接调用。

### Pl 模块
- 优化嵌入图的可视化效果。
- 新增 `ov.pl.umap`、`ov.pl.pca`、`ov.pl.mde` 和 `ov.pl.tsne`。


## v 1.7.8

实现延迟加载系统，将 `import omicverse` 时间减少 **40%**（从约 7.8 秒降至约 4.7 秒）。
新增对 Apple Silicon（MLX）和 CUDA（TorchDR）设备的 GPU 加速 PCA 支持。
引入智能体系统，支持来自 8 家供应商的 50 余个 AI 模型的自然语言处理。
新增并修复 `anndata-rs`，以支持百万级数据集（#336）。

### PP 模块
- 在 `ov.pp.pca()` 中新增 GPU 加速 PCA，支持 Apple Silicon MPS 设备的 MLX 加速。
- 在 `ov.pp.pca()` 中新增基于 TorchDR 的 PCA 加速，适用于 NVIDIA CUDA 设备。
- 在 `init_pca()` 和 `pca()` 函数中新增智能设备检测和自动后端选择。
- 新增 GPU 加速失败时优雅回退到 CPU 实现的机制。
- 新增增强的详细输出，包含设备选择信息和 emoji 指示符。
- 在 `init_pca()` 中新增基于方差贡献阈值的最优成分数确定。
- 在 `ov.pp.sude()` 中新增 GPU 加速 SUDE 降维，支持 MLX/CUDA。
- 优化 `ov.pp.qc`，新增核糖体和血红蛋白基因，以获取更多数据质量信息。

### Datasets 模块
- 完全消除对 scanpy 的依赖，提升加载速度。
- 新增类似 dynamo 风格的数据集框架，收录全面的数据集集合。
- 新增带进度跟踪和缓存的鲁棒下载系统。
- 新增增强的 mock 数据生成功能，具有真实结构。
- 新增对 h5ad、loom、xlsx 和压缩格式的支持。

### Agent 模块
- 新增多供应商 LLM 支持（OpenAI、Anthropic、Google、DeepSeek、Qwen、Moonshot、Grok、智谱 AI）。
- 新增对英文和中文的自然语言处理。
- 新增带本地执行的代码生成架构。
- 新增多语言别名的函数注册系统。
- 新增智能 API 密钥管理和供应商特定配置。

### Bulk 模块
- 新增 `BayesPrime` 和 `Scaden`，用于去卷积 Bulk RNA-seq 的细胞类型比例。
- 新增 `alignment`，用于将 fastq 对齐到计数矩阵。

### Single 模块
- 新增 `ov.single.Annotation` 和 `ov.single.AnnotationRef`，用于自动注释细胞类型。
- 新增 `ov.alignment.single`，用于直接将 scRNA-seq 对齐到计数矩阵。

## v 1.7.9

实现**智能延迟加载系统**，将 `import omicverse` 时间大幅减少 **85.6 倍**（从约 16.57 秒降至约 0.19 秒）。
增强 RNA-seq 比对工作流，提供完整的 FASTQ 处理和计数工具集。
优化数据集管理，通过嵌套目录创建实现更好的组织结构。

### 性能优化

**延迟加载系统**：
- 对所有主要模块实现基于 `__getattr__` 机制的模块级延迟加载。
- 为常用函数（read、palette、Agent 等）添加属性级延迟加载。
- 引入智能缓存系统，确保首次加载后即时访问。
- 初始导入时间从 **16.57 秒降至 0.19 秒**（提速 85.6 倍）。
- 完全保持向后兼容性——所有现有代码无需修改即可运行。
- 通过 `__dir__()` 实现保留完整的 IDE 支持（含 Tab 补全）。
- 通过延迟 settings 模块初始化修复循环导入问题。
- **MkDocs API 文档生成与延迟加载完全兼容**。

**用户收益**：
- 即时启动 Jupyter notebooks 和脚本
- 按需加载——模块在首次访问时导入
- 简单任务减少内存占用
- 第二次访问已缓存，几乎即时（< 0.001 秒）

### Alignment 模块

**全新 RNA-seq 比对综合工具集**：

新增完整的原始测序数据处理端到端工作流：

- **`ov.alignment.prefetch`**：从 NCBI 下载 SRA 数据集，内置重试逻辑。
- **`ov.alignment.fqdump`**：将 SRA 转换为 FASTQ 格式，支持并行处理。
- **`ov.alignment.parallel_fastq_dump`**：高性能并行 FASTQ 提取。
- **`ov.alignment.fastp`**：FASTQ 文件的质控和接头修剪。
- **`ov.alignment.STAR`**：使用 STAR 进行 RNA-seq 比对，参数可定制。
- **`ov.alignment.featureCount`**：基因级读段计数（从 `count` 更名以避免冲突）。
- **`ov.alignment.single`**：使用 kb-python（kallisto|bustools）一键完成 scRNA-seq 比对。
- **`ov.alignment.ref`**：为比对构建 kallisto|bustools 参考索引。
- **`ov.alignment.count`**：从比对读段定量基因表达。

**主要特性**：
- 为 bulk RNA-seq（STAR + featureCount）和 scRNA-seq（kb-python）工作流提供统一 API。
- 内置支持 kb-python 的 RNA 速度分析。
- 并行处理能力，加快数据转换速度。
- 自动处理双端和单端测序数据。
- 针对 bulk 和单细胞数据的技术特异性过滤。
- 与 SRA 工具集集成，无缝下载数据。

**示例工作流**：
```python
# 下载并处理 bulk RNA-seq
ov.alignment.prefetch('SRR1234567', output_dir='./data')
ov.alignment.fqdump('SRR1234567', output_dir='./fastq')
ov.alignment.fastp('sample_1.fastq.gz', 'sample_2.fastq.gz', output_prefix='clean')
ov.alignment.STAR(fastq1='clean_1.fastq.gz', fastq2='clean_2.fastq.gz',
                  genome_dir='./genome', output_prefix='aligned')
ov.alignment.featureCount(bam='aligned.bam', annotation='genes.gtf', output='counts.txt')

# 或使用一键 scRNA-seq 比对
ov.alignment.single(
    fastq=['read1.fastq.gz', 'read2.fastq.gz'],
    index='./kb_index',
    output_dir='./kb_output',
    technology='10xv3'
)
```

### PP 模块
- 修复 `ov.pp.preprocess` 中的 HVG（高变基因）选择问题。
- 提升预处理流程的稳定性和准确性。
- 重构 PCA 实现，使用 `torch_pca` 进行 GPU 加速（替代 TorchDR）。
- 增强稀疏矩阵的 PCA 计算支持。
- 将 PCA 嵌入基础从 `X_pca` 更新为 `PCA`，提高清晰度和一致性。
- 改善 PCA 计算中的 try-except 错误处理。
- 修复 PCA GPU 模式对稀疏矩阵的支持，避免内存错误。

### Single 模块
- 在 `ov.single.batch_correction` 中新增 `CONCORD` 方法，用于单细胞数据整合。
- 以最先进的算法增强批次校正能力。
- **修复 pySCENIC 中的关键性能问题**：还原了导致内存问题和 scRNA-seq 数据处理减速的低效相关性计算优化。
- 移除 SCENIC 相关性计算中关于 dropout 基因的误导性警告。
- 恢复高效内存的成对相关性计算（防止超过 2 万基因时 OOM）。
- SCENIC 现在使用原始方法：仅计算特定 TF-靶标对的相关性，而非创建完整的基因×基因矩阵。
- 新增 `ov.single.find_markers`，支持五种方法的统一标记基因识别：`cosg`、`t-test`、`t-test_overestim_var`、`wilcoxon` 和 `logreg`；统计方法原生移植自 scanpy，无需 scanpy 运行时依赖，数值结果一致（rtol=1e-4）。
- 新增 `ov.single.get_markers`，以 `DataFrame` 或 `dict` 形式提取顶级标记基因，支持单/多聚类过滤和基于 `min_logfoldchange`、`min_score`、`min_pval_adj` 的可选过滤；输出包含 `pct_group` 和 `pct_rest` 列，显示每个聚类内外的细胞表达比例。

### Space 模块
- 新增 `FlashDeconv`，用于 Visium 空间转录组学的快速无 GPU 去卷积。
- 新增 `Banksy` 聚类方法，用于空间域识别。
- 更新空间分析文档，新增新的聚类方法。

### Web 模块
- 发布 `Omicverse-Notebook`，无需本地安装即可在浏览器中进行交互式分析。
- 发布 `Omicverse-Web`，无需编程即可进行基于 Web 的数据分析。
- 为无编程背景的研究人员普及生物信息学分析。

### Agent 模块
- 增强 `ov.Agent` 的自然语言数据分析处理能力。
- 扩展 LLM 供应商支持和模型选择。
- 优化代码生成和执行流程。

### Pl 模块
- 增强散点图嵌入的分类图例处理。
- 新增 `legend_loc='on data'` 选项，支持在图上直接标注。
- 改善复杂数据集的可视化清晰度。
- 新增 `ov.pl.markers_dotplot`，作为 `rank_genes_groups_dotplot` 更简洁的替代品，改善默认值（`standard_scale='var'`、`cmap='Spectral_r'`、`dendrogram=False`）。
- 修复 `rank_genes_groups_df` 在聚类名称为数字字符串（如 leiden 的 `'0'`、`'1'`）时的 `KeyError`；现在正确处理来自所有标记方法的结构化数组、DataFrame 和普通 2D 数组。

### Datasets 模块
- 新增完整的数据集 URL，便于数据访问。
- 扩展数据下载工具，带进度跟踪。
- **修复数据集下载自动创建嵌套目标目录的问题**。
- 改善数据集工具的错误处理。
- 更新下载行为，提升数据获取可靠性。

### 文档
- 强化点图和 DEG 分析教程中的数据处理文档。
- 更新 scTour 聚类教程，采用最新最佳实践。
- 新增 v1.7.9 的完整版本说明。
- 增强比对模块文档，提供端到端工作流。

### Bug 修复
- 解决 `_settings` 和 `utils` 模块之间的循环导入问题。
- 修复与最新包版本（zarr、pandas 等）的兼容性问题。
- 改善并行处理函数中的错误处理。

### Single 模块
**增强 DEG 分析，加入表达百分比信息**：为差异表达结果新增细胞表达百分比信息

- 新增 `pct_ctrl` 列，显示对照组中表达每个基因的细胞百分比（0-100%）。
- 新增 `pct_test` 列，显示处理组中表达每个基因的细胞百分比（0-100%）。
- 新增 `pct_diff` 列，显示表达百分比差值（pct_test - pct_ctrl）。
- 适用于所有 DEG 方法：`wilcoxon`、`t-test` 和 `memento-de`。
- 通过基于表达普遍性过滤基因，实现更好的标记基因识别。
- 类似于点图圆圈大小信息，有助于识别广泛表达与稀少表达的基因。

**使用示例**：
```python
deg_obj = ov.single.DEG(adata, condition='condition',
                        ctrl_group='Control', test_group='Treatment')
deg_obj.run(celltype_key='cell_label', celltype_group=['T_cells'])
results = deg_obj.get_results()
# 现在包含 pct_ctrl、pct_test、pct_diff 列
```

### 兼容性
**NumPy 2.0 兼容性**：修复所有 NPY201 兼容性问题，确保对 NumPy 1.x 和 2.x 的无缝支持。

**已修复问题（共 31 个）**：

1. **`np.in1d` → `np.isin`**（9 处）
   - `omicverse/bulk/_dynamicTree.py`：3 处（第 697、741 行）
   - `omicverse/single/_cosg.py`：1 处（第 77 行）
   - `omicverse/external/GNTD/_preprocessing.py`：2 处
   - `omicverse/external/scdiffusion/guided_diffusion/cell_datasets_WOT.py`：1 处
   - 其他外部模块：2 处

2. **`np.row_stack` → `np.vstack`**（13 处）
   - `omicverse/external/CAST/CAST_Projection.py`：2 处
   - `omicverse/external/CAST/visualize.py`：2 处
   - `omicverse/external/scSLAT/viz/multi_dataset.py`：多处
   - `omicverse/single/_mdic3.py`：1 处

3. **`np.product` → `np.prod`**（4 处）
   - `omicverse/external/umap_pytorch/model.py`：2 处
   - `omicverse/external/umap_pytorch/modules.py`：2 处

4. **`np.trapz` 兼容性包装器**（2 处）
   - 在以下文件中添加兼容性包装器：
     - `omicverse/external/VIA/plotting_via.py`
     - `omicverse/external/VIA/plotting_via_ov.py`
   - 使用 `numpy.trapezoid`（NumPy 2.0+），回退到 `numpy.trapz`（NumPy 1.x）

**向后兼容性**：
- 所有更改完全保持与 NumPy 1.x（1.13+）的向后兼容性
- `np.isin` 自 NumPy 1.13 起可用
- `np.vstack` 在所有 NumPy 版本中可用
- `np.prod` 在所有 NumPy 版本中可用
- 自定义兼容性包装器处理 `trapz`/`trapezoid` 的过渡

## v 1.7.10

### 范围
- 本版本说明总结了从提交 `cd3d151`（版本设置为 `1.7.10rc1`）到当前 `HEAD` 的变更。
- 本窗口内的总代码变更：`252 个文件修改`，`+46,992 / -9,752`。

### Agent 与运行时
- 将 `ov.Agent` 架构升级为具有子代理委托的现代 agentic 工具调用工作流（v4/v5 演进）。
- 提升 GPT-5.2 的鲁棒性、响应解析和后端错误处理。
- 新增执行合约、工具目录、运行时状态、追踪和清理策略的 harness 运行时组件。
- 强化沙箱行为，对内部模块实施受限导入控制。
- 新增 web 桥接和会话级执行改进，适用于 agent 工作流。

### 新模块
- 新增 `omicverse.biocontext`，通过 BioContext MCP 工具进行生物医学知识查询。
- 新增 `omicverse.fm`（基础模型适配器、路由、注册表和 API）。
- 为通用/单细胞/bulk/空间 I/O 路径新增结构化 `omicverse.io` 命名空间。
- 新增 `omicverse.jarvis` 多渠道机器人框架（飞书/QQ/Telegram），带桥接支持。

### OmicVerse 核心改进
- 持续增强 `pp`、`pl`、`single`、`space` 和 `utils` 模块。
- 修复预处理工具内部（`_utils.py` 和 `_scale.py` 路径）之间的循环导入问题。
- 在关键分析模块（预处理、注释、轨迹、空间、数据集、bulk）中新增/更新函数级元数据和文档质量。
- 通过新的签名资源和改进的加载路径扩展数据集工具。

### 注册表与帮助系统
- 改进注册表行为和包入口点中的模块导入暴露。
- 增强 agent 可发现性的函数/类注册元数据覆盖率。
- 注册表帮助生成现在与基于类的工具中的类构造函数文档更好地对齐。

### Web 与 UI
- 单细胞分析 UI 收到迭代升级：
  - 更好的代码单元格管理和撤销行为
  - 改进的 AnnData slot 详情检索和显示
  - 更好的 DataFrame 渲染和集成
  - 绘图密度/点样式控制优化
  - 分析面板的国际化和 UX 打磨
- `omicverse_web` 服务层扩展了面向会话的 agent 服务支持。

### 开发者体验与测试
- 新增 FM 测试套件和多个 harness/ovagent 测试模块。
- 移除已废弃的遗留优先级和复杂度分类器测试路径。
- 新增运行时合约和操作指南的工作流和 harness 文档页面。

### 文档
- 更新和扩展 agent 架构和流式 API 文档。
- 更新 `t_preprocess_cpu.ipynb`，匹配最新的 GPU/版本检测行为。
- 为 Jarvis 和 agent 相关工作流新增双语和部署导向指南。


## v 2.2.4

补记:该版本发布到 PyPI 时没有写 release notes。

### 新增模块
- **`ov.synbio`(PR #887、#895)** —— 三层合成生物学模块(代谢 / 蛋白·酶 / DNA),
  同期扩展了 mRNA 设计、de novo binder、prime editing 与动态 FBA。

### single 模块
- **跨物种整合(PR #893、#894)** —— 直系同源 + SAMap + SATURN,并新增 CAMEX
  后端(`method='camex'`)。
- **Seurat 风格的 RPCA 整合(PR #899)** —— `methods='rpca'`。

### pp 模块
- **GPU 双细胞检测(PR #886、#888、#889)** —— scDblFinder 与 DoubletFinder 的
  pANN 改用分块 GPU kNN,sccomposite 后处理转 GPU/torch(此前在 1e5 细胞量级会
  内存溢出)。
- **修复** —— `qc_gpu` 最终过滤统计的对象搞错了(应为细胞与基因数而非 counts,
  PR #890);`qc_gpu` 的双细胞方法在 GPU 矩阵上直接失败(PR #897);
  pyscdblfinder 低于 0.2.0 时大数据集卡死(PR #892)。

### 其他
`ov.pl.qc` 对 UMI 与基因数只做显示层裁剪(PR #896);`ov.space.svg` 的
`mode='pearsonr'` 对全零 spot 加了保护(PR #898);FlowSig 的 bootstrap 改为
进程安全(PR #878);`cpu_gpu_mixed_init` 新增 `devices` 参数(PR #891)。

## v 2.3.0

次版本号而非补丁号:自 2.2.4 起新增了八个模块。

### 新增模块
- **`ov.flow`(PR #906、#907)** —— 流式细胞术。通用 FCS 读取器
  (`ov.io.read_fcs`)、显示变换、门控策略树。同期两处修复:写出的 Gating-ML
  并不是合法的 Gating-ML(PR #910);象限的子群本身就是群体,可以作为父节点
  (PR #911)。
- **`ov.mol` 分子动力学(PR #905)** —— GPU 模拟、轨迹分析、MM-GBSA。
- **`ov.alignment`(PR #904)** —— 基于 DIAMOND / BLAST+ 的同源搜索,以及
  Sanger `.ab1` 验证。

### pl 模块
- **表格优先的统计绘图与 AnnData 适配器(PR #920)** —— DataFrame、裸数组和
  AnnData 可互换,凡是会算出数字的图,都用 scipy 或 statsmodels 在同一份数据上
  对过。
- **临床统计与出版级图表排版(PR #919)**。

### space 模块
- **SPATA2 风格的坐标工具(PR #847)** —— 坐标表、变量合并、组织轮廓、空间离群
  过滤、像素与物理单位换算。
- **排布层(PR #924)** —— `ov.space.nb` 提供空间图上的统计(邻域富集、随距离的
  共现、交互矩阵、群体中心性、Ripley、sepal、区域掩膜、滑动窗口、距锚点的表达
  梯度);`ov.space.niche` 处理重复出现的多细胞结构,补齐 squidpy
  `calculate_niche` 的三种 flavor,并把 `nmf_tissue_zones` 以文献惯用的名字
  `niche.molecular` 暴露出来;`ov.space.geom` 负责连续切片对齐、3D 堆叠与插值。
  语义刻意对齐 squidpy,使得数字可核对:在同一张图上对照 squidpy 1.6.5,
  `interaction_matrix`、`nhood_enrichment` 计数与 `centrality` **完全一致**,
  `co_occurrence` 与三种 Ripley 模式的 Pearson r = 1.0000,`var_by_distance`
  差异 1.11e-16。
- **Stereo-seq(PR #924)** —— `ov.io.spatial.read_stereoseq` 读取 GEM 并分箱;
  `bin_stereoseq` 在内存中重新聚合,并拒绝无法整除嵌套的 bin 尺寸。
- **`spatial_neighbors` 新增 `coord_type='grid'`** —— 纯 kNN 无法知道阵列平台
  存在晶格,组织边缘的 spot 会跨过空隙凑够邻居数,连上并不相邻的点。默认仍为
  `'generic'`,不改变既有结果。

### synbio 模块
- **补齐 D 段缺口(PR #916)** —— 重建、组学到 GEM、可制造性、生物安全。
- **修正约四十处会产出"看似合理但错误的数字"的缺陷(PR #917)** —— 转换后的
  吉布斯自由能、tRNA 计数与摆动配对约定、replichore 比例、Echo 转移量的算术、
  生长模型选择等。每一处都是把图或数字对照原始文献核出来的,不是靠测试报错。
- **`[synbio]` 曾经装不上**(`rs3` 的固定版本所致,PR #912);Rule Set 3 通过
  `--no-deps` 运行时拉取回归(PR #913)。

### 缺陷修复
- **MCP 下的 `ov.pp.leiden`(PR #925)** —— MCP 服务器广告了这个工具,而它自己的
  extra 装不出 `leidenalg`。
- **移除 rpy2 mclust(PR #918)** —— 五个空间 wrapper 各自内嵌了 `rpy2` 桥接,
  现统一走纯 Python 的 `pymclustR` 后端。在同一批坐标上对照 R mclust 6.1.2,
  对数似然与 BIC 到小数点后六位一致,每个细胞落在同一个簇。
- **CopyKAT 在缺少基因组表时会明确报错(PR #922)**,而不是静默失败。
- **AIRR 的 multichain 细胞(PR #923)** —— 按生物学上不同的亚型拆解,而不是当作
  技术假象丢弃。
- **`ov.tl` / `ov.es` / `ov.micro` 在新会话中可被发现(PR #908)**。

### 基础设施
- `omicverse_guide` submodule 前进十个提交,覆盖 `ov.flow` 系列之后合入的全部
  教程。文档构建通过这个指针读取教程,指针滞后就意味着这些内容进不了文档站。
