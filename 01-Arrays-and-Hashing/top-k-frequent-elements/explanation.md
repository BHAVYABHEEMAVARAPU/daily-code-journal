# Top K Frequent Elements

**Difficulty:** Medium  
**Topic:** Arrays & Hashing  
**Approach:** Frequency Counting + Sorting

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

## Approach

I used a dictionary to count the frequency of each element and then sorted the dictionary keys based on their frequencies in descending order.

1. Initialize an empty list `l` to store the final result.
2. Initialize an empty dictionary `freq` to store the frequency of each number.
3. Iterate through the input array.
4. Use `freq.get(num, 0) + 1` to count the occurrences of each number.
5. Sort the dictionary keys based on their corresponding frequencies using `sorted()`.
6. Use `reverse=True` to arrange the elements from highest frequency to lowest frequency.
7. Append the sorted elements to the result list.
8. Return the first `k` elements using list slicing.

## Code Explanation

### 1. Initialize variables

```python
l = []
freq = {}
```

- `l` stores the final top K frequent elements.
- `freq` stores each number and its frequency.

### 2. Count the frequency

```python
for num in nums:
    freq[num] = freq.get(num, 0) + 1
```

- `freq.get(num, 0)` retrieves the current frequency of the number.
- If the number does not exist, it returns 0.
- We increment the frequency by 1.

### 3. Sort based on frequency

```python
for num in sorted(freq, key=freq.get, reverse=True):
```

- `sorted(freq)` sorts the dictionary keys.
- `key=freq.get` tells Python to sort the keys based on their corresponding dictionary values.
- `reverse=True` sorts them in descending order.

This places the most frequent elements first.

### 4. Store the sorted elements

```python
l.append(num)
```

Adds each sorted number to the result list.

### 5. Return the first K elements

```python
return l[:k]
```

List slicing extracts only the first `k` elements.

## Dry Run

**Input:**

```python
nums = [1, 2, 2, 3, 3, 3]
k = 2
```

### Step 1: Frequency counting

| Number | Frequency |
|---|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |

Dictionary:

```python
freq = {
    1: 1,
    2: 2,
    3: 3
}
```

### Step 2: Sort by frequency

```python
sorted(freq, key=freq.get, reverse=True)
```

Result:

```python
[3, 2, 1]
```

### Step 3: Select the first K elements

Since `k = 2`:

```python
l[:2]
```

Output:

```python
[3, 2]
```

## Complexity Analysis

Let:
- `n` = total number of elements.
- `m` = number of distinct elements.

**Time Complexity: O(n + m log m)**

- Frequency counting takes O(n).
- Sorting the distinct elements takes O(m log m).
- Building the result takes O(m).

**Space Complexity: O(m)**

The frequency dictionary, sorted keys and result list require space proportional to the number of distinct elements.

## Key Learnings

- Using dictionaries for frequency counting.
- Understanding `dict.get()` with a default value.
- Sorting dictionary keys based on their values.
- Understanding `key=freq.get` and `reverse=True`.
- Using list slicing to retrieve the first K elements.
- Applying frequency counting to solve array problems.

## Possible Optimization

A bucket sort approach can solve this problem in O(n) time by grouping numbers according to their frequencies instead of sorting the dictionary keys.
