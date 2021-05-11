:orphan:

# Working with Derivatives

## Using Finite Difference or Complex Step

- [Approximating Partial Derivatives](approximating_partial_derivatives.ipynb)
- [Approximating Semi-Total Derivatives](approximating_totals.ipynb)
- [Speeding up Derivative Approximations with Parallel Finite Difference and Parallel Complex Step](parallel_fd.ipynb)

## Providing Analytic Partial Derivatives
- [Declaring Partial Derivatives](specifying_partials.ipynb)
- [Sparse Partial Derivatives](sparse_partials.ipynb)

## Verifying Partial Derivatives are Correct
- [Checking Partial Derivatives with Finite Difference](basic_check_partials.ipynb)
- [Changing Check Settings for FD or CS](check_partials_settings.ipynb)
- [Sparse Partial Derivatives](sparse_partials.ipynb)
- [Checking Partial Derivatives on a Subset of a Model](check_partials_subset.ipynb)
- [Visually Checking Partial Derivatives with Matrix Diagrams](partial_derivative_viz.ipynb)
- [Unit Testing Partial Derivatives](unit_testing_partials.ipynb)

## Computing Total Derivatives Across a Model
- [Picking Forward or Reverse Total Derivative Solve](picking_mode.ipynb)
- [Computing Total Derivatives](compute_totals.ipynb)
- [Checking Total Derivatives](check_total_derivatives.ipynb)
- [Matrix Free Total Derivatives](total_compute_jacvec_product.ipynb)

## Reducing the Cost of Total Derivative Solves Using Advanced Features

There are a number of special cases where a model has a particular structure that can be exploited to
reduce the cost of linear solves used to compute total derivatives. You can learn details of how to determine if
your problem has the necessary structure to use one of these features, or how to restructure your problem to
make use of them in the :ref:`Theory Manual entry on how OpenMDAO computes total derivatives<total_derivs_theory>`

- [In-Memory Assembly of Jacobians](assembled_jacobian.ipynb)
- [Simultaneous Total Derivative Coloring For Separable Problems](simul_derivs.ipynb)
- [Parallel Coloring for Multipoint or Fan-Out Problems](parallel_derivs.ipynb)
- [Vectorizing Linear Solves for Feed-Forward Models](vectorized_derivs.ipynb)
- [Restarting Linear Solutions for Expensive Linear Solves](linear_restart.ipynb)

```python

```
