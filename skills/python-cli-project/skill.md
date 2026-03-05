---
name: python-cli-project-builder
description: Build a production-ready Python CLI project scaffold with Typer, setuptools, pytest, packaging metadata, and release workflow. Use when an agent needs to create or regenerate a pip/uv-installable CLI tool repository from scratch.
---

# Python CLI Project Builder

Create a reusable Python CLI project with clean layering, tests, and packaging based on Typer and setuptools.

## Inputs

Require these values before execution:

1. `project_name` (example: `cli-tool-test`)
2. `package_name` (example: `cli_tool_test`)
3. `cli_command` (example: `cli-tool-test`)
4. `python_min_version` (default: `3.13`)
5. `author_name`
6. `author_email`

If any required value is missing, stop and request it.

**Location**: Create project at `{workspace_root}/{project_name}/`

## Target Structure

Create this exact structure:

```text
<project_name>/
├── src/
│   └── <package_name>/
│       ├── __init__.py
│       ├── __main__.py
│       ├── core.py
│       └── cli.py
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   └── test_cli.py
├── skills/
│   └── <cli_command>/
│       └── SKILL.md
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## Build Workflow

Execute steps in order.

### 1. Initialize Repository Files

1. Create project root directory: `{workspace_root}/{project_name}/`
2. Create directories `src/<package_name>` and `tests`.
3. Create `__init__.py` with `__version__ = "0.1.0"` and import `core`.
4. Create `__main__.py` as module execution entry point.
5. Create `.gitignore` for Python, venv, cache, coverage, build artifacts, `*.egg-info`.
6. Create `skills/<cli_command>/` directory with skill documentation.

### 2. Configure Packaging (`pyproject.toml`)

1. Set build backend to `setuptools.build_meta`.
2. Fill `[project]` fields using input values.
3. Set Python minimum version (e.g., `>=3.8`).
4. Add runtime dependencies:
   - `typer>=0.12.0`
5. Add dev dependencies:
   - `pytest>=8.0.0`
6. Set CLI entrypoint:
   - `[project.scripts]`
   - `<cli_command> = "<package_name>.cli:main"`
7. Set setuptools configuration:
   - `[tool.setuptools]`
   - `package-dir = {"" = "src"}`
   - `[tool.setuptools.packages]`
   - `find = {where = ["src"]}`

### 3. Implement Core Layer (`core.py`)

Create pure business logic layer with NO CLI dependencies:

1. Implement business logic functions (e.g., `greet()`, `add_numbers()`).
2. Keep functions independent from `typer`, `print()`, or `sys.exit()`.
3. Add comprehensive docstrings with Args and Returns.
4. Focus on reusability - these functions should be usable outside CLI context.

Minimum sample functions:

1. `greet(name: str = "World") -> str` - greeting function
2. `add_numbers(nums: List[float]) -> float` - arithmetic operation

### 4. Implement CLI Layer (`cli.py`)

CLI layer handles user interaction using Typer decorators:

1. Import Typer: `import typer`
2. Import `core` module: `from . import core`
3. Create Typer app: `app = typer.Typer(name="...", help="...")`
4. Define commands using `@app.command()` decorator.
5. Use `typer.Argument()` and `typer.Option()` for parameters.
6. Use `typer.echo()` for output instead of `print()`.
7. Keep all I/O and error handling in this layer only.

Example command:

```python
@app.command()
def hello(
    name: str = typer.Argument("World", help="Name to greet"),
) -> None:
    """Greet a user"""
    result = core.greet(name)
    typer.echo(result)
```

**Advantages**:
- Automatic help generation with `--help`
- Type hints directly define CLI parameters
- Less boilerplate than argparse
- Rich output support built-in
- Shell completion support

### 5. Implement `__main__.py`

Create module execution entry point:

```python
import sys
from .cli import app

if __name__ == "__main__":
    app()
```

Or with exit code handling:

```python
import sys
from .cli import main

if __name__ == "__main__":
    sys.exit(main())
