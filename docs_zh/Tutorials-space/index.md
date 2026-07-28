

## Arrangement, niches and 3-D

- [How the tissue is arranged: spatial statistics and niches](t_spatial_arrangement.ipynb) — neighbourhood enrichment, co-occurrence over distance, group centrality, Ripley, distance-from-anchor gradients, region masking, and the three flavours of niche analysis ([issue #760](https://github.com/omicverse/omicverse/issues/760)).
- [From serial sections to a volume, and reading Stereo-seq](t_spatial_3d.ipynb) — `ov.space.geom` alignment validated against known rotations, 3-D stacking, section interpolation, and the Stereo-seq GEM reader with bin-size sweep.

## 受 SPATA2 启发的工具

- [受 SPATA2 启发的 AnnData 空间工具](t_spata2py.ipynb) - 坐标表、变量拼接、组织轮廓、空间离群点过滤、单位换算、benchmark，并明确说明这不是完整 SPATA2 parity。

# 空间转录组学教程

此页面镜像了 `mkdocs.yml` 中的 `Space` 部分，为空间教程笔记本提供了一个 markdown 入口点。

## 预处理

- [空间转录组学数据的裁剪和旋转](t_crop_rotate.ipynb)
- [Visium 10x HD Cellpose](t_cellpose.ipynb)
- [分析 Nanostring 数据](t_nanostring_preprocess.ipynb)
- [分析 10x Atera (WTA Preview) 数据](t_atera_preprocess.ipynb)
- [分析 Visium HD 数据](t_visium_hd_preprocess.ipynb)
- [空间聚类和表达去噪](t_cluster_space.ipynb)
- [空间整合与聚类](t_staligner.ipynb)

## 反卷积

- [识别伪空间图](t_spaceflow.ipynb)
- [基于参考 scRNA-seq 的空间反卷积](t_decov.ipynb)
- [使用 RCTD 进行空间反卷积](t_decov_rctd.ipynb)
- [FlashDeconv (快速、无GPU反卷积)](t_flashdeconv.ipynb)
- [无参考 scRNA-seq 的空间反卷积](t_starfysh_new.ipynb)

## 下游分析

- [单细胞的空间转移张量](t_stt.ipynb)
- [空间通讯](t_commot_flowsig.ipynb)
- [空间 IsoDepth 计算](t_gaston.ipynb)
- [单细胞空间对齐工具](t_slat.ipynb)
