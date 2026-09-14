# RDBMS Normalizer

A Python-based database design tool that demonstrates how relational schemas can be decomposed through successive normal forms using functional dependencies (FDs), multivalued dependencies (MVDs), candidate keys, and sample data.

## Why this project matters

Database normalization is easy to describe on paper and harder to automate correctly. This project turns the theory into an executable workflow: parse a relation, reason about dependencies, decompose the schema toward a requested normal form, and generate SQL-oriented output that makes the resulting design easier to inspect.

## What it does

- Reads a sample relation from CSV input.
- Parses functional dependencies and multivalued dependencies from text files.
- Processes normalization stages from **1NF through 5NF**.
- Uses data instances when needed to help evaluate multivalued dependencies.
- Produces normalized relation structures and SQL-style output.
- Keeps parsing, normalization logic, and output generation separated into focused modules.

## Architecture

```text
Input files
   │
   ├── CSV relation data
   ├── functional dependencies
   └── multivalued dependencies
   │
   ▼
data_parser.py
   │
   ▼
normalizedformtables.py
   │
   ▼
outputallformtables.py
   │
   ▼
Normalized relations + SQL output
```

`Main.py` coordinates the end-to-end flow.

## Repository structure

```text
RDBMS-Normalizer/
├── Main.py
├── data_parser.py
├── normalizedformtables.py
├── outputallformtables.py
├── Student.csv
├── Functionaldependencies.txt
├── mvd_fds.txt
└── README.md
```

## Quick start

### Requirements

- Python 3.10+ recommended
- No external database server is required to inspect the normalization workflow

### Run

```bash
git clone https://github.com/sasi921/RDBMS-Normalizer.git
cd RDBMS-Normalizer
python Main.py
```

The repository includes a sample `Student.csv` relation along with dependency files so the project can be explored without creating input files from scratch.

## Normalization workflow

The project applies the major ideas behind each stage:

| Normal form | Goal |
|---|---|
| 1NF | Keep attribute values atomic |
| 2NF | Remove partial dependency on a composite key |
| 3NF | Remove transitive dependency |
| BCNF | Require determinants to be candidate keys |
| 4NF | Remove non-trivial multivalued dependencies |
| 5NF | Decompose relations where join dependencies require it |

## Key modules

### `data_parser.py`
Loads and prepares relation data and dependency definitions for the normalization pipeline.

### `normalizedformtables.py`
Contains the core decomposition and normal-form logic.

### `outputallformtables.py`
Formats normalized relations and generates SQL-oriented output for inspection.

### `Main.py`
Connects the parser, normalization workflow, and output layer. Input files are resolved relative to the project source so the program is less dependent on the shell's working directory.

## Engineering concepts demonstrated

`Python` · `Relational Databases` · `Functional Dependencies` · `Schema Decomposition` · `Database Normalization` · `SQL Generation` · `Modular Program Design`

## Current scope

This is an academic implementation intended to demonstrate database-normalization concepts. It is not positioned as a replacement for a production database-design tool. A strong next step would be to add a formal test suite covering representative FD/MVD decompositions and expected normalized schemas.

## Contributors

- Sasidhar Reddy Velkuri
- Venkata Mokshagna Nadella
