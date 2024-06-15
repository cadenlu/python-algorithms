# `collections.Counter` Operations

## Arithmetic Operations

### Addition (`+`)
- **Description**: Combines counts from two counters. If an element appears in both counters, their counts are added.
- **Example**:
    ```python
    from collections import Counter
    c1 = Counter(a=3, b=1)
    c2 = Counter(a=1, b=2, c=2)
    result = c1 + c2
    print(result)  # Output: Counter({'a': 4, 'b': 3, 'c': 2})
    ```

### Subtraction (`-`)
- **Description**: Subtracts counts, but only keeps positive counts. If an element's count becomes zero or negative, it is removed.
- **Example**:
    ```python
    from collections import Counter
    c1 = Counter(a=3, b=1)
    c2 = Counter(a=1, b=2, c=2)
    result = c1 - c2
    print(result)  # Output: Counter({'a': 2})
    ```

### Intersection (`&`)
- **Description**: Keeps the minimum of counts for each element found in both counters.
- **Example**:
    ```python
    from collections import Counter
    c1 = Counter(a=3, b=1)
    c2 = Counter(a=1, b=2, c=2)
    result = c1 & c2
    print(result)  # Output: Counter({'a': 1, 'b': 1})
    ```

### Union (`|`)
- **Description**: Keeps the maximum of counts for each element found in either counter.
- **Example**:
    ```python
    from collections import Counter
    c1 = Counter(a=3, b=1)
    c2 = Counter(a=1, b=2, c=2)
    result = c1 | c2
    print(result)  # Output: Counter({'a': 3, 'b': 2, 'c': 2})
    ```

## Logical Operations

### Equality (`==`)
- **Description**: Checks if two counters have the same counts for all elements.
- **Example**:
    ```python
    from collections import Counter
    c1 = Counter(a=3, b=1)
    c2 = Counter(a=3, b=1)
    print(c1 == c2)  # Output: True
    ```

### Inequality (`!=`)
- **Description**: Checks if two counters do not have the same counts for all elements.
- **Example**:
    ```python
    from collections import Counter
    c1 = Counter(a=3, b=1)
    c2 = Counter(a=1, b=2)
    print(c1 != c2)  # Output: True
    ```
