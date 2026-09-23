![Python](https://img.shields.io/badge/Python-3.13-blue)

# Gradebook Memory

## Description

Homework №6 - In-memory group log

## Features

- Student search
- Average score calculation
- Max average
- Group filtering

## Data Structures

- `list` — stores scores and keeps duplicates. Replacing it with `set` removes duplicate scores.
- `tuple` — stores a fixed student ID `(group, number)`. Replacing it with `set` loses the fixed order.
- `set` — stores unique groups. Replacing it with `list` may create duplicate groups.
- `dict` — connects an ID with student data. Replacing it with a simple list loses direct ID-to-student mapping.



## Output 
``` text
___Average scores___

Andrew's average score:  77.75
Mary's average score:  64.25
Peter's average score:  68.25
Robert's average score:  93.5
John has no scores
Mary's average score:  86.25

Best result: Robert - 93.5

___List copy___

([0, 0, 0, 0], [76, 65, 80, 90])
([0, 0, 0, 0], [60, 56, 66, 75])
([0, 0, 0, 0], [76, 65, 76, 56])
([0, 0, 0, 0], [95, 92, 96, 91])
([0, 0, 0, 0], [])
([0, 0, 0, 0], [90, 89, 90, 76])

___Student groups___

Groups: ['CS-55', 'CS-56', 'MR-23']
Enter Group: 
```

## Run

```bash
python main.py