import json

def reset_notebook(fname):
    """
    Empties out the output fields and resets the execution_count in all cells in the given notebook.

    The specified notebook is overwritten.

    Parameters
    ----------
    fname : str
        Name of the notebook file.
    """

    with open(fname) as f:
        dct = json.load(f)

    for cell in dct['cells']:
        if cell['cell_type'] == 'code':
            cell['execution_count'] = None
            cell['outputs'] = []

    with open(fname, 'w') as f:
        json.dump(dct, f, indent=1)


def reset_notebook_cmd():
    import os, sys
    if not len(sys.argv) == 2:
        print(f"usage: python {os.path.basename(sys.argv[0])} <notebook_file>")
        sys.exit(-1)

    fname = sys.argv[1]
    if os.path.splitext(fname)[-1] != '.ipynb':
        fname += '.ipynb'

    if not os.path.isfile(fname):
        print(f"Can't find file '{fname}'.")
        sys.exit(-1)

    reset_notebook(fname)


# TODO: once OpenMDAO_Book is a python package, register a console script to call reset_notebook

if __name__ == '__main__':
    reset_notebook_cmd()

