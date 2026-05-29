# Genomics

A systematic, best-practice **GWAS pipeline** built on the
`omicverse.genetics` module — a unified statistical-genetics framework that
threads genotype, expression and complex traits into one analysis.

This chapter is a **three-notebook end-to-end workflow**, not a catalogue of
methods.

The first two notebooks run entirely on **real public data** — exposed through
`ov.datasets` loaders — so each result is what the data actually show, and
each step feeds the next:

1. **From genotypes to a fine-mapped locus** — a real cis-eQTL association
   study on the **GEUVADIS** cohort (462 1000-Genomes individuals with
   real chr22 genotypes *and* lymphoblastoid-cell-line RNA-seq). Sample QC,
   variant QC, population-structure correction by genotype PCA (the real
   European/African split), a cis-eQTL screen that picks a gene with a
   strong signal, a PC-adjusted association scan, genomic-inflation and
   Q-Q / Manhattan diagnostics, and SuSiE statistical fine-mapping to a
   95% credible set.
2. **From a GWAS hit to a mechanism** — functional follow-up of the real
   blood **lymphocyte-count GWAS** of Astle *et al.* 2017 (GWAS Catalog
   GCST004627, *N* ≈ 173k). Manhattan + genomic-inflation overview,
   SNP-heritability by LD score regression, Bayesian colocalization of the
   GWAS against real **GTEx v8 whole-blood** cis-eQTLs, transcriptome-wide
   association (S-PrediXcan TWAS), Mendelian randomization with MR-Egger
   pleiotropy sensitivity, and single-cell disease-relevance scoring
   (scDRS) on a real **PBMC** atlas to find the disease-relevant cell type.

Every step opens with the rationale — the *why*, the standard thresholds
and how to interpret the result — and reports the real numbers honestly,
caveats and all, so the chapter reads as a GWAS protocol on real data.
The statistical engines are the standalone R-parity packages
`pymatrixeqtl`, `pysusie`, `pycoloc`, `pytwosamplemr`, `pyscdrs`, `pyldsc`
and `pytwas`; the GWAS core (QC, association, genomic inflation) needs no
backend.

3. **From a GWAS hit to spatially resolved mapping** — spatially resolved
   GWAS with **gsMap** on the official **MOSTA** embryo dataset
   (`E16.5_E1S1.MOSTA.h5ad`, 121,767 spots). The pipeline learns a latent
   representation from expression and spatial structure, maps it back to
   gene-level specificity scores (GSS), connects pre-computed LD resources,
   runs spatial-LDSC with real GWAS summary statistics (`IQ_NG_2018`),
   aggregates spot-level p-values by Cauchy combination, and visualises
   the results with native OmicVerse plotting methods.

```{toctree}
:maxdepth: 1

../Tutorials-genetics/t_genetics_01_gwas_pipeline
../Tutorials-genetics/t_genetics_02_functional_followup
../Tutorials-genetics/t_genetics_03_spatially_resolved_gwas
```
