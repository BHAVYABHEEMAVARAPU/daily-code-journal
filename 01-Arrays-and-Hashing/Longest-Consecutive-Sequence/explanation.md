# Longest Consecutive Sequence

**Problem:** Given an unsorted array of integers, return the length of the longest consecutive elements sequence.

## Approach: Using a Set

I used a set to store the unique elements of the array. This allows efficient membership checking and helps avoid unnecessary duplicate processing.

### Step 1: Convert the array into a set

```python
l = set(nums)
```

- Removes duplicate elements.
- Allows average O(1) membership checking.

### Step 2: Identify the beginning of a sequence

```python
if num - 1 not in l:
```

A number is considered the beginning of a consecutive sequence if its previous number does not exist in the set.

For example, in `[100, 4, 200, 1, 3, 2]`:

- `1` is a starting number because `0` is absent.
- `100` is a starting number because `99` is absent.
- `200` is a starting number because `199` is absent.

### Step 3: Count consecutive elements

```python
curr_num = num
c = 1

while (curr_num + 1) in l:
    curr_num = curr_num + 1
    c = c + 1
```

Starting from the beginning of a sequence, I repeatedly check whether the next consecutive number exists in the set.

If it exists, I move forward and increase the count.

### Step 4: Update the maximum length

```python
long = max(long, c)
```

After counting a sequence, I compare its length with the previously found maximum.

### Example

**Input:**
```python
nums = [100, 4, 200, 1, 3, 2]
```

The set contains:

`{100, 4, 200, 1, 3, 2}`

The longest consecutive sequence is:

`1 → 2 → 3 → 4`

**Output:**
```python
4
```

## Complexity Analysis

Let `n` be the number of elements in the input array.

- **Time Complexity:** O(n) average. Creating the set takes O(n), and each sequence is explored only from its starting element.
- **Space Complexity:** O(n) for storing the elements in the set.

## Key Learnings

- Using sets to remove duplicate elements.
- Understanding efficient membership checking.
- Identifying the starting point of a consecutive sequence.
- Avoiding repeated traversal by checking whether the previous element exists.
- Using `max()` to maintain the longest sequence found.
- Understanding how to achieve an O(n) average-time solution.
