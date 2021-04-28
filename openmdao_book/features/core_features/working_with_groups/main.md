# Working with Groups
---
It’s often desirable to represent a complex model as a collection of components. Using Group objects, we can group components, as well as other Groups, together to form a tree structure. The following sections explain how to create that tree structure, how to access subsystems and variables within the tree, and how to connect those variables. They will also explain how to promote a variable from a subsystem up to its parent Group.

- [Adding Subsystems to a Group and Promoting Variables](add_subsystem.ipynb)
- [Connecting Variables](connect.ipynb)
- [Using src_indices with Promoted Variables](src_indices.ipynb)
- [Connections Involving Distributed Variables](dist_serial.md)
- [Setting the Order of Subsystems in a Group](set_order.ipynb)
- [Accessing Subsystems Within a Group](get_subsystem.ipynb)
- [Parallel Groups](parallel_group.ipynb)
- [Modifying Children of a Group with Configure Method](configure_method.ipynb)
- [Changing Model Settings After Setup](post_setup_config.ipynb)
- [Providing an Initial Guess for Implicit States in a Group](guess_method.ipynb)