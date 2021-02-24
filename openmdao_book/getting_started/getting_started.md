---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.8.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Getting Started (Markdown)
Installation Instructions:

From your python environment (we recommend [Anaconda](https://www.anaconda.com/distribution)), just type:

``` bash
pip install 'openmdao[all]'
```

```{note}

The [all] suffix to the install command ensures that you get all the optional dependencies
(e.g. for testing and visualization).  You can omit this for a minimal installation.

The quotation marks are required to prevent some command shells (e.g. zsh) from trying to interpret
the square brackets.
```

Alternatively, in a notebook environment such as [Google Colab](https://colab.research.google.com),
you can install OpenMDAO by running the above as a shell command (precede it with !).

You'll see the following  import statement throughout this documentation.
This simply installs OpenMDAO in a Jupyter notebook if it is not already available.

```{code-block} python3
try:
    import openmdao.api as om
except:
    !pip install openmdao
```

```{admonition} **The examples in this documentation are interactive!**

Use the rocket icon above to launch examples throughout this documentation in Binder or Google Colab
```

## Sample Optimization File

With OpenMDAO installed, let's try out a simple example, to get you started running your first optimization.
Copy the following code into a file named paraboloid_min.py:

```{code-cell} python3
:tags: [hide-output]
import openmdao.api as om

# build the model
prob = om.Problem()

prob.model.add_subsystem('paraboloid', om.ExecComp('f = (x-3)**2 + x*y + (y+4)**2 - 3'))

# setup the optimization
prob.driver = om.ScipyOptimizeDriver()
prob.driver.options['optimizer'] = 'SLSQP'

prob.model.add_design_var('paraboloid.x', lower=-50, upper=50)
prob.model.add_design_var('paraboloid.y', lower=-50, upper=50)
prob.model.add_objective('paraboloid.f')

prob.setup()

# Set initial values.
prob.set_val('paraboloid.x', 3.0)
prob.set_val('paraboloid.y', -4.0)

# run the optimization
prob.run_driver()
```

Then, to run the file, simply type:

``` bash
>> python paraboloid_min.py
```

If all works as planned, results should appear as such:

```{code-cell} python3
:tags: [hide-input, hide-output]

# This block of code tests that the documented code functions as
# expected and is hidden by default.

from openmdao.utils.assert_utils import assert_near_equal

# minimum value
assert_near_equal(prob.get_val('paraboloid.f'), -27.33333, 1e-6)

# location of the minimum
assert_near_equal(prob.get_val('paraboloid.x'), 6.6667, 1e-4)
assert_near_equal(prob.get_val('paraboloid.y'), -7.33333, 1e-4)
```
