# Tutorials of Flow Cytometry

Tutorials for the `omicverse.flow` module — flow, spectral and mass cytometry.

Cytometry is a modality, not a sub-analysis of single-cell RNA-seq. An event is
a cell, but the file format, the display scalings, the compensation model and
above all the sequential **gating hierarchy** have no analogue anywhere else in
omicverse — so they get their own module rather than a corner of `ov.single`.

| What `ov.flow` owns | Functions |
|---|---|
| **display transforms** | `Logicle`, `Hyperlog`, `Asinh`, `Log`, `Linear`, `make_transform` |
| **gate geometry** | `RectangleGate`, `PolygonGate`, `EllipsoidGate`, `QuadrantGate`, `BooleanGate` |
| **the gating strategy** | `GatingStrategy`, `GatingResult` |
| **compensation** | `compensate`, `spillover_to_compensation`, `spillover_spreading_matrix` |
| **interchange** | `to_gatingml`, `from_gatingml`, `read_gatingml`, `write_gatingml` |
| **clustering** | `flowsom`, `SOM`, `som_metacluster` |
| **plots** | `biaxial`, `histogram`, `backgate`, `hierarchy`, `spillover_heatmap`, `flowsom_heatmap` |

Reading FCS files is **not** here — that is `ov.io.read_fcs`, because it is I/O.

The idea the module is built around: **a gate carries the display scale its
boundary was drawn on.** A polygon drawn on a logicle axis and the same vertices
read as linear values describe completely different populations, so a gate that
does not carry its transform cannot be re-applied, saved or shared honestly.
Everything else — plotting the gate, writing it to Gating-ML, running one
strategy across ninety samples — follows from that.

## The series

- [Reading FCS, compensation and display scales](t_flow_01_reading_and_compensation.ipynb) — `ov.io.read_fcs` and what lands in the `AnnData`; the spillover matrix and what it does to a plot; why a log axis cannot display compensated data, and how logicle's `W` parameter is chosen.
- [Gates, the gating strategy, and reading the numbers](t_flow_02_gating.ipynb) — the five gate geometries, the strategy tree, parent-restricted evaluation, `stats()` and its `low_n` warning, the quadrant plot, the hierarchy, and back-gating as the check that catches a bad gate.
- [Saving a strategy and applying it to a batch](t_flow_03_gatingml.ipynb) — round-tripping through a dict and through **Gating-ML 2.0** (the ISAC interchange standard that FlowJo, Cytobank and flowCore read), one strategy over three samples, and diffing two strategies.
- [FlowSOM — and what clustering does not replace](t_flow_04_flowsom.ipynb) — the cytometry-standard unsupervised method in pure numpy, shown working *and* shown failing in the specific way it fails when the gating is skipped.
- [The whole module on real data](t_flow_05_real_data.ipynb) — two real, published, CC-BY-4.0 experiments: a BD LSRFortessa PBMC panel with a genuine 13x13 spillover matrix, and a Cytek Aurora spectral panel with the FSC-H a singlet gate needs. Covers what only real data can teach: `$PnR` rather than a hard-coded top of scale, fitting the logicle `W` to the detector noise, and a pooled frequency that turns out to be one sample's failed stain.

Notebooks 01-04 write their own simulated FCS file, so they need no data of your
own and each stands alone. Notebook 05 downloads its two datasets from Zenodo and
PLOS on first use.

## Installation

```bash
pip install omicverse
```

There is nothing else to install. The transforms are derived from the GatingML
2.0 and Parks 2006 specifications rather than wrapped from `flowutils` — which
would force a numpy major version on every omicverse user — and the FlowSOM
implementation is pure numpy with no R or Java dependency. Writing the demo
files in the tutorials needs `flowio`, which `ov.io.read_fcs` already uses.
