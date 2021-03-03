import unittest
import os.path
import json

exclude = [
    'tests',
    'test',
    '_build',
    '.ipynb_checkpoints'
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
        new_failures = []
        failures = {}

        for file in _get_files():
            with open(file) as f:
                json_data = json.load(f)
                for i in json_data['cells']:
                    if 'execution_count' in i and i['execution_count'] is not None:
                        new_failures.append("Output found in {0}.".format(file))
                        break

        for i, failure in enumerate(new_failures):
            failures[i] = failure

        if failures:
            msg = '\n'
            count = 0
            for key in failures:
                count += 1
                msg += '    {0}\n'.format(failures[key])
            msg += 'Found {0} issues in docstrings'.format(count)
            self.fail(msg)
            self.fail("Clear output with 'upyter nbconvert  --clear-output --inplace "
                      "path_to_notebook.ipynb'")

    def test_header(self):
        """
        Check Jupyter Notebooks for code cell installing openmdao.
        """

        new_failures = []
        failures = {}
        skip_notebooks = ['notebooks.ipynb']
        header = ["try:",
                  "import openmdao.api as om",
                  "except ImportError:",
                  "python -m pip install openmdao[notebooks]"]

        for file in _get_files():
            header_found = False
            print(file)

            with open(file) as f:
                if not any(x in file for x in skip_notebooks):
                    json_data = json.load(f)
                    for i in json_data['cells']:
                        if 'source' in i and i['source'] is not None:
                            i['source'] = [line.strip() for line in i['source']]
                            if i['source'] == header:
                                header_found = True

                    if not header_found:
                        new_failures.append("Pip install header not found in {0}".format(file))

        for i, failure in enumerate(new_failures):
            failures[i] = failure

        if failures:
            msg = '\n'
            count = 0
            for key in failures:
                count += 1
                msg += '    {0}\n'.format(failures[key])
            msg += 'Found {0} issues in docstrings'.format(count)
            self.fail(msg)
            self.fail("Clear output with 'upyter nbconvert  --clear-output --inplace "
                      "path_to_notebook.ipynb'")

if __name__ == '__main__':
    unittest.main()
