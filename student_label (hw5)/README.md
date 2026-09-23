![Python](https://img.shields.io/badge/Python-3.13-blue)

# Student Record Normalization

## Description

Homework №5 — student record normalization and validation.

The program receives a student's full name and group code, normalizes the entered data and checks whether the input format is correct.

Regular expressions are not used.

## Features

- Removes extra spaces from input
- Checks that the full name contains exactly two words
- Capitalizes the name and surname
- Converts the group code to uppercase
- Checks the group code format `AB-12`
- Validates letters, dash and digits separately
- Generates student initials
- Displays a specific error message for invalid input

## String Methods

- `strip()` — removes spaces from the beginning and end of a string
- `split()` — separates the full name into parts and removes extra spaces between words
- `title()` — capitalizes the first letter of each name part
- `upper()` — converts group letters to uppercase
- `isalpha()` — checks whether characters are letters
- `isdigit()` — checks whether characters are digits

## Slices

The group code is checked using slices:

```python
group[:2]
group[3:]
```

For example:

```text
CS-55
```

`group[:2]` returns:

```text
CS
```

`group[3:]` returns:

```text
55
```

The slice `group[3:]` does not need a right boundary because Python automatically reads characters until the end of the string.

## Unicode Letters

`isalpha()` supports Unicode letters.

Because of this, there is no need to manually create a custom alphabet for different languages.

## Example

Input:

```text
Enter your name and surname: john   smith
Enter group (AB-12): cs-55
```

Output:

```text
Smith, John - CS-55 J.S.
```

## Error Examples

```text
Error: incorrect name or surname
Incorrect length | example: >>AB-12<<
There is no dash between | example: AB-12
There are no letters | example: >>AB-12
There are no numbers | example: AB-12<<
```

## Run

```bash
python student_label.py
```