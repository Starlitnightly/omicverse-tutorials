# Maintenance Guide

This repository is maintained as a standalone project and is also consumed from the main `omicverse` repository as a git submodule.

## 1. Repository Relationship

- Standalone repo: `analysis/omicverse-tutorials`
- Parent repo: `analysis/omicverse`
- Submodule path inside parent repo: `omicverse/omicverse_guide`

Normal workflow:

1. Make documentation changes in `omicverse-tutorials`.
2. Commit and push in `omicverse-tutorials`.
3. Update the submodule pointer in `omicverse`.

## 2. Daily Development In `omicverse-tutorials`

```bash
cd /Users/fernandozeng/Desktop/analysis/omicverse-tutorials
git status
git checkout main
git pull origin main
```

After editing:

```bash
git add -A
git commit -m "Describe the tutorial update"
git push origin main
```

## 3. Sync The New Commit Back To `omicverse`

After pushing the standalone repo, update the parent repository:

```bash
cd /Users/fernandozeng/Desktop/analysis/omicverse
git submodule update --init --recursive
cd omicverse_guide
git checkout main
git pull origin main
cd ..
git add omicverse_guide .gitmodules
git commit -m "Update omicverse_guide submodule"
git push
```

If `.gitmodules` did not change, `git add omicverse_guide` is enough.

## 4. How Another Clone Updates The Submodule

```bash
cd /Users/fernandozeng/Desktop/analysis/omicverse
git pull --recurse-submodules
git submodule update --init --recursive
```

If the submodule already exists but is behind:

```bash
cd /Users/fernandozeng/Desktop/analysis/omicverse/omicverse_guide
git checkout main
git pull origin main
cd ..
git add omicverse_guide
```

## 5. Clone From Scratch

```bash
git clone --recurse-submodules https://github.com/Starlitnightly/omicverse.git
```

If the repo was cloned without submodules:

```bash
cd omicverse
git submodule update --init --recursive
```

## 6. Common Pitfalls

- Do not update only the submodule pointer in `omicverse` and forget to push the real documentation commit in `omicverse-tutorials`.
- Do not treat `omicverse/omicverse_guide` as the long-term source of truth; use `analysis/omicverse-tutorials`.
- If the submodule is in detached HEAD state, run `git checkout main` inside `omicverse_guide` before pulling.
