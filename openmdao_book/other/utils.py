import json

def reset_notebook(fname):
    """
    Empties the output fields and resets execution_count in all code cells in the given notebook.

    Also removes any empty code cells. The specified notebook is overwritten.

    Parameters
    ----------
    fname : str
        Name of the notebook file.
    """

    with open(fname) as f:
        dct = json.load(f)

    newcells = []
    for cell in dct['cells']:
        if cell['cell_type'] == 'code':
            if cell['source']:  # cell is not empty
                cell['execution_count'] = None
                cell['outputs'] = []
                newcells.append(cell)
        else:
            newcells.append(cell)

    dct['cells'] = newcells

    with open(fname, 'w') as f:
        json.dump(dct, f, indent=1)


def reset_notebook_cmd():
    """
    Run reset_notebook on any notebook files passed in via the command line.
    """
    import os, sys
    if len(sys.argv) < 2:
        print(f"usage: python {os.path.basename(sys.argv[0])} <notebook_file(s)>")
        sys.exit(-1)

    for fname in sys.argv[1:]:
        if os.path.splitext(fname)[-1] != '.ipynb':
            fname += '.ipynb'

        if not os.path.isfile(fname):
            print(f"Can't find file '{fname}'.")
            sys.exit(-1)

        reset_notebook(fname)


# TODO: once OpenMDAO_Book is a python package, register a console script to call reset_notebook

if __name__ == '__main__':
    reset_notebook_cmd()

