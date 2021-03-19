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


## Notebook Guidelines

1. Each notebook should include this block at the top to import OpenMDAO if not already available.  This is necessary on the cloude-based notebook environments like colab.

``` python3
try:
    import openmdao.api as om
except ImportError:
    !python -m pip install openmdao[notebooks]
    import openmdao.api as om
```

This cell should be tagged with the following metadata.  The "remove-input" and "remove-output" tags prevent it from showing up in the documentation, and the "hide_input" portion collapses the input cell. When adding the import code from above, add the tag `active-ipynb` to the list. To add a tag, select `View` -> `Cell Toolbar` -> `Tags`.

``` yaml
{
  "hide_input": true,
  "tags": [
    "remove-input",
    "remove-output"
  ],
  "trusted": true
}
```

2. Executed code in notebooks should be tested using the same assertions used in unittests.

For instance, in the paraboloid case we have:

``` python3
# This code block is hidden by default.
# It exists to verify that the above code works correctly.

from openmdao.utils.assert_utils import assert_near_equal

# minimum value
assert_near_equal(prob.get_val('paraboloid.f'), -27.33333, 1e-6);

# location of the minimum
assert_near_equal(prob.get_val('paraboloid.x'), 6.6667, 1e-4);
assert_near_equal(prob.get_val('paraboloid.y'), -7.33333, 1e-4);
```

It's not necessary to show this in the documentaiton, so remove it using the same
hiding metadata above.

3. We will use a git pre commit hook to clean all output cells from the notebooks when committing them.  This will prevent git from picking up on meaningless diffs in the output cells and their metadata.

4. Since 'n2.html' files and other build artifacts need to be manually copied over to the output `_build` directory to make the docs, each example notebook should be kept in its own directory.

### Troubleshooting

- If you get an error `jupyter_client.kernelspec.NoSuchKernel: No such kernel named name-of-your-env`, this means your notebook's kernel is not set to `Python 3`. To fix this, select `Kernel` -> `Change Kernel` -> `Python 3` and then rebuild the docs.
