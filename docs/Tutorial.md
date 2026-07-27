# Tutorials

This page is the markdown overview for the tutorial structure defined in `mkdocs.yml`. It is meant to help readers scan the current OmicVerse tutorial map before jumping into notebooks or topic-specific guides.

## Genomics

- [GWAS — end-to-end pipeline](Tutorials-genetics/t_genetics_01_gwas_pipeline.ipynb)
- [Functional follow-up of GWAS hits](Tutorials-genetics/t_genetics_02_functional_followup.ipynb)

## Bulk Transcriptomics

- [Bulk tutorial index](Tutorials-bulk/index.md)
- Upstream
  - [Bulk RNA-seq alignment with STAR](Tutorials-bulk/t_mapping_STAR.ipynb)
  - [Bulk RNA-seq alignment with kb-python](Tutorials-bulk/t_mapping_kbpython.ipynb)
- Preprocessing
  - [Batch correction in Bulk RNA-seq or microarray data](Tutorials-bulk/t_bulk_combat.ipynb)
- Downstream
  - [Different expression analysis](Tutorials-bulk/t_deg.ipynb)
  - [Different expression analysis with DEseq2](Tutorials-bulk/t_deseq2.ipynb)
  - [Protein-Protein interaction (PPI) analysis by String-db](Tutorials-bulk/t_network.ipynb)
  - [WGCNA (Weighted gene co-expression network analysis) analysis](Tutorials-bulk/t_wgcna.ipynb)
- Deconvolution
  - [Bulk deconvolution with reference scRNA-seq](Tutorials-bulk/t_decov_bulk.ipynb)
- Others
  - [TCGA database preprocess](Tutorials-bulk/t_tcga.ipynb)

## Single-Cell Transcriptomics

- [Single-cell tutorial index](Tutorials-single/index.md)
- Alignment
  - [Alignment of single-cell RNA-seq data](Tutorials-single/t_alignment_1k.ipynb)
  - [Alignment of single-cell RNA-seq data for RNA velocity analysis](Tutorials-single/t_alignment_velocity.ipynb)
- Preprocessing
  - [Preprocessing the data of scRNA-seq [CPU]](Tutorials-single/t_preprocess_cpu.ipynb)
  - [Preprocessing the data of scRNA-seq [GPU]](Tutorials-single/t_preprocess_gpu.ipynb)
  - [Preprocessing the data of scRNA-seq [Rust / out-of-memory]](Tutorials-single/t_preprocess_rust.ipynb)
  - [Clustering space](Tutorials-single/t_cluster.ipynb)
  - [Consensus Non-negative Matrix factorization (cNMF)](Tutorials-single/t_cnmf.ipynb)
  - [Lazy analysis of scRNA-seq](Tutorials-single/t_lazy.ipynb)
- Batch correction
  - [Batch correction overview — backends, decision tree, schema](Tutorials-single/batch/index.md)
  - [Recommended workflow — side-by-side comparison of all backends + scib-metrics](Tutorials-single/batch/t_single_batch.ipynb)
  - [**Backend zoo** › Harmony · ComBat · Scanorama · scVI · scANVI · totalVI · scPoli · CellANOVA · Concord · Seurat-CCA](Tutorials-single/batch/zoo/index.md)
- Annotation
  - [Reference-free automated single-cell cell type annotation](Tutorials-single/t_anno_noref.ipynb)
  - [Reference automated single-cell cell type annotation](Tutorials-single/t_anno_ref.ipynb)
  - [Automatic cell type annotation with GPT/Other](Tutorials-single/t_gptanno.ipynb)
  - [Mapping Cell Names to the Cell Ontology](Tutorials-single/t_cellmatch.ipynb)
  - [Celltype auto annotation with SCSA](Tutorials-single/t_cellanno.ipynb)
  - [Celltype auto annotation with MetaTiME](Tutorials-single/t_metatime.ipynb)
  - [Celltype annotation migration(mapping) with TOSICA](Tutorials-single/t_tosica.ipynb)
  - [Celltype auto annotation with scMulan](Tutorials-single/t_scmulan.ipynb)
  - [Consensus annotation with CellVote](Tutorials-single/t_cellvote.md)
