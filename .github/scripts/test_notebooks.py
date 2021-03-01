#!/usr/bin/env python
# coding: utf-8
import os
import argparse
import glob
import traceback
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors.execute import CellExecutionError

import pathlib
import fnmatch
import json
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

# Parse args
parser = argparse.ArgumentParser(description="Runs a set of Jupyter \
                                              notebooks.")
file_text = """ Notebook file(s) to be run, e.g. '*.ipynb' (default),
'my_nb1.ipynb', 'my_nb1.ipynb my_nb2.ipynb', 'my_dir/*.ipynb'
"""
parser.add_argument('file_list', metavar='F', type=str, nargs='*',
    help=file_text)
parser.add_argument('-t', '--timeout', help='Length of time (in secs) a cell \
    can run before raising TimeoutError (default 600).', default=600,
    required=False)
parser.add_argument('-p', '--run-path', help='The path the notebook will be \
    run from (default pwd).', default='.', required=False)
args = parser.parse_args()
# print('Args:', args)
# if not args.file_list: # Default file_list
#     args.file_list = glob.glob('*.ipynb')
# # Check list of notebooks
# notebooks = []
# print('Notebooks to run:')
# for f in args.file_list:
#     # Find notebooks but not notebooks previously output from this script
#     if f.endswith('.ipynb') and not f.endswith('_out.ipynb'):
#         print(f[:-6])
#         notebooks.append(f[:-6]) # Want the filename without '.ipynb'
# # Execute notebooks and output
# num_notebooks = len(notebooks)
# print('*****')


def test_notebooks(notebooks):

    num_notebooks = len(notebooks)
    failed = []
    passed = []

    for i, n in enumerate(notebooks):
        n_out = n + '_out'
        with open(n) as f:
            try:
                nb = nbformat.read(f, as_version=4)
            except json.decoder.JSONDecodeError:
                print('wtf 1')
                print(n)
                continue
            except nbformat.reader.NotJSONError:
                print('wtf 2')
                print(n)
                continue
            ep = ExecutePreprocessor(timeout=int(args.timeout), kernel_name='python3')
            try:
                print('Running', n, ':', i + 1, '/', num_notebooks)
                out = ep.preprocess(nb, {'metadata': {'path': args.run_path}})
                passed.append(n)
            except CellExecutionError as e:
                print(e.traceback)
                out = None
                msg = f'Error executing the notebook {n}.\n'
                msg += 'See notebook "{n_out}" for the traceback.'
                # print(msg)
                failed.append((n, 'exception'))
            except TimeoutError:
                msg = f'Timeout executing the notebook {n}.\n'
                print(msg)
                failed.append((n, 'timeout'))
            finally:
                # Write output file
                pass
                # with open(n_out + '.ipynb', mode='wt') as f:
                #     nbformat.write(nb, f)

    if failed:
        s = f'Failed [{len(failed)}/{num_notebooks}]'
        print('\n')
        print(s)
        print('-'*len(s))
        print()

        lbl_cause = 'Cause'
        lbl_file = 'Notebook'
        print(f'{lbl_cause:9}    {lbl_file:100}')
        print(f'{9*"-"}    {100*"-"}')

        for nb, err in failed:
            print(f'{err:9}    {nb}')

    s = f'Passed [{len(passed)}/{num_notebooks}]'
    print('\n')
    print(s)
    print('-' * len(s))
    print()



if __name__ == '__main__':
    this_file = pathlib.PurePath(__file__)
    repo_root = this_file.parent.parent.parent
    book_dir = pathlib.PurePath(repo_root, 'openmdao_book')
    files_to_test = collect_filenames(book_dir)
    test_notebooks(files_to_test)
