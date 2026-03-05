---
name: python-cli-project-clone-setup
description: Clone python-cli-project from GitHub, customize it with user parameters, remove git remotes, and validate that all tests pass. Use this when an agent needs to create a new customized Python CLI project based on the template.
---

# Python CLI Project Clone & Setup

複製 python-cli-project 範本，自訂參數，並完成初始化設定。

## 📋 Required Input Parameters

先請 user 提供以下 6 個參數：

1. **`project_name`** (example: `my-cli-tool`)
   - 專案資料夾名稱，使用 kebab-case

2. **`package_name`** (example: `my_cli_tool`)
   - Python 套件名稱，使用 snake_case

3. **`cli_command`** (example: `my-cli`)
   - 終端命令名稱，使用 kebab-case

4. **`python_min_version`** (default: `3.13`)
   - 格式：`3.8`, `3.10`, `3.13` 等

5. **`author_name`** (example: `John Doe`)
   - 作者名稱

6. **`author_email`** (example: `john@example.com`)
   - 作者電子郵件

**Stop and request if any parameter is missing.**

## Workflow

Execute these 12 steps in order. Stop and report if any step fails.

### Step 1: Validate Input Parameters

Verify all parameters before proceeding:

- `package_name`: lowercase letters, numbers, underscores only (no hyphens)
- `cli_command`: lowercase letters, numbers, hyphens only (no underscores)
- `project_name`: kebab-case format
- `python_min_version`: format `X.Y` (e.g., `3.8`)

### Step 2: Clone Repository

```bash
git clone https://github.com/mz038197/python-cli-project.git {project_name}
```

Replace `{project_name}` with user-provided value.

### Step 3: Remove Git Remote

```bash
cd {project_name}
git remote remove origin
git remote -v  # Verify empty
```

### Step 4: Rename Package Directory

```bash
mv src/demo_cli src/{package_name}
```

### Step 5: Update Python Files in src/{package_name}/

Update these 4 files with new `package_name`:

1. `__init__.py` - Change docstring, keep `__version__` and imports
2. `__main__.py` - Change docstring only
3. `cli.py` - Change docstring and update:
   ```python
   app = typer.Typer(
       name="{cli_command}",
       help="簡單的 Python CLI 工具示範",
   )
   ```
4. `core.py` - Change docstring only

### Step 6: Update Test Files

1. `tests/test_core.py`:
   - Change docstring
   - Update import: `from {package_name} import core`

2. `tests/test_cli.py`:
   - Change docstring
   - Update import: `from {package_name}.cli import app, main`

### Step 7: Update pyproject.toml

Update `[project]` section:
```toml
name = "{project_name}"
authors = [{name = "{author_name}", email = "{author_email}"}]
requires-python = ">={python_min_version}"
```

Update `[project.scripts]`:
```toml
{cli_command} = "{package_name}.cli:main"
```

### Step 8: Update README.md

Replace all `demo-cli` with `{cli_command}`:
- Title: `# {project_name}`
- Usage examples
- Skill add command (if GitHub username provided)

### Step 9: Remove Skills Folder

```bash
rm -r skills
```

### Step 10: Create and Activate Virtual Environment

Create a virtual environment first:

```bash
py -m venv venv
```

Activate it:

```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 11: Install Project

Inside the activated virtual environment:

with uv:

```bash
uv pip install -e .
```

or pip:

```bash
pip install -e .
```

### Step 12: Run Tests

Inside the activated virtual environment:

```bash
pytest
```

Verify all tests pass (exit code 0).

### Step 13: Verify CLI Commands

Test each command works (still in venv):

```bash
{cli_command} --help
{cli_command} hello World
{cli_command} add 10 5
```

### Step 14: Commit Initial State

```bash
git add .
git commit -m "Initial project setup from template"
```

## ✅ Validation Checklist

Mark complete only when ALL are true:

- [ ] All 6 parameters provided and validated
- [ ] Project cloned successfully
- [ ] Git remote removed
- [ ] Package directory renamed
- [ ] All src files updated
- [ ] All test files updated
- [ ] pyproject.toml configured correctly
- [ ] README.md updated
- [ ] skills/ folder deleted
- [ ] Virtual environment created and activated
- [ ] Project installed without errors (in venv)
- [ ] All pytest tests pass (in venv)
- [ ] CLI commands work (`--help`, `hello`, `add` in venv)
- [ ] Initial git commit created

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Git clone fails | Verify internet connection and GitHub URL |
| Import errors | Check all 4 Python files in `src/{package_name}/` have correct imports |
| Tests fail | Ensure `pyproject.toml` CLI entrypoint is `{package_name}.cli:main` |
| Command not found | Make sure virtual environment is activated (use `source venv/bin/activate` or `venv\Scripts\activate`) |
| Permission denied | Use `rm -rf skills/` with elevated permissions if needed |
| Module not found after install | Verify `pip install -e .` ran successfully inside the activated venv |

## Post-Setup

After successful setup, user can:

1. Add remote and push to their repository:
   ```bash
   git remote add origin https://github.com/{username}/{project_name}.git
   git push -u origin main
   ```

2. Start developing CLI commands in `src/{package_name}/cli.py`

3. Add business logic in `src/{package_name}/core.py`

4. Add tests following existing patterns in `tests/`
