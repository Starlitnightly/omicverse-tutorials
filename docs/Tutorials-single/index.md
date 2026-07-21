# Tutorial of single cell RNA-seq

This page mirrors the `Single` section in `mkdocs.yml`.

## Alignment

- [Alignment of scRNA-seq data with simpleaf / alevin-fry](t_alignment_1k.ipynb)
- [Alignment of scRNA-seq data with kb-python](t_alignment_kb.ipynb)
- [simpleaf vs kb-python — speed & accuracy comparison](t_alignment_compare.ipynb)
- [Alignment of single-cell RNA-seq data for RNA velocity analysis](t_alignment_velocity.ipynb)

## Preprocessing

- [Preprocessing the data of scRNA-seq [CPU]](t_preprocess_cpu.ipynb)
- [Preprocessing the data of scRNA-seq [GPU]](t_preprocess_gpu.ipynb)
- [Preprocessing the data of scRNA-seq [Rust / out-of-memory]](t_preprocess_rust.ipynb)
- [Ambient / contamination RNA removal](t_ambient_rna.ipynb)
- [Clustering space](t_cluster.ipynb)
- [Consensus Non-negative Matrix factorization (cNMF)](t_cnmf.ipynb)
- [Lazy analysis of scRNA-seq](t_lazy.ipynb)

## Batch correction

- [Batch correction overview — backends, decision tree, schema](batch/index.md)
- [Recommended workflow — side-by-side comparison of all backends + scib-metrics](batch/t_single_batch.ipynb)
- [**Backend zoo** › Harmony · ComBat · Scanorama · scVI · scANVI · totalVI · scPoli · CellANOVA · Concord · Seurat-CCA](batch/zoo/index.md)

## Cross-species integration

- [Cross-species integration via orthologs (Ensembl BioMart + Harmony/scVI)](t_cross_species.ipynb)

## Annotation

- [Reference-free automated single-cell cell type annotation](t_anno_noref.ipynb)
- [Reference automated single-cell cell type annotation](t_anno_ref.ipynb)
- [Consensus annotation with CellVote](t_cellvote.ipynb)
- [Mapping Cell Names to the Cell Ontology](t_cellmatch.ipynb)
- [**Individual methods** › SCSA · GPT-cell-type · MetaTiME · scMulan · TOSICA](anno-zoo/index.md)

## Trajectory

- [Trajectory inference overview — backends, decision tree, schema](trajectory/index.md)
- [Recommended workflow — Slingshot end-to-end on a branching topology](trajectory/t_traj_slingshot.ipynb)
- [Unified downstream — macrostates · terminal states · fate probabilities](trajectory/t_traj_fate.ipynb)
- [**Backend zoo** › Palantir · diffusion-map · scTour · StaVIA · Monocle 2 · VIA · CytoTrace 2 · SCORPIUS · TSCAN · destiny · URD · Monocle 3 · CytoTRACE](trajectory/zoo/index.md)
- [Timing-associated genes analysis with TimeFateKernel](t_cellfate_gene.ipynb)
- [Identify the driver regulators of cell fate decisions](t_cellfate.ipynb)

## MetaCell

- [MetaCell overview — metacell vs pseudobulk, decision tree](metacell/index.md)
- [Recommended workflow — SEACells end-to-end + downstream](metacell/t_metacell_recommended.ipynb)
- [Multi-sample metacells with batch correction](metacell/t_metacell_multisample.ipynb)
- [**Backend zoo** › SEACells · MetaQ · SuperCell · k-means · random · GeoSketch · compare](metacell/zoo/index.md)

## Cell Structure

- [Differential expression and celltype analysis [All Cell]](t_deg_single.ipynb)
- [Differential expression analysis [Meta Cell]](t_scdeg.ipynb)
- [Gene Regulatory Network Analysis with SCENIC](t_scenic.ipynb)
- [Drug response predict with scDrug](t_scdrug.ipynb)
- [Batch Correction with SIMBA](t_simba.ipynb)

## Copy-Number Variation

- [Single-cell CNV with CopyKAT](t_copykat.ipynb)
- [Single-cell CNV with inferCNV](t_infercnv.ipynb)

## Metabolism

- [Single-cell metabolism — scMetabolism, scFEA & Compass](t_metabolism.ipynb)
- [Metabolite cell-cell communication with MEBOCOST](t_metabolism_ccc.ipynb)

## Enrichment

- [Pathway analysis with AUCell](t_aucell.ipynb)
- [Comparing enrichment-score methods on scRNA-seq](enrichment/t_es_compare.ipynb)

## Cell-Cell Communication

- [Cell-cell communication with CellPhoneDB](t_ccc_cellphonedb.ipynb)
- [Cell-cell communication with LIANA+](t_ccc_liana.ipynb)

## Multi-omics

- [Multi omics analysis by MOFA](t_mofa.ipynb)
- [Multi omics analysis by MOFA and GLUE](t_mofa_glue.ipynb)
- [Celltype annotation transfer in multi-omics](t_anno_trans.ipynb)

## Single-EV proteomics

- [Single-extracellular-vesicle (single-EV) proteomics](t_single_ev.ipynb)
