# Find X in a Sorted Array

**Problem:** Given a sorted array and a target value `x`, find the index of the target. If the target is not present, return `-1`.

## Approach: Linear Search

I used a simple linear search approach to find the target element.

### Step 1: Traverse the array

```python
for i in range(len(nums)):
```

I iterate through the array using the index of each element.

### Step 2: Compare with the target

```python
if nums[i] == target:
    return i
```

If the current element matches the target, I return its index.

### Step 3: Handle the missing target

```python
return -1
```

If the loop finishes without finding the target, I return `-1`.

### Example

**Input:**
```python
nums = [1, 3, 5, 7, 9]
target = 5
```

The target `5` is found at index `2`.

**Output:**
```python
2
```

### Complexity Analysis

- **Time Complexity:** O(n) – In the worst case, every element is checked.
- **Auxiliary Space Complexity:** O(1) – No additional data structure is used.

### Key Learnings
- Traversing arrays using indices.
- Comparing array elements with a target.
- Returning the index when an element is found.
- Returning `-1` when the target does not exist.
- Understanding linear search.

### Optimization to Explore

Since the input array is sorted, this problem can also be solved using Binary Search.

Binary Search repeatedly divides the search range in half and achieves O(log n) time complexity.
