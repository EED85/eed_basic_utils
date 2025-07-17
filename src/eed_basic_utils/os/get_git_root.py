from pathlib import Path
from typing import Optional


def get_git_root(path: Optional[Path] = None) -> Path | None:
    """
    Returns the root directory of the git repository containing the given path.

    Parameters
    ----------
    path : Optional[Path], optional
        The starting path to search for the git root. If None, uses the current working directory.

    Returns
    -------
    Path or None
        The root directory of the git repository, or None if not found.

    Notes
    -----
    Searches upwards from the given path until a directory containing a `.git` folder is found.
    """
    if path is None:
        path = Path.cwd()

    if (path / ".git").exists():
        return path

    git_root = next(iter(path.parents))
    while not (git_root / ".git").exists() and git_root != git_root.parent:
        git_root = git_root.parent
    if not (git_root / ".git").exists():
        return None
    else:
        return git_root