- Trajectory
  - [Prediction of absolute developmental potential using CytoTrace2](Tutorials-single/t_cytotrace.ipynb)
  - [Trajectory Inference with Diffusion Map and PAGA](Tutorials-single/t_traj_diffusion.ipynb)
  - [Trajectory Inference with Slingshot](Tutorials-single/t_traj_slingshot.ipynb)
  - [Trajectory Inference with Palantir](Tutorials-single/t_traj_palantir.ipynb)
  - [Trajectory Inference with scTour](Tutorials-single/t_traj_sctour.ipynb)
  - [Trajectory Inference with Monocle 2](Tutorials-single/t_traj_monocle2.ipynb)
  - [Trajectory Inference with StaVIA](Tutorials-single/t_traj_stavia.ipynb)
  - [Trajectory Inference with VIA and scVelo](Tutorials-single/t_via_velo.ipynb)
  - [Timing-associated genes analysis with TimeFateKernel](Tutorials-single/t_cellfate_gene.ipynb)
  - [Identify the driver regulators of cell fate decisions](Tutorials-single/t_cellfate.ipynb)
- MetaCell
  - [MetaCell overview — metacell vs pseudobulk](Tutorials-single/metacell/index.md)
  - [Recommended workflow — SEACells end-to-end](Tutorials-single/metacell/t_metacell_recommended.ipynb)
  - [Multi-sample metacells with batch correction](Tutorials-single/metacell/t_metacell_multisample.ipynb)
  - [Backend zoo — 7 partitioners compared](Tutorials-single/metacell/zoo/index.md)
- Cell Structure
  - [Differential expression and celltype analysis [All Cell]](Tutorials-single/t_deg_single.ipynb)
  - [Differential expression analysis [Meta Cell]](Tutorials-single/t_scdeg.ipynb)
  - [Gene Regulatory Network Analysis with SCENIC](Tutorials-single/t_scenic.ipynb)
  - [Pathway analysis with AUCell](Tutorials-single/t_aucell.ipynb)
  - [Drug response predict with scDrug](Tutorials-single/t_scdrug.ipynb)
  - [Batch Correction with SIMBA](Tutorials-single/t_simba.ipynb)
- Cell-Cell Communication
  - [Cell-cell communication with CellPhoneDB](Tutorials-single/t_ccc_cellphonedb.ipynb)
  - [Cell-cell communication with LIANA+](Tutorials-single/t_ccc_liana.ipynb)
- Velocity
  - [Velocity Basic Calculation](Tutorials-velo/t_velo.ipynb)
  - [Velocity Optimization](Tutorials-velo/t_graphvelo.ipynb)
  - [RNA Velocity with RegVelo](Tutorials-velo/t_regvelo.ipynb)
  - [Run RegVelo with inferred GRN](Tutorials-velo/t_regvelo_infer_grn.ipynb)
  - [Velocity-guided CellRank Analysis](Tutorials-velo/t_velo_cellrank.ipynb)
- Multi-omics
  - [Multi omics analysis by MOFA](Tutorials-single/t_mofa.ipynb)
  - [Multi omics analysis by MOFA and GLUE](Tutorials-single/t_mofa_glue.ipynb)
  - [Celltype annotation transfer in multi-omics](Tutorials-single/t_anno_trans.ipynb)

## Spatial Transcriptomics

