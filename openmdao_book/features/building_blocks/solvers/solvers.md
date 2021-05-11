:orphan:

# Solvers

## Nonlinear Solvers

- [NonlinearBlockGS](nonlinear_block_gs.ipynb)
- [NonlinearBlockJac](nonlinear_block_jac.ipynb)
- [NonlinearRunOnce](nonlinear_runonce.ipynb)
- [NewtonSolver](newton.ipynb)
- [BroydenSolver](broyden.ipynb)

(linear-solvers)=
## Linear Solvers

- [LinearBlockGS](linear_block_gs.ipynb)
- [LinearBlockJac](linear_block_jac.ipynb)
- [LinearRunOnce](linear_runonce.ipynb)
- [DirectSolver](direct_solver.ipynb)
- [PETScKrylov](petsc_krylov.ipynb)
- [ScipyKrylov](scipy_iter_solver.ipynb)
- [LinearUserDefined](linear_user_defined.ipynb)

(linesearch-section)=
## Linesearch/Backtracking

Backtracking line searches are subsolvers that can be specified in the `line_search` attribute of a NewtonSolver, and are used to pull back to a reasonable point when a Newton step goes too far. This can occur when a step causes output variables to exceed their specified lower and upper bounds. It can also happen in more complicated problems where a full Newton step happens to take you well past the nonlinear solution, even to an area where the residual norm is worse than the initial point. Specifying a value for line_search can help alleviate these problems and improve robustness of your Newton solve.
There are two different backtracking line-search algorithms in OpenMDAO:

- [ArmijoGoldsteinLS](armijo_goldstein.ipynb)
- [BoundsEnforceLS](bounds_enforce.ipynb)
