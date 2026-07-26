# Flow Cytometry

Tutorials for the `omicverse.flow` module — flow, spectral and mass cytometry.

**New to `ov.flow`? Start with the [case study](../Tutorials-flow/t_flow_06_case_study.ipynb)** — one complete analysis on real published data, in short `ov.*` calls with the reasoning in the text.

An event is a cell, but nothing else transfers from single-cell RNA-seq. The
file format is FCS; the value a detector reports is contaminated by every other
fluorochrome in the panel; the axis you look at is a nonlinear display scale;
and the analysis is a **sequential gating hierarchy** rather than a clustering.
`ov.flow` owns those, and `ov.io.read_fcs` owns the reading.

The rule the module is built around: **a gate carries the display scale its
boundary was drawn on.** The same vertices mean different populations on a
linear and a logicle axis, so a gate without its transform cannot be re-applied,
saved or shared honestly. Saving to Gating-ML, running one strategy across a
batch, and drawing the gate on the right axis all follow from that one decision.

| Layer | Functions |
|---|---|
| **display transforms** | `Logicle`, `Hyperlog`, `Asinh`, `Log`, `Linear`, `make_transform` |
| **gate geometry** | `RectangleGate`, `PolygonGate`, `EllipsoidGate`, `QuadrantGate`, `BooleanGate` |
| **gating strategy** | `GatingStrategy`, `GatingResult` |
| **compensation** | `compensate`, `spillover_to_compensation`, `spillover_spreading_matrix` |
| **interchange (Gating-ML 2.0)** | `to_gatingml`, `from_gatingml`, `read_gatingml`, `write_gatingml` |
| **clustering** | `flowsom`, `SOM`, `som_metacluster` |
| **plots** | `biaxial`, `histogram`, `backgate`, `hierarchy`, `spillover_heatmap`, `flowsom_heatmap` |

Notebooks 01-04 write their own simulated FCS file — nine known populations, a
real `$SPILLOVER` keyword and a noise floor that goes negative — so they run with
no data of your own. Notebook 05 runs the same module on two real, published,
CC-BY-4.0 experiments downloaded from their original repositories.

```{toctree}
:maxdepth: 1

../Tutorials-flow/t_flow_01_reading_and_compensation
../Tutorials-flow/t_flow_02_gating
../Tutorials-flow/t_flow_03_gatingml
../Tutorials-flow/t_flow_04_flowsom
../Tutorials-flow/t_flow_05_real_data
../Tutorials-flow/t_flow_06_case_study
```

## Installation

```bash
pip install omicverse
```

No extra needed. The transforms are derived from the Gating-ML 2.0 and Parks
2006 specifications and verified bit-for-bit against the reference C
implementation, rather than wrapped from `flowutils` — whose `numpy>=2`
requirement would otherwise be imposed on every omicverse user. FlowSOM is pure
numpy, with no R or Java dependency.