- [Space tutorial overview](Tutorials-space/index.md)
- Preprocess
  - [Crop and Rotation of spatial transcriptomic data](Tutorials-space/t_crop_rotate.ipynb)
  - [Visium 10x HD Cellpose](Tutorials-space/t_cellpose.ipynb)
  - [Analyze Nanostring data](Tutorials-space/t_nanostring_preprocess.ipynb)
  - [Analyze Xenium data](Tutorials-space/t_xenium_preprocess.ipynb)
  - [Analyze 10x Atera (WTA Preview) data](Tutorials-space/t_atera_preprocess.ipynb)
  - [Analyze Visium HD data](Tutorials-space/t_visium_hd_preprocess.ipynb)
  - [Spatial clustering and denoising expressions](Tutorials-space/t_cluster_space.ipynb)
  - [Spatial integration and clustering](Tutorials-space/t_staligner.ipynb)
- Deconvolution
  - [Identifying Pseudo-Spatial Map](Tutorials-space/t_spaceflow.ipynb)
  - [Spatial deconvolution with reference scRNA-seq](Tutorials-space/t_decov.ipynb)
  - [Spatial deconvolution with RCTD](Tutorials-space/t_decov_rctd.ipynb)
  - [FlashDeconv (fast, GPU-free deconvolution)](Tutorials-space/t_flashdeconv.ipynb)
  - [Spatial deconvolution without reference scRNA-seq](Tutorials-space/t_starfysh_new.ipynb)
- Downstream
  - [Spatial transition tensor of single cells](Tutorials-space/t_stt.ipynb)
  - [Spatial Communication](Tutorials-space/t_commot_flowsig.ipynb)
  - [Spatial IsoDepth Calculation](Tutorials-space/t_gaston.ipynb)
  - [Single cell spatial alignment tools](Tutorials-space/t_slat.ipynb)

## Immune Repertoire

- [AIRR-seq tutorial index](Tutorials-airr/index.md)
- [Single-cell TCR + transcriptome — the immune-repertoire pipeline](Tutorials-airr/t_airr_01_singlecell.ipynb)
- [Bulk TCR repertoire analysis (immunarch backend)](Tutorials-airr/t_airr_02_bulk.ipynb)
- [BCR somatic hypermutation, selection & lineage trees — bulk (Immcantation)](Tutorials-airr/t_airr_03_bcr.ipynb)
- [Single-cell BCR + transcriptome — clonal expansion, isotypes & SHM](Tutorials-airr/t_airr_06_bcr_singlecell.ipynb)
- [TCR specificity — TCRdist, GLIPH2, meta-clonotypes, VDJdb annotation](Tutorials-airr/t_airr_04_tcr.ipynb)
- [Joint TCR + gene-expression analysis (CoNGA-style)](Tutorials-airr/t_airr_05_tcr_gex.ipynb)

## Flow Cytometry

- [Flow cytometry tutorial index](Tutorials-flow/index.md)
- [**Case study — immunophenotyping PBMC after cardiac arrest**](Tutorials-flow/t_flow_06_case_study.ipynb) — start here: one complete analysis on real published data in short `ov.*` calls, including the QC step that catches a failed stain
- [Reading FCS, compensation and display scales](Tutorials-flow/t_flow_01_reading_and_compensation.ipynb) — `ov.io.read_fcs`, the spillover matrix and what it does to a plot, and why compensated data needs a biexponential (logicle / hyperlog) axis rather than a log one
- [Gates, the gating strategy, and reading the numbers](Tutorials-flow/t_flow_02_gating.ipynb) — the five Gating-ML gate geometries, the strategy tree, `stats()` with its `low_n` warning, quadrant plots, the hierarchy, and back-gating
- [Saving a strategy and applying it to a batch](Tutorials-flow/t_flow_03_gatingml.ipynb) — Gating-ML 2.0 round-trip (the ISAC standard FlowJo / Cytobank / flowCore read), one strategy across three samples, and diffing two strategies
- [FlowSOM — and what clustering does not replace](Tutorials-flow/t_flow_04_flowsom.ipynb) — pure-numpy FlowSOM shown working, and shown failing in the way it fails when the gating is skipped
- [The whole module on real data](Tutorials-flow/t_flow_05_real_data.ipynb) — two published CC-BY-4.0 experiments (BD LSRFortessa with a real 13x13 spillover matrix; Cytek Aurora with FSC-H and CD19): `$PnR` instead of a hard-coded top of scale, fitting logicle `W` to real detector noise, and a pooled 40% that turns out to be one sample's failed stain

