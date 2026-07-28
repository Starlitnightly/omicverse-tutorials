# Tutorials of Spatial Transcriptomics

This page mirrors the `Space` section in `mkdocs.yml` and provides a markdown entry point for the spatial tutorial notebooks.

## Arrangement, niches and 3-D

- [How the tissue is arranged: spatial statistics and niches](t_spatial_arrangement.ipynb) — neighbourhood enrichment, co-occurrence over distance, group centrality, Ripley, distance-from-anchor gradients, region masking, and the three flavours of niche analysis ([issue #760](https://github.com/omicverse/omicverse/issues/760)).
- [From serial sections to a volume, and reading Stereo-seq](t_spatial_3d.ipynb) — `ov.space.geom` alignment validated against known rotations, 3-D stacking, section interpolation, and the Stereo-seq GEM reader with bin-size sweep.

## SPATA2-inspired utilities

- [SPATA2-inspired AnnData spatial utilities](t_spata2py.ipynb) - coordinate tables, variable joins, tissue outlines, spatial outlier filtering, unit conversion, benchmark, and a clear note that this is not full SPATA2 parity.

## Preprocess

- [Crop and Rotation of spatial transcriptomic data](t_crop_rotate.ipynb)
- [Visium 10x HD Cellpose](t_cellpose.ipynb)
- [Analyze Nanostring data](t_nanostring_preprocess.ipynb)
- [Analyze Xenium data](t_xenium_preprocess.ipynb)
- [Analyze 10x Atera (WTA Preview) data](t_atera_preprocess.ipynb)
- [Analyze Visium HD data](t_visium_hd_preprocess.ipynb)

## Cluster

See [`cluster/index.md`](cluster/index.md) for the full overview, recommendations and references. One notebook per spatial embedder, all clustered with [`pymclustR`](https://pypi.org/project/pymclustR/) (no rpy2 required):

- [GraphST](cluster/t_cluster_graphst.ipynb) — Long et al., *Nat. Commun.* 2023
- [BINARY](cluster/t_cluster_binary.ipynb) — Lin et al., *Cell Genomics* 2024
- [STAGATE](cluster/t_cluster_stagate.ipynb) — Dong & Zhang, *Nat. Commun.* 2022
- [CAST](cluster/t_cluster_cast.ipynb) — Tang et al., *Nat. Methods* 2024
- [BANKSY](cluster/t_cluster_banksy.ipynb) — Singhal et al., *Nat. Genet.* 2024
- [All methods in one notebook (legacy)](t_cluster_space.ipynb)
- [Spatial integration and clustering](t_staligner.ipynb)

## Deconvolution

- [Identifying Pseudo-Spatial Map](t_spaceflow.ipynb)
- [Spatial deconvolution with reference scRNA-seq](t_decov.ipynb)
- [Spatial deconvolution with RCTD](t_decov_rctd.ipynb)
- [FlashDeconv (fast, GPU-free deconvolution)](t_flashdeconv.ipynb)
- [Spatial deconvolution without reference scRNA-seq](t_starfysh_new.ipynb)

## Downstream

- [Spatial transition tensor of single cells](t_stt.ipynb)
- [Spatial Communication](t_commot_flowsig.ipynb)
- [Spatial IsoDepth Calculation](t_gaston.ipynb)
- [Single cell spatial alignment tools](t_slat.ipynb)

## H&E → spatial transcriptomics (HE-zoo)

See [`he-zoo/index.md`](he-zoo/index.md) for the full overview and recommendations on which backend to pick. Every notebook predicts on the same 10x Visium Breast Cancer Block A Section 1 sample so results are directly comparable.

- [Quick start: HEST-FM (CTransPath + Ridge)](he-zoo/t_histo_hest_fm.ipynb) — Jaume et al., *NeurIPS 2024* Spotlight
- [STPath zero-shot prediction](he-zoo/t_histo_stpath.ipynb) — Huang et al., *npj Digital Medicine* 2025
- [STFlow per-slide fine-tune](he-zoo/t_histo_stflow.ipynb) — Huang et al., *ICML 2025* Spotlight
- [iStar super-resolution](he-zoo/t_histo_istar.ipynb) — Zhang et al., *Nature Biotechnology* 2024
