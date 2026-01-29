# Retool Agent Guidelines

This document provides guidelines for agentic coding agents working on the Retool codebase.

## Project Overview

Retool is a Python desktop utility for filtering Redump and No-Intro DAT files to create One Game, One ROM (1G1R) sets. It has both CLI (`retool.py`) and GUI (`retoolgui.py`) interfaces using PySide6/Qt.

## Development Environment

- **Python**: 3.10+ required
- **Package Manager**: UV (modern Python package manager)
- **Build System**: Hatch with PyInstaller support
- **Dependencies**: PySide6, lxml, strictyaml, alive-progress, darkdetect, psutil, validators

## Build/Style/Test Commands

### Environment Setup
```bash
# Install dependencies using UV
hatch env show
```

### Code Quality Commands
```bash
# Fix code style
hatch run style:fix

# Check code style
hatch run style:check

# Type checking
hatch run types:check

# Linting
hatch run lint:check

# Run all quality checks
hatch run all
```

### Testing Commands
```bash
# Quick tests (Python 3.13 only)
hatch run quick:test

# Full tests (Python 3.10-3.13)
hatch run full:test

# Run single test module
python -m tests.<test_name>

# Common single tests:
python -m tests.unit
python -m tests.exclusions
python -m tests.languages
python -m tests.prefer_regions
python -m tests.compilations
```

### Building
```bash
# Build executable (includes all quality checks)
hatch run build:build

# Build without checks
hatch build --target pyinstaller
```

## Code Style Guidelines

### Formatting
- **Line Length**: 100 characters
- **Formatter**: Black with `skip-string-normalization = true`
- **Import Sorting**: isort with Black profile
- **Linting**: Ruff with comprehensive rule selection

### Import Patterns
```python
# Standard library imports first
import pathlib
import sys
from re import Pattern
from typing import TYPE_CHECKING, Any

# Third-party imports
from PySide6 import QtCore as qtc

# Local imports with explicit module aliases
import modules.constants as const
from modules.utils import eprint

# TYPE_CHECKING imports for type hints only
if TYPE_CHECKING:
    from modules.input import UserInput
```

### Naming Conventions
- **Variables**: `snake_case` with descriptive names
- **Constants**: `UPPER_SNAKE_CASE` (defined in constants.py)
- **Functions**: `snake_case` with verb-first naming
- **Classes**: `PascalCase`
- **Modules**: `snake_case`
- **Type Hints**: Required everywhere (strict MyPy checking)

### Type Annotations
- All functions require explicit type annotations
- Use `from __future__ import annotations` for forward references
- Complex types should be imported from `typing`
- Use `TYPE_CHECKING` guard for import-time type hints

### Error Handling
- Use custom utilities from `modules.utils` for consistent error reporting
- Exception handling should be specific and informative
- Follow Python's EAFP (Easier to Ask for Forgiveness) pattern

### Code Structure
- Modular separation of concerns in `modules/` directory
- Configuration-driven architecture using YAML/JSON
- Main entry points: `retool.py` (CLI) and `retoolgui.py` (GUI)
- Test modules in `tests/` directory, each runnable as `python -m tests.<name>`

### Documentation
- Standard Python docstrings for all public functions
- Comments should explain why, not what
- README.md contains comprehensive project documentation

### Testing Guidelines
- Each feature has dedicated test module
- Tests are runnable as independent Python modules
- Use `sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))` in tests
- Unit tests focus on individual components
- Integration tests verify end-to-end functionality

### Exclusions
- Skip formatting for generated files: `modules/gui/resources_rc.py`, `modules/gui/retool_*.py`
- Spell checking excludes specific words: `-L ue`
- Ruff ignores: `E501`, `E731`, `PLC0206`, `PLC0415`

## Architecture Notes

- **GUI**: PySide6/Qt-based with separate UI files in `qt_source/`
- **Config**: YAML system configs with JSON user configs
- **Data Processing**: XML parsing using lxml for DAT files
- **CLI/GUI Entry Points**: Both share the same core modules
- **Module Structure**: Well-separated concerns (dat/, config/, title_selection/, etc.)

## Development Workflow

1. Run `hatch run style:fix` before committing
2. Run `hatch run types:check` to ensure type safety
3. Run relevant single tests: `python -m tests.<feature>`
4. For changes affecting core functionality, run `hatch run quick:test`
5. Use `hatch run all` for comprehensive validation before major commits

## Project Status

Note: This project is marked as "no longer maintained" as of issue #337. When making changes, prioritize stability and avoid unnecessary refactoring.