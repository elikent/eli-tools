# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- _TBD_
### Changed
- _TBD_
### Removed
- _TBD_

## [0.1.1] - 2025-11-10
### Added
- `text_utils.canon()`: lower-cases all letters and replaces \s with hyphen
- `text_utils.remove_diacritics()`: removes diacritics
- `log_utils.report()`: log results and optionally print
- `log_utils.logging_config()`: Configure global logging for the application
- `file_transforms.combine_pdfs()`: combine multiple pdfs into one
- `file_transforms.remove_pages()`: remove pages from pdf
### Changed
_None_

### Removed
_None_

## [0.1.0] - 2025-09-05
### Added
- `fs.get_one_path(data_dir, pattern, *, ext=None)`: return exactly one matching file or raise helpful errors.
- Basic package structure (`src/` layout), `pyproject.toml`.
- Ruff config and dev extras (`pytest`, `ruff`, `mypy`).
- Initial tests for `get_one_path`.
### Changed
_None_

### Removed
_None_
