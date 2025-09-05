from pathlib import Path


def get_one_path(data_dir: Path, pattern: str, *, ext: str | None = None) -> Path:
    """
    Return exactly one matching file Path in 'data_dir' for pattern.

    - Raises FileNotFoundError if no files match.
    - Raises ValueError if more than one file matches.
    - If 'ext' is provided (e.g. 'csv'), enforce that suffix (case-insensitive).
    """
    it = (
        p
        for p in data_dir.glob(pattern)
        if p.is_file() and (ext is None or p.suffix.lower() == ext.lower())
    )
    first = next(it, None)
    if first is None:
        raise FileNotFoundError(f"No file matching {pattern!r} in {data_dir}")
    second = next(it, None)
    if second is not None:
        raise ValueError(f"More than one file matching {pattern!r} in {data_dir}")
    return first
