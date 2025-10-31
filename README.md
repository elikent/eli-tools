# eli_tools

eli_tools is a 1st-party Python toolbox of small helper functions I reuse across projects.

- Python: 3.12+
- Layout: `src/` (package: `eli_tools`)

## Installation

Editable (local path):

```bash
# from a project venv
pip install -e d:/my-projects/eli-tools
# or (recommended) a relative path from your project folder
pip install -e ..\..\eli-tools
```

## Usage

```python
from pathlib import Path
from eli_tools import fs
from eli_tools import frames

DATA_DIR = Path('...')

# Return exactly one matching file (raises on 0 or >1 matches).
path = fs.get_one_path(DATA_DIR, '*maria*', ext='.csv')
print(path)
```

## Development
### Install editable
a clean way to install package and dev tools into environment
what it does:
   - installs __editable__.eli_tools-0.1.0.pth with path to src which allows my to use eli_tools in this directory
   - installs all dev dependencies in dev in pyproject.toml[project.optional-dependencies] in venv
run when:
   - create a new venv
   - change dev dependencies
   - move project path

```bash
pip install -e .[dev]

# each edit cycle
ruff check . --fix
ruff format .
pytest -q
```

## Release
- Bump `version` in `pyproject.toml`
- Move items from Unreleased -> new section in `CHANGELOG.md`
- Commit & (optionally) tag
```bash
git add -A
git commit -m "chore(release): x.x.x"
git tag -a vx.x.x -m "eli-tools x.x.x"
git push && git push --tags
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
