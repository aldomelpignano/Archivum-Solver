⚠️ **Project Status — Early Development / Roadmap**

Archivum Solver is currently in **early development**. Many features described in this document are **not yet implemented**. This README should be considered a **roadmap and design specification** describing the planned architecture and capabilities of the project.

The goal of this document is to outline the direction of development and the intended functionality of Archivum Solver.


# Archivum Solver

**Archivum Solver** (from Latin *Archivum* — archive, repository — and *Solver* — one who solves) is a command-line tool designed to automatically analyze and solve password-protected compressed archives.

The project is intended primarily for:

- Capture The Flag (CTF) competitions
- security research and experimentation
- automated archive analysis
- password auditing in controlled environments

Archivum Solver aims to automate the process of discovering passwords, extracting archives, scanning their contents, and recursively processing newly discovered archives.

The long-term vision is to create a **fully automated archive-solving engine** capable of navigating complex nested archive structures commonly found in CTF challenges.

# Project Goals

Archivum Solver is designed with the following goals:

- automate password discovery for protected archives
- support multiple archive formats
- recursively process nested archives
- safely extract archives while preventing resource exhaustion
- collect detailed statistics about cracking attempts
- provide a modular architecture for future expansion



### Archive Support

Planned support for common archive formats:

- ZIP
- 7Z
- RAR

Additional formats may be added in the future.


### Password Cracking

Archivum Solver aims to support multiple password discovery strategies:

- **Dictionary attacks** Using password lists.

- **Brute-force attacks**

Automatic generation of passwords based on configurable parameters:

- character sets
- minimum and maximum length
- pattern-based generation


### Recursive Archive Extraction

Archivum Solver will be able to automatically detect archives contained inside other archives.

Example structure:

```bash

challenge.zip
└── archive.7z
└── hidden.rar
└── flag.txt

```

The solver will:

1. crack the outer archive
2. extract its contents
3. scan for additional archives
4. repeat the process

This allows the tool to automatically navigate complex archive chains.



### Parallel Processing

Future versions aim to support:

- multi-threaded password testing
- parallel archive analysis
- efficient task scheduling

This will allow Archivum Solver to process large wordlists or multiple archives more efficiently.



### Statistics and Monitoring

Archivum Solver will include a statistics system capable of tracking:

- total password attempts
- cracking speed (attempts per second)
- number of archives analyzed
- number of archives successfully cracked
- total files extracted
- total data extracted
- execution time
- maximum archive nesting depth

Statistics may be displayed in real time or exported to structured formats such as JSON.



### Configuration System

A configuration file will allow users to define default parameters.

Planned location:

```

~/.config/Archivum Solver/config.toml

````

Example configuration:

```toml
threads = 8
recursive = true
max_depth = 20
max_extract_size = "5GB"

[wordlists]
default = "/usr/share/wordlists/rockyou.txt"

[bruteforce]
enabled = true
min_length = 1
max_length = 6
charset = "a-zA-Z0-9"
````

Command line arguments will override configuration file settings.



### Resource Protection

Archivum Solver aims to implement safeguards against malicious or malformed archives.

These protections include:

* maximum extraction size limits
* archive nesting depth limits
* file count limits
* protection against zip bombs

Such protections are necessary when processing untrusted archive inputs.



# Planned Command Line Interface

Example usage:

```
Archivum Solver -w passwords.txt challenge.zip
```

Recursive extraction:

```
Archivum Solver -r -w rockyou.txt challenge.zip
```

Brute-force mode:

```
Archivum Solver -b -l 1-6 archive.zip
```



# Architecture (Planned)

The planned architecture is modular.

```
CLI
 │
 ├── Config Loader
 │
 ├── Solver Engine
 │     ├── Password Cracker
 │     ├── Archive Extractor
 │     └── Archive Scanner
 │
 └── Statistics Collector
```

Each module will be responsible for a specific task:

* **Password Cracker**
  tests candidate passwords

* **Archive Extractor**
  extracts archives once passwords are found

* **Archive Scanner**
  detects additional archives in extracted content

* **Statistics Collector**
  tracks execution metrics

This modular architecture should allow easy expansion and integration of new archive formats or cracking strategies.



# Current Status

The project is **not yet feature-complete**.

Some components may exist only as prototypes or design ideas.

Future development will gradually implement the planned functionality described in this roadmap.



# Disclaimer

Archivum Solver is intended **only for legal and authorized security research**, including:

* Capture The Flag competitions
* academic security experimentation
* controlled environments

Users are responsible for complying with all applicable laws and regulations.


```