## Proteomics

- [Proteomics tutorial index](Tutorials-protein/index.md)
- Bulk LC-MS/MS
  - [Bulk LC-MS/MS best-practice pipeline](Tutorials-protein/t_protein_01_bulk_pipeline.ipynb)
  - [Missing values: diagnosis & imputation](Tutorials-protein/t_protein_02_missing_values.ipynb)
  - [Peptide → protein summarization & DIA](Tutorials-protein/t_protein_03_summarization_dia.ipynb)
  - [Differential expression: methods compared](Tutorials-protein/t_protein_04_differential_expression.ipynb)
- Affinity proteomics
  - [Olink NPX affinity proteomics](Tutorials-protein/t_protein_05_olink.ipynb)

## Structure & Docking

- [3D molecular structure visualization](Tutorials-mol/t_mol_structure.ipynb)
- [Binding-pocket detection & druggability (fpocket)](Tutorials-mol/t_mol_druggability.ipynb)
- [Molecular docking with AutoDock Vina](Tutorials-mol/t_mol_docking.ipynb)

## Synthetic Biology

- [Synthetic biology tutorial index](Tutorials-synbio/index.md)
- [Synthetic biology with `ov.synbio` — from metabolism to enzyme to DNA](Tutorials-synbio/t_synbio_01_intro.ipynb) — metabolic FBA / strain design, ESMFold + ESM + ProteinMPNN protein design, codon & primer design, and the enzyme→yield A↔B coupling
- [Circuits, CRISPR, assembly & pathway design](Tutorials-synbio/t_synbio_02_circuits_to_pathways.ipynb) — genetic-circuit ODE/stochastic simulation, RBS/promoter strength, CRISPR guides, Golden Gate/Gibson assembly, MDF thermodynamics, retrosynthesis, library design
- [CRISPR editing & directed-evolution libraries](Tutorials-synbio/t_synbio_03_crispr_library.ipynb) — gRNA design + off-target CFD scoring, base editing, HDR knock-in, degenerate-codon / DMS libraries, ESM-guided directed evolution
- [Advanced SOTA — mRNA design, de-novo binders, prime editing](Tutorials-synbio/t_synbio_04_advanced.ipynb) — LinearDesign mRNA, RNA/siRNA/antisense design, prime editing (PrimeDesign), CRISPRi/a & Cas13, dynamic FBA, minimal cut sets, retrobiosynthesis, and the full de-novo binder pipeline (RFdiffusion → ProteinMPNN → Boltz-2)
- [Building a strain from scratch — layer A end to end](Tutorials-synbio/t_synbio_05_strain_from_scratch.ipynb) — GEM reconstruction + gap-filling, omics→GEM contextualisation on real E. coli proteomics, MOMA/ROOM knockouts, OptForce, TMFA, RBA, SteadyCom communities, reaction→enzyme matching
- [From a design to an order](Tutorials-synbio/t_synbio_06_design_to_order.ipynb) — solubility/aggregation/signal peptide/localisation, K_M and substrate scope, MSA→tree→ancestral reconstruction, codon harmonisation, synthesis difficulty, overhang fidelity, terminators, truth-table→DNA compilation, biosecurity screening, backbone selection
- [Case study I — E. coli succinate cell factory](Tutorials-synbio/t_synbio_case01_succinate.ipynb) — real metabolic engineering end-to-end
- [Case study II — engineering a thermostable DHFR](Tutorials-synbio/t_synbio_case02_dhfr_engineering.ipynb) — real enzyme engineering end-to-end
- [Case study III — evaluating a protein design](Tutorials-synbio/t_synbio_case03_dhfr_evaluation.ipynb) — score a DHFR variant with the `evaluate_design` scorecard + 3D WT-vs-variant overlay (self-consistency RMSD), each metric reliability-tagged

