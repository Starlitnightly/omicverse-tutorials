# Epigenetics

Tutorials for the `omicverse.epi` (`ov.epi`) module — single-cell and bulk **epigenomics**,
built as a thin wrapper over the [epione](https://github.com/aristoteleo/epione) toolkit. Every
`ov.epi` function imports epione internally and delegates, so the familiar `pp` / `tl` / `pl`
grammar now also covers chromatin accessibility and 3D genome organisation.

The **single-cell ATAC** tutorials (1–6) use small public 10x PBMC datasets that `ov.epi.datasets`
downloads on demand, so they run end-to-end on a laptop CPU. The **Hi-C** tutorials (7–8) read
local `.cool` / `.scool` files (provenance and accession noted in each notebook); replace the data
path with your own to reproduce them.

```{toctree}
:maxdepth: 1

../Tutorials-epigenetics/t_epi_01_atac_preprocess
../Tutorials-epigenetics/t_epi_02_atac_clustering_annotation
../Tutorials-epigenetics/t_epi_03_atac_chromvar
../Tutorials-epigenetics/t_epi_04_peak_to_gene
../Tutorials-epigenetics/t_epi_05_marker_peaks
../Tutorials-epigenetics/t_epi_06_integration_label_transfer
../Tutorials-epigenetics/t_epi_07_bulk_hic
../Tutorials-epigenetics/t_epi_08_single_cell_hic
```
