from eed_basic_utils.os import get_git_root
import pytest


@pytest.mark.parametrize(
    "path, expected",
    [
        ("cwd", "eed_basic_utils"),
        ("cwd_subfolder", "eed_basic_utils"),
        ("home_dir", None),
    ],
    ids=[
        "cwd = git root",
        "subfolder",
        "non_git_path",
    ],
)
def test_get_git_root(cfg_test, path, expected):
    """Test the get_git_root function."""
    if path == "cwd":
        path = cfg_test["cwd"]
    elif path == "cwd_subfolder":
        path = cfg_test["cwd_subfolder"]
    elif path == "home_dir":
        path = cfg_test["home_dir"]

    git_root = get_git_root(path)
    if git_root is None:
        assert expected is git_root
    else:
        assert git_root.name == expected
        assert (git_root / ".git").exists()
        assert git_root.is_dir()
