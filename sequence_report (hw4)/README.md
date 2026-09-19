# Homework 4 — Sequence report

## Description

This program analyzes a sequence of integers entered by the user.

The program stops when `0` is entered. The number `0` is not included in the statistics.

The program:
- counts positive and negative numbers;
- calculates the total sum and count of numbers;
- finds the minimum and maximum values;
- skips the number `13` using `continue` and counts how many times it was skipped;
- displays `No data` if there are no valid numbers;
- displays the final results in three numbered summary lines using `for` and `range()`.

## `pass` vs `continue`

`pass` does nothing and execution continues normally.

`continue` skips the rest of the current loop iteration and starts the next iteration.

Therefore, `continue` is used to skip the number `13`.

## Test Cases

### Test 1
Input: `5, -2, 13, 7, 0`

Expected:
- Positive: 2
- Negative: 1
- Count: 3
- Total: 10
- 13s: 1
- Minimum: -2
- Maximum: 7

### Result:

1 Positive: 2 | Negative: 1

2 Count: 3 | Total: 10 | 13s: 1

3 Minimum: -2 | Maximum: 7


### Test 2
Input: `0`

Expected: `No data`

Result: No data

### Test 3
Input: `-5, -2, -10, 0`

Expected:
- Positive: 0
- Negative: 3
- Count: 3
- Total: -17
- Minimum: -10
- Maximum: -2

### Result:

1 Positive: 0 | Negative: 3

2 Count: 3 | Total: -17 | 13s: 0

3 Minimum: -10 | Maximum: -2

### Test 4
Input: `13, 13, 13, 0`

Expected: `No data`

### Result: No data

### Test 5
Input: `8, 0`

Expected:
- Positive: 1
- Negative: 0
- Count: 1
- Total: 8
- Minimum: 8
- Maximum: 8

### Result: 

1 Positive: 1 | Negative: 0

2 Count: 1 | Total: 8 | 13s: 0

3 Minimum: 8 | Maximum: 8