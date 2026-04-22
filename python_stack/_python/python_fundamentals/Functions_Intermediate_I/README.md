# Random Integer Function

## Description

A simple Python function that returns a random integer between two values.
If `min` is greater than `max`, the values are swapped automatically.

## Code

```python
import random

def randInt(min=0, max=100):
    if min > max:
        min, max = max, min 
        
    num = random.random() * (max - min) + min
    return round(num)

print(randInt(min=10, max=-50))
```

## Example Output

```
-23
```

(Note: output changes every time)