## Metabolomics

- [Metabolomics tutorial index](Tutorials-metabol/index.md)
- Preprocessing and univariate analysis
  - [Metabolomics preprocessing and univariate statistics](Tutorials-metabol/t_metabol_01_intro.ipynb)
- Multivariate discrimination
  - [Multivariate discrimination with PLS-DA and OPLS-DA](Tutorials-metabol/t_metabol_02_multivariate.ipynb)
- Pathway enrichment
  - [Metabolite-set enrichment analysis (MSEA)](Tutorials-metabol/t_metabol_03_pathway.ipynb)
- Untargeted LC-MS
  - [Untargeted LC-MS and mummichog pathway inference](Tutorials-metabol/t_metabol_04_untargeted.ipynb)
- Lipidomics
  - [Lipidomics with LIPID MAPS and LION](Tutorials-metabol/t_metabol_05_lipidomics.ipynb)

## Microbiome

- [Microbiome tutorial index](Tutorials-microbiome/index.md)
- Amplicon (16S / ITS / 18S)
  - [16S amplicon pipeline (cutadapt + vsearch UNOISE3 + SINTAX)](Tutorials-microbiome/t_16s_amplicon.ipynb)
  - [16S phylogeny: MAFFT + FastTree → Faith PD + UniFrac](Tutorials-microbiome/t_16s_phylogeny.ipynb)
  - [DADA2 backend (pure-Python via pydada2)](Tutorials-microbiome/t_16s_dada2.ipynb)
  - [Differential abundance: Wilcoxon vs DESeq2 vs ANCOM-BC](Tutorials-microbiome/t_16s_da_comparison.ipynb)
  - [Cross-cohort 16S meta-analysis (combine_studies + meta_da)](Tutorials-microbiome/t_16s_meta_analysis.ipynb)

## Multi-Omics

- [Multi-Omics tutorial index](Tutorials-Multi-Omics/index.md)
- [Bulk ↔ Single-cell ↔ Spatial overview](Tutorials-Multi-Omics/bulk-single/index.md)
- [Bulk RNA-seq generate 'interrupted' cells to interpolate scRNA-seq](Tutorials-Multi-Omics/bulk-single/t_bulktrajblend.ipynb)
- [Bulk RNA-seq to Single RNA-seq](Tutorials-Multi-Omics/bulk-single/t_bulk2single.ipynb)
- [Single RNA-seq to Spatial RNA-seq](Tutorials-Multi-Omics/bulk-single/t_single2spatial.ipynb)
- [Microbe ↔ Metabolite overview](Tutorials-Multi-Omics/micro-meta/index.md)
- [Paired microbe ↔ metabolite integration (MMvec-style)](Tutorials-Multi-Omics/micro-meta/t_micro_metabol_paired.ipynb)

## Foundation Models

- [Foundation model overview](Tutorials-llm/index.md)
- [scGPT](Tutorials-llm/t_scgpt.ipynb)
- [Geneformer](Tutorials-llm/t_geneformer.ipynb)
- [scFoundation](Tutorials-llm/t_scfoundation.ipynb)
- [UCE](Tutorials-llm/t_uce.ipynb)
- [CellPLM](Tutorials-llm/t_cellplm.ipynb)

## Visualization

- [Plotting tutorial overview](Tutorials-plotting/index.md)
- [Visualization of single cell RNA-seq](Tutorials-plotting/t_visualize_single.ipynb)
- [Visualization of bulk RNA-seq](Tutorials-plotting/t_visualize_bulk.ipynb)
- [Palette optimization for publication-quality single-cell & spatial plots](Tutorials-plotting/t_palette.ipynb)
- [Color system](Tutorials-plotting/t_visualize_colorsystem.ipynb)
- [Circular UMAP + plot1cell-style visualizations](Tutorials-plotting/t_plot1cell.ipynb)
- [Funky heatmaps for benchmark / multi-metric tables](Tutorials-plotting/t_funkyheatmap.ipynb)
