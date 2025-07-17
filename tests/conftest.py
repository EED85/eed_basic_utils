from collections.abc import Iterator
from pathlib import Path


import pytest


@pytest.fixture(scope="session")
def cfg_test() -> Iterator[dict]:
    home_dir = Path.home()
    cwd = Path.cwd()
    for item in cwd.iterdir():
        if item.is_dir() and item.name[0] != ".":
            subfolder = item
            break
    # Ensure cwd is a valid directory
    cfg_test = {
        "home_dir": home_dir,
        "cwd": cwd,
        "cwd_subfolder": cwd / subfolder,  # Example subfolder, adjust as needed
    }
    yield cfg_test


@pytest.fixture(scope="session")
def prepare_files(cfg_test):
    import tempfile

    tempdir = Path(tempfile.gettempdir())
    file_path = tempdir / "existing_file.txt"
    file_path.touch()
    cfg_test["tempdir"] = tempdir
    yield cfg_test
    file_path.unlink()
