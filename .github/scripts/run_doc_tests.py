#!/usr/bin/env python
import argparse
import os
import pathlib
import fnmatch
import shutil


def collect_filenames(book_dir='openmdao_book'):
    """
    Copy build artifacts (html files, images, etc) to the output _build directory.

    Parameters
    ----------
    book_dir : str
        The directory containing the Jupyter-Book to be created.

    Returns
    -------

    """
    PATTERNS_TO_TEST = ('*.ipynb', '*.md')
    EXCLUDE_DIRS = ('_build', '.ipynb_checkpoints')

    files_to_test = []
    for dirpath, dirs, files in os.walk(book_dir, topdown=True):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        found_files = set()
        for pattern in PATTERNS_TO_TEST:
            found_files |= set(fnmatch.filter(files, pattern))
        for f in found_files:
            files_to_test.append(str(pathlib.PurePath(dirpath, f)))
    return sorted(files_to_test)


# def test_notebooks(files_to_test):
#     for file in files_to_test:
#         os.system("jupytext --check 'testflo -n 1 --pre_announce {} '" + f"{file}")


if __name__ == '__main__':
    this_file = pathlib.PurePath(__file__)
    repo_root = this_file.parent.parent.parent
    book_dir = pathlib.PurePath(repo_root, 'openmdao_book')
    files_to_test = collect_filenames(book_dir)
    print('\n'.join(files_to_test))
