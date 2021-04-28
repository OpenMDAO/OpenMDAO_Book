# Features

OpenMDAO’s fully-supported features are documented here, each in a self-contained context. Any feature documented here, with the exception of those in the Experimental Features section, has been thoroughly tested, and should be considered fully functional.


## Core Features
---
- [Working with Components](core_features/working_with_components/main.md)
- [Working with Groups](core_features/working_with_groups/main.md)
- [Working with Derivatives](core_features/working_with_derivatives/main.md)
- [Adding design variables, constraints, and objectives](core_features/adding_desvars_cons_objs/main.md)
- [Running Your Models](core_features/running_your_models/main.md)
- [Controlling Solver Behavior](core_features/controlling_solver_behavior/main.md)

## Building Blocks
---
- [Components](building_blocks/components/components.md)
- [Drivers](building_blocks/drivers/index.md)
- [Solvers](building_blocks/solvers/solvers.md)
- [SurrogateModels](building_blocks/surrogates/index.md)

## Recording Data
---

## Model Visualization
---
- [Basics of Creating N2 Model Visualizations](model_visualization/n2_basics/n2_basics.ipynb)
- [Details of the N2 Model Visualizations](model_visualization/n2_details/n2_details.ipynb)
- [Metamodel Visualization](model_visualization/meta_model_basics.ipynb)
- [View Connections of a Model](model_visualization/view_connections.ipynb)
- [View Driver Scaling Information](model_visualization/view_scaling_report.ipynb)

## Debugging
---
- [Listing Variables](debugging/listing_variables.ipynb)
- [The Newton Solver Isn’t Converging](debugging/newton_solver_not_converging.ipynb)
- [Driver Debug Printing](debugging/debugging_drivers.ipynb)
- [Solver Debug Printing](debugging/debugging_solvers.ipynb)
- [Profiling and Tracing](debugging/profiling/index.ipynb)
- [MPI Detection, Troubleshooting, and Testing](debugging/controlling_mpi.ipynb)

## [Units Definitions](units.ipynb)

## Experimental Features
---
- [Determining Variable Shapes at Runtime](experimental/dyn_shapes.ipynb)
- [Simultaneous Coloring of Approximated Derivatives](experimental/approx_coloring.ipynb)
- [Working with Plugins](experimental/plugins.md)
