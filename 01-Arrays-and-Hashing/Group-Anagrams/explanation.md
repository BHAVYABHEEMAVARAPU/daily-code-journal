# Group Anagrams

**Difficulty:** Medium  
**Topic:** Arrays & Hashing  
**Approach:** Sorting + Hash Map

## Problem Statement

Given an array of strings, group the anagrams together. The order of the groups does not matter.

Anagrams are words that contain the same characters with the same frequency but may have different arrangements.

## Approach

I used a dictionary to group words that have the same characters.

1. Initialize an empty dictionary called `anagrams`.
2. Iterate through each word in the input list.
3. Sort the characters of each word using `sorted(word)`.
4. Convert the sorted character list into a string using `''.join()`.
5. Use this sorted string as the dictionary key.
6. Check whether the key already exists in the dictionary.
   - If it does not exist, create an empty list for that key.
   - If it exists, use the existing list.
7. Append the original word to the corresponding list.
8. Return all dictionary values as a list using `list(anagrams.values())`.

## Code Explanation

### 1. Initialize the dictionary

```python
anagrams = {}
```

Stores the groups of anagrams. Each key represents a unique sorted character combination.

### 2. Generate the key

```python
key = ''.join(sorted(word))
```

- `sorted(word)` arranges the characters alphabetically.
- `''.join()` combines the sorted characters into a string.
- Anagrams generate the same key.

Example:

| Word | Sorted key |
|---|---|
| hat | aht |
| act | act |
| cat | act |
| stop | opst |
| pots | opst |
| tops | opst |

### 3. Create a group if the key is new

```python
if key not in anagrams:
    anagrams[key] = []
```

Creates an empty list only when a particular sorted key is encountered for the first time.

### 4. Add the original word

```python
anagrams[key].append(word)
```

Adds the original word to its corresponding anagram group.

### 5. Return the final groups

```python
return list(anagrams.values())
```

Extracts all the dictionary values and returns them as a nested list.

## Dry Run

**Input:**

```python
strs = ["hat", "act", "cat", "stop", "pots", "tops"]
```

| Word | Sorted key | Dictionary action |
|---|---|---|
| hat | aht | Create new group |
| act | act | Create new group |
| cat | act | Append to existing group |
| stop | opst | Create new group |
| pots | opst | Append to existing group |
| tops | opst | Append to existing group |

**Final dictionary:**

```python
{
    "aht": ["hat"],
    "act": ["act", "cat"],
    "opst": ["stop", "pots", "tops"]
}
```

**Output:**

```python
[
    ["hat"],
    ["act", "cat"],
    ["stop", "pots", "tops"]
]
```

## Complexity Analysis

Let:
- `n` = number of words.
- `k` = maximum length of a word.

**Time Complexity: O(n × k log k)**

- We iterate through all `n` words.
- Sorting each word takes O(k log k).
- Dictionary insertion and lookup take O(k) for creating and handling string keys in the general analysis, which is dominated by sorting for nontrivial k.

**Space Complexity: O(n × k)**

The dictionary stores all the original words and their grouping information. The sorted keys also require additional space.

## Key Learnings

- Using dictionaries to group related elements.
- Understanding how `sorted()` and `join()` work together.
- Using a common key to identify anagrams.
- Creating nested lists dynamically.
- Using `dict.values()` to retrieve grouped results.

## Possible Optimization

A frequency-counting approach can be used instead of sorting each word. This can reduce the time complexity to O(n × k) when the character set is fixed and bounded.
