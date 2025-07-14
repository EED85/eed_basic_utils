import os
from collections.abc import Iterator
from pathlib import Path


import pytest


@pytest.fixture(scope="session")
def cfg_test() -> Iterator[dict]:
    home_dir = os.path.expanduser("~")
    cfg_test = {
        "home_dir": home_dir,
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
