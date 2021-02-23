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

# How to Cite OpenMDAO

There is a general OpenMDAO paper that includes a high-level overview of the framework,
including how implicit and explicit components leverage the underlying core APIs to support multidisciplinary modeling.
There is a walk-through example of how some of the key underlying mathematics of the framework are used and how analytic derivatives are computed.
Lastly, there are  examples of how and when to use some of the specialized algorithms for computing derivatives efficiently for different kinds of problems.

We hope the paper helps you understand the framework better, and most importantly,
helps you to solve some really nice MDO problems! If you do make use of OpenMDAO, please cite this paper.

```
    @article{openmdao_2019,
    Author={Justin S. Gray and John T. Hwang and Joaquim R. R. A. Martins and Kenneth T. Moore and Bret A. Naylor},
    Title="{OpenMDAO: An Open-Source Framework for Multidisciplinary Design, Analysis, and Optimization}",
    Journal="{Structural and Multidisciplinary Optimization}",
    Year={2019},
    Volume={59},
    pages={1075-1104},
    issue={4},
    Publisher={Springer},
    pdf={http://mdolab.engin.umich.edu/sites/default/files/OpenMDAO_preprint_0.pdf},
    Doi={10.1007/s00158-019-02211-z},
    }
```

##  With the `openmdao` command

Depending on which parts of OpenMDAO you are using, there are also a few other papers that are appropriate to cite.
OpenMDAO can tell you which citations are appropriate, accounting for what classes you're actually using in your model.

If you copy the following script into a file called `paraboloid.py`,
then you can get the citations from the command line using the :ref:`openmdao command-line script<om-command>`.

```{code-cell}
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
prob.run_driver();
```

```{code-cell}
:tags: [hide-input, hide-output]

# minimum value
assert_near_equal(prob.get_val('paraboloid.f'), -27.33333, 1e-6)

# location of the minimum
assert_near_equal(prob.get_val('paraboloid.x'), 6.6667, 1e-4)
assert_near_equal(prob.get_val('paraboloid.y'), -7.33333, 1e-4)
```
