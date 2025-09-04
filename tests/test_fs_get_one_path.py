from pathlib import Path
import pytest
from eli_tools.fs import get_one_path

# Assign constant to satisfy DRY paradigm
PAT_MARIA = '*maria*'

def test_no_matches_rasises_file_not_found(tmp_path: Path):
    # pattern matches nothing
    with pytest.raises(FileNotFoundError):
        get_one_path(tmp_path, PAT_MARIA + '.csv', ext='.csv')

def test_one_match_returns_the_path(tmp_path: Path):
    # create a single matching file; ext compare should be case-insensitive
    p = tmp_path / 'maria_report.csv'
    p.write_text('dummy')
    out = get_one_path(tmp_path, PAT_MARIA, ext='.csv')
    assert out == p

# parametrize with ids
@pytest.mark.parametrize(
        'name', 
        [
            pytest.param('maria.csv', id='lower'),
            pytest.param('maria.CSV', id='upper')
        ]
)
def test_one_match_case_insensitive(tmp_path: Path, name: str):
    p = tmp_path / name
    p.write_text('dummy')
    out = get_one_path(tmp_path, name)
    assert out == p

def test_multiple_matches_raises_value_error(tmp_path: Path):
    (tmp_path / 'maria_1.csv').write_text('a')
    (tmp_path / 'maria_2.csv').write_text('b')
    with pytest.raises(ValueError, match=r'More than one file'):
        get_one_path(tmp_path, PAT_MARIA + '.csv', ext='.csv')

def test_directories_are_ignored(tmp_path: Path):
    # a directory matching the pattern should be ifnored by is_file()
    d = tmp_path / 'fiona_dir'
    d.mkdir()
    f = tmp_path / 'fiona.csv'
    f.write_text('x')
    out = get_one_path(tmp_path, '*fiona*')
    assert out == f

def test_ext_filter_excludes_wrong_suffix(tmp_path: Path):
    # file matches mattern by wrong ext -> behaves like "no match"
    (tmp_path / 'maria_notes.txt').write_text('x')
    with pytest.raises(FileNotFoundError):
        get_one_path(tmp_path, PAT_MARIA, ext='.csv')
