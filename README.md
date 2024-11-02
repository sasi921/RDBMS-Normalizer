# RDBMS-Normalizer
Objective:

Develop an automated tool to normalize a relational database schema from 1NF to 5NF. The program will parse user inputs for database schema, functional dependencies (FDs), multi-valued dependencies (MVDs), and data instances where required, providing a final, normalized schema and SQL queries that represent the target normal form.

Program inputs:

The program requires the database schema, including table structure with attributes, primary and candidate keys, and multi-valued attributes; functional dependencies in the form of X → Y to guide normalization; user-specified multi-valued dependencies for 4NF verification; and a target normal form to determine the extent of normalization, outputting SQL CREATE TABLE statements and a normalized schema representation with constraints.

Working of the program:

The program begins by receiving the database schema details, including tables, attributes, primary keys, candidate keys, and any multi-valued attributes. It then reads functional dependencies (FDs) and multi-valued dependencies (MVDs) to guide the normalization process, alongside the user-defined target normal form. Each table is processed independently, ensuring a structured approach to normalization.

As it works, the program applies the normalization rules step-by-step: moving to 1NF by making attributes atomic, then to 2NF by removing partial dependencies, then to 3NF by eliminating transitive dependencies, and finally to BCNF by ensuring all tables have only one candidate key. If the target form is 4NF or 5NF, it further decomposes tables based on verified MVDs, creating fully normalized tables without redundancy.

The program validates MVDs by checking data instances to ensure they hold before decomposing to 4NF. For each normalized table, it outputs an SQL CREATE TABLE statement with appropriate constraints such as primary and foreign keys. The program also provides a detailed schema representation, either in text or diagrammatic form, that shows each table, its attributes, primary keys, and any defined constraints, resulting in a streamlined and efficient database design.

Functionality of each file: The program is organized into four essential components:

main.py: Acts as the primary entry point of the program. This file manages user input redirection, initializes modules, and controls the overall program flow by orchestrating the parsing, normalization, and SQL generation processes.

data_parser.py: Focuses on efficiently parsing input from multiple sources, such as CSV files, text files, or direct user input. This module ensures all data is accurately extracted, cleaned, and formatted for use in the normalization and SQL generation processes.

normalizedformtables.py: Contains the core logic for table normalization, guiding each input relation through a systematic normalization process from 1NF up to 5NF. This file implements the rules and dependencies necessary for decomposing tables into fully normalized forms.

outputallformtables.py: Generates SQL queries based on the normalized tables, creating CREATE TABLE statements with appropriate constraints. This component ensures that each normalized form is represented in SQL format, ready for database creation and deployment.

Team Members:

Sasidhar Reddy Velkuri(svdfy@mst.edu),Venkata Mokshagna Nadella(vnqrd@mst.edu)

