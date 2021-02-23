# OpenMDAO Book

This repo contains the prototype for new, more interactive documentation of OpenMDAO
based on [jupyter-book](https://jupyterbook.org/intro.html).

For now I've left in the default Jupyter-book files, which includes some
useful how-to information. OpenMDAO-specific documentation begins with `main.md`.

## Pre-requisites

You will need to pip install `jupyter-book`.
Also, building the notebook seems to require Python 3.8.

## Building

From the repo root

```
jupyter-book build openmdao_book
```

The file `other/citing.md` contains an executable code-cell that is
executed when the notebook is built.  When introducing a new code-cells
to a markdown file, the user is required to use the command

```
jb myst init openmdao_book/other/citing.md 
```

This adds meta-data for the file that should only need to be changed
if additional execution information is added (I think).

Building the actual docs is then done from the repo root using:

```
jb build openmdao_book 
cp openmdao_book/examples/n2.html openmdao_book/_build/html/examples/
```

That last command is what we need to automate, since the n2's will have the same name by default.
