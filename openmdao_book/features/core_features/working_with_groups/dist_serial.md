# Connections involving distributed variables

The purpose of this section is to describe the behavior you should expect when connecting two variables together when at least one of them is a distributed variable.

## Distributed output to serial input
Because distributed variables may have different sizes and/or values on different ranks, and serial variables must have the same value and size on all ranks, the only way that a distributed to serial connection is allowed is if `src_indices` are specified for the serial input and that the specified `src_indices` are identical on all ranks where the input variable exists.  Otherwise the serial inputs could have different values on different ranks, which is illegal. Note that in previous versions of OpenMDAO the behavior when connecting a distributed output to a serial input when `src_indices` were not specified was that the serial input on each rank will be the same size as the full distributed output.  This is no longer the case.  In fact, this case is no longer allowed.  However, you can still achieve the same behavior by specifying `src_indices` of `om.slicer[:]` on the input, which explicitly specifies that the input on each rank is the same size as the full distributed output.  For example:

```python
group.connect('mydistcomp.out', 'myserial.in', src_indices=om.slicer[:])
```

## Distributed output to distributed input
When connecting two distributed variables, you can specify `src_indices` on the input however you choose, or OpenMDAO will automatically assign `src_indices` to the input based on the size of the input in each rank.  For example, if the component that owns the input is running on 3 ranks with input sizes of [2, 3, 4], then `src_indices` of [0, 1], [2, 3, 4], and [5, 6, 7, 8] will be specified on the 3 ranks.  If, however, the global size of the output does not equal the global size of the input, an exception will be raised saying that OpenMDAO is not able to determine the `src_indices`.

## Serial output to distributed input
These types of connections are deprecated and will become errors in a future release, but for now, you are allowed to connect a serial output to a distributed input, provided that the global sizes of input and output are equal and the inputs are the same size on every rank.

