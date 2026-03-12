# omicverse-tutorials

`omicverse-tutorials` is the standalone documentation and tutorial repository extracted from the `omicverse` monorepo.

It contains:

- user guides and installation docs in `docs/`
- Chinese documentation in `docs_zh/`
- MkDocs configuration in `mkdocs.yml`
- generated static site output in `site/`
- custom documentation templates in `templates/`

## Repository Layout

```text
omicverse-tutorials/
├── docs/           # Main documentation source
├── docs_zh/        # Chinese documentation source
├── site/           # Generated site output
├── templates/      # MkDocs/mkapi templates
├── mkdocs.yml      # Documentation site config
├── conf.py
└── README.md
```

## Local Development

Serve the docs locally from this standalone repository:

```bash
cd /Users/fernandozeng/Desktop/analysis/omicverse-tutorials
mkdocs serve
```

Build the static site:

```bash
mkdocs build
```

## Relationship To `omicverse`

This repository is the source of truth for tutorials and docs.

The main `omicverse` repository consumes it as a git submodule at:

```text
omicverse/omicverse_guide
```

## Maintenance

For repository maintenance and submodule synchronization, see:

- [MAINTENANCE.md](MAINTENANCE.md)
- [MAINTENANCE_CN.md](MAINTENANCE_CN.md)
