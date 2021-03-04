#!/usr/bin/env python
# coding: utf-8
import pathlib
import fnmatch
import json
import os
import unittest
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors.execute import CellExecutionError


RUN_PATH = '.'
TIMEOUT = 600
KERNEL = 'python3'


def collect_filenames(book_dir='openmdao_book'):
    """
    Copy build artifacts (html files, images, etc) to the output _build directory.

    Parameters
    ----------
    book_dir : str
        The directory containing the Jupyter-Book to be created.

    Returns
    -------
    list
        The names of the files to be tested.

    """
    PATTERNS_TO_TEST = ('*.ipynb',)
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


class TestNotebooks(unittest.TestCase):

    def test_notebooks(self):
        """ Run each notebook in a subtest to check for errors."""
        this_file = pathlib.PurePath(__file__)
        book_dir = this_file.parent.parent
        notebooks = collect_filenames(book_dir)

        num_notebooks = len(notebooks)

        for i, n in enumerate(notebooks):
            nb_rel_path = pathlib.PurePath(n).relative_to(book_dir)
            print(nb_rel_path)
            with self.subTest(nb_rel_path):
                with open(n) as f:
                    try:
                        nb = nbformat.read(f, as_version=4)
                    except json.read.NotJSONError:
                        msg = f'Notebook is not valid JSON: {nb_rel_path}.\n'
                        self.fail(msg)
                    except json.decoder.JSONDecodeError:
                        msg = f'Unable to parse notebook {nb_rel_path}.\n'
                        self.fail(msg)
                    ep = ExecutePreprocessor(timeout=int(TIMEOUT), kernel_name=KERNEL)
                    try:
                        print('Running', nb_rel_path, ':', i + 1, '/', num_notebooks)
                        ep.preprocess(nb, {'metadata': {'path': RUN_PATH}})
                    except CellExecutionError as e:
                        self.fail(f'{nb_rel_path} failed due to exception.\n{e.traceback}')
                    except TimeoutError:
                        msg = f'Timeout executing the notebook {n}.\n'
                        self.fail(msg)
                    finally:
                        # This is where we could optionally write the notebook to an output file
                        # with open(n_out + '.ipynb', mode='wt') as f:
                        #     nbformat.write(nb, f)
                        pass


if __name__ == '__main__':
    unittest.main()
