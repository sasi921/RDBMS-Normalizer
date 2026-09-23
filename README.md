# RDBMS Normalizer

A Python tool for exploring relational-database normalization from **1NF through 5NF**. It reads relation data and dependency definitions, applies normalization logic, and produces normalized table representations and SQL-oriented output.

## What this project demonstrates

- Parsing tabular input and dependency definitions
- Functional-dependency analysis and candidate/superkey reasoning
- Progressive normalization across 1NF, 2NF, 3NF, BCNF, 4NF, and 5NF
- Multivalued-dependency handling for higher normal forms
- SQL-oriented output for decomposed relations

## Repository structure

The current repository uses these top-level files:

| File | Purpose |
| --- | --- |
| `Main.py` | Command-line entry point and orchestration |
| `data_parser.py` | Converts input data into the structures used by the normalizer |
| `normalizedformtables.py` | Core normalization and dependency logic |
| `outputallformtables.py` | Formats normalized relations and SQL-oriented output |
| `Student.csv` | Small example relation used to exercise the program |
| `Functionaldependencies.txt` | Example functional-dependency definitions |
| `mvd_fds.txt` | Example multivalued-dependency definitions |
| `RDBMS Normalizer.pdf` | Project report and design background |

> Note: the entry point is named `Main.py` with a capital **M**. This matters on case-sensitive operating systems.

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/sasi921/RDBMS-Normalizer.git
cd RDBMS-Normalizer
```

### 2. Create an isolated Python environment

```bash
python -m venv .venv
```

Activate it with the command appropriate for your operating system, then install the project dependencies if a dependency manifest is present on the branch you are using.

The source imports `pandas`, so a minimal manual setup is:

```bash
python -m pip install pandas
```

### 3. Run the normalizer

```bash
python Main.py
```

The repository includes `Student.csv`, `Functionaldependencies.txt`, and `mvd_fds.txt` as small example inputs for exploring the workflow.

## How the normalization workflow fits together

1. **Input parsing** — relation data and dependency definitions are loaded and converted into Python structures.
2. **Dependency analysis** — the program reasons about functional dependencies, keys, and normalization conditions.
3. **Progressive decomposition** — relations are transformed toward the requested normal form.
4. **Higher-normal-form checks** — multivalued dependencies are considered for 4NF/5NF processing.
5. **Output generation** — the resulting relations are formatted for inspection and SQL-oriented use.

This separation keeps input handling, normalization logic, and output generation in distinct modules, making the implementation easier to inspect and extend.

## Example inputs

The checked-in sample files are intentionally small so the algorithm can be reviewed without first sourcing an external dataset. When experimenting with your own schema, keep a copy of the example files and introduce changes incrementally; higher-normal-form behavior depends on the supplied dependency definitions as well as the relation data.

## Project scope

This repository is an educational implementation of relational normalization concepts rather than a production database-migration system. Generated decompositions and SQL should be reviewed before applying them to a real database, especially when working with domain-specific constraints that cannot be inferred from sample data alone.

## Team

- Sasidhar Reddy Velkuri
- Venkata Mokshagna Nadella
