import unittest
import os.path
import pathlib
import json

exclude = [
    'tests',
    'test',
    '_build',
    '.ipynb_checkpoints',
    '_srcdocs'
]

directories = []

top = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

for root, dirs, files in os.walk(top, topdown=True):
    # do not bother looking further down in excluded dirs
    dirs[:] = [d for d in dirs if d not in exclude]
    for di in dirs:
            directories.append(os.path.join(root, di))

def _get_files():

    for dir_name in directories:
        dirpath = os.path.join(top, dir_name)

        # Loop over files
        for file_name in os.listdir(dirpath):
            if not file_name.startswith('_') and file_name[-6:] == '.ipynb':
                yield dirpath + "/" + file_name

class LintJupyterOutputsTestCase(unittest.TestCase):
    """
    Check Jupyter Notebooks for outputs through execution count and recommend to remove output.
    """

    def test_output(self):
        this_file = pathlib.PurePath(__file__)
        book_dir = this_file.parent.parent

        for file in _get_files():
            print(file)
            with self.subTest(file):
                with open(file) as f:
                    json_data = json.load(f)
                    for i in json_data['cells']:
                        if 'execution_count' in i and i['execution_count'] is not None:
                            msg = "Clear output with 'jupyter nbconvert  --clear-output " \
                                  f"--inplace path_to_notebook.ipynb'"
                            self.fail(f"Output found in {file}.\n{msg}")

    def test_header(self):
        """
        Check Jupyter Notebooks for code cell installing openmdao.
        """
        skip_notebooks = ['notebooks.ipynb']
        header = ["try:",
                  "import openmdao.api as om",
                  "except ImportError:",
                  "!python -m pip install openmdao[notebooks]",
                  "import openmdao.api as om"]

        for file in _get_files():
            with self.subTest(file):

                with open(file) as f:
                    if not any(x in file for x in skip_notebooks):
                        json_data = json.load(f)
                        for i in json_data['cells']:
                            if 'source' in i and i['source'] is not None:
                                i['source'] = [line.strip() for line in i['source']]
                                if i['source'] == header:
                                    break
                        else:
                            header_text = ''.join(header)
                            msg = f'required header not found in notebook {file}\n' \
                                  f'All notebooks should contain the following block before ' \
                                  f'any other code blocks:\n' \
                                  f'-----------------------------------------\n' \
                                  f'{header_text}\n' \
                                  f'-----------------------------------------\n'
                            self.fail(msg)


if __name__ == '__main__':
    unittest.main()