```

### 6. Implement Tests

Separate tests into two files for clear separation of concerns:

**`tests/test_core.py`** - Test pure business logic:

1. Test each core function with various inputs.
2. No dependencies on CLI or I/O.
3. Cover edge cases: empty lists, negative numbers, zero, floats, etc.
4. Use simple assertions without mocking.

Example test class:

```python
class TestGreet:
    def test_greet_default(self):
        assert core.greet() == "你好，World！..."
    
    def test_greet_with_name(self):
        assert core.greet("Alice") == "你好，Alice！..."
```

**`tests/test_cli.py`** - Test CLI interface using Typer CliRunner:

1. Import `CliRunner` from `typer.testing`.
2. Create runner instance: `runner = CliRunner()`
3. Test commands: `result = runner.invoke(app, ["command", "arg"])`
4. Check exit code: `assert result.exit_code == 0`
5. Check output: `assert "expected text" in result.stdout`

Example test:

```python
from typer.testing import CliRunner
from demo_cli.cli import app

runner = CliRunner()

def test_hello_command():
    result = runner.invoke(app, ["hello", "Alice"])
    assert result.exit_code == 0
    assert "你好，Alice" in result.stdout
```

### 7. Create Skill Documentation

Create `skills/<cli_command>/SKILL.md`:

1. Document the CLI tool purpose and features.
2. Include usage examples for all commands.
3. Explain command arguments and options.
4. Provide integration guidance for Claude Code Agent.
5. Document the `core` module functions if meant for programmatic use.

### 8. Write README

Include:

1. install via `pip` (editable: `pip install -e .` and global: `pip install .`)
2. install via `uv` (parallel commands)
3. usage examples for all commands
4. development setup
5. test command (`pytest` or `uv run pytest`)
6. release workflow
7. project structure explanation (core vs CLI separation)

### 9. Validate

Run and pass:

1. `<cli_command> --help` - verify help text is auto-generated
2. `<cli_command> <command> --help` - verify command-specific help
3. `python -m <package_name> --help` - module execution
4. `pytest` (or `uv run pytest`) - all tests must pass
5. `pip install -e .` - editable install works
6. All command examples from README work correctly

If any command fails, fix files and rerun until all pass.

## Rules

1. **Separate concerns**: Pure business logic in `core.py`, CLI handling in `cli.py`.
2. **Use Typer** with `@app.command()` decorators for modern CLI definition.
3. **No I/O in core**: Core functions must not use `typer.echo()`, `input()`, or `sys.exit()`.
4. **Testability first**: Write core functions so they're easy to test without mocking.
5. **Add `__main__.py`** for module execution (`python -m <package_name>`).
6. **Test both layers**: Separate `test_core.py` and `test_cli.py`.
7. **Use CliRunner** from `typer.testing` for CLI testing.
8. **Use setuptools** with `src/` layout for packaging.
9. **Keep it minimal**: Start with 1-2 commands and 1-2 core functions.
10. **Update `README.md`** when command interface changes.
11. **Bump version** in both `__init__.py` and `pyproject.toml` before release.
12. **Update `CHANGELOG.md`** for each release.
13. **Support both** `pip install` and `uv pip install`.
14. **Add `*.egg-info`** to `.gitignore` (auto-generated, not version controlled).

## Definition of Done

Mark complete only when all are true:

1. project structure matches target structure (including `core.py`)
2. `core.py` has pure business logic with no CLI dependencies (2+ functions)
3. `cli.py` uses Typer decorators with `@app.command()` (2+ commands)
4. CLI entrypoint `main` is exposed at module level in `cli.py` and handles exceptions
5. CLI entrypoint works after editable install (`pip install -e .`)
6. module execution works (`python -m <package_name>`)
7. all tests pass (`pytest` returns 0)
8. `test_core.py` has 5+ core function tests
9. `test_cli.py` uses `CliRunner` from `typer.testing` (4+ tests)
10. `--help` output is auto-generated and readable
11. README examples match actual command behavior
12. skill documentation is accurate and complete