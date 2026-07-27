# Structure, Docking & Dynamics

Tutorials for the `omicverse.mol` module — the bridge from an omics **target
protein** to its **3D structure**, its **drug context**, and how both **behave
over time**.

A typical omicverse analysis ends with a target: a differential gene from
`ov.bulk`, a marker or driver from `ov.single`, a variant from `ov.genetics`.
The natural next questions are structural and pharmacological — *what does the
protein look like in 3D, where are its confident regions, does it have a
druggable pocket, are there known drugs against it, and can a candidate
molecule bind it?* `ov.mol` answers them, with **interactive 3D
visualization** (py3Dmol) that renders inline in Jupyter and **persists in the
exported HTML docs**.

The notebooks follow the natural arc *see the target → assess it → test a drug
→ watch it move*, and each one follows the analysis workflow the field
actually uses — with the discipline (model-confidence assessment, redocking
validation, minimisation and equilibration before production) a structural
biologist or computational chemist would apply. They run real targets —
**EGFR** and **ubiquitin** — framed as hits handed over by an upstream omics
analysis.

| Notebook | What you learn |
|---|---|
| **Structure** | Fetch / predict and interactively visualize a target's structure — and assess model confidence (pLDDT, PAE) *before* trusting it. |
| **Druggability** | Detect binding pockets, score druggability, and check what drugs are already known — structure-based target prioritization. |
| **Docking** | Validate a docking protocol by redocking, then dock a candidate molecule and inspect the binding pose. |
| **Dynamics** | Take a static model or a docked pose and actually *run* it: solvate, minimise, equilibrate, produce a trajectory on the GPU, then read stability (RMSD/RMSF/DSSP) and rescore binding with MM-GBSA. |

```{toctree}
:maxdepth: 1

../Tutorials-mol/t_mol_structure
../Tutorials-mol/t_mol_druggability
../Tutorials-mol/t_mol_docking
../Tutorials-mol/t_mol_dynamics
```

## Why add dynamics

Structure prediction and docking both hand you a **single static snapshot**.
That snapshot cannot tell you whether a loop is genuinely ordered or whether a
docked pose survives more than a picosecond of thermal motion. Molecular
dynamics adds the missing axis:

* an **AlphaFold model** → is the fold stable, and which regions are floppy
  (`rmsf`) rather than merely low-pLDDT?
* a **docked pose** → does the ligand stay in the pocket, and what is its
  binding free energy averaged over an *ensemble* rather than one pose?

That last step is what `ov.mol` uniquely chains end to end:

```python
result = ov.mol.dock(s, 'erlotinib', pocket=1)   # static pose + Vina score
traj   = ov.mol.simulate(result, ns=5)           # relax it with real dynamics
res    = ov.mol.mmgbsa(traj)                     # ensemble-averaged ΔG
```

`dock → MD → MM-GBSA` in three calls, with the receptor carried through
automatically. Docking alone gives you a point; MD alone gives you a process;
only the chain gives you a *rescored* answer.

## Installation

The structural-biology stack is optional. The core layer — structure
acquisition, interactive visualization and known-drug lookup:

```bash
pip install 'omicverse[mol]'
```

The docking layer (AutoDock Vina + receptor / ligand preparation):

```bash
pip install 'omicverse[mol-dock]'
```

Binding-pocket detection uses `rust-fpocket`, a pip-installable Rust port of
fpocket:

```bash
pip install fpocket-rs
```

The molecular-dynamics layer (OpenMM engine + MDTraj analysis):

```bash
pip install 'omicverse[md]'
```

**On a GPU machine, install OpenMM from conda-forge instead.** Its CUDA build
is far more likely to match your driver, and the PyPI OpenMM (<8.2) is
incompatible with NumPy 2:

```bash
conda install -c conda-forge openmm mdtraj
```

PDBFixer — needed to repair structures before simulation — is **not published
on PyPI**, so omicverse vendors it (`omicverse.external.pdbfixer`). You never
install it separately.

To simulate a protein–**ligand** complex (`ov.mol.simulate(docking_result)`,
`ov.mol.mmgbsa`) you also need small-molecule parameterisation. Note that
**AmberTools is required, not optional**: both GAFF and OpenFF assign AM1-BCC
partial charges, which are computed by AmberTools' `sqm`. It is conda-only, so
install the ligand stack from conda-forge:

```bash
conda install -c conda-forge openmmforcefields openff-toolkit ambertools
```

Without it, parameterisation fails with *"no registered toolkits can provide
assign_partial_charges"*. (`openff-nagl` is a lighter alternative that predicts
charges with a graph network instead of running semi-empirical QM.)

Two environment gotchas worth knowing, because both surface as that same
unhelpful message:

* the OpenFF toolkit locates AmberTools with `shutil.which`, so an interpreter
  launched by absolute path (a Jupyter kernel, a cron job, an environment that
  was never "activated") will not see it — put the environment's `bin` on
  `PATH`;
* `antechamber` needs **`AMBERHOME`** set to find its parameter files, and
  exits non-zero without it: `export AMBERHOME=/path/to/env`.

`ov.mol` detects both cases and says exactly which one you are in.

### Checking you are actually on the GPU

Every run prints the OpenMM platform it resolved. If you see `CPU` where you
expected `CUDA`, the CUDA build is not installed or does not match your
driver — MD on CPU is 10–100× slower and only viable for toy systems.

```python
traj = ov.mol.simulate(s, ns=1)     # prints "OpenMM platform: CUDA (precision=mixed)"
traj.provenance['platform']          # 'CUDA'
```

Force a device with `platform='CUDA'` or the `OMICOS_MD_DEVICE` environment
variable.
