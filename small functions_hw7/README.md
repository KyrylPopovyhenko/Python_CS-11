# Homework 7

Small Python functions with clear input and output contracts.

## Files

- `calculations.py` — main functions
- `demo.py` — tests and result checking

## Functions

### `mean(*values)`
Returns the average value or `None` if no values are provided.

### `clamp(value, lower=0, upper=100)`
Keeps the value inside the given range.  
Returns `None` if `lower > upper`.

### `weighted_sum(values, weights)`
Returns the weighted sum of two lists.  
Returns `None` if lists are empty or have different lengths.

### `format_record(name, **fields)`
Returns a formatted record with a name and additional fields.

### `factorial(n)`
Calculates factorial recursively.

### `factorial_loop(n)`
Calculates factorial using a loop.

## Run

```bash
python demo.py