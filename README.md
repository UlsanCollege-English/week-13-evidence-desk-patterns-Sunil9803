# Week 1 Homework: Evidence Desk Patterns

## Student Name

Sunil Khadka

## Summary

This homework focuses on practicing common problem-solving patterns using Python data structures. It includes frequency counting with dictionaries, duplicate detection using sets, stack matching with lists, and lookup tables with dictionaries. The assignment helps build understanding of how different data structures solve different types of problems efficiently. Optional challenges also introduce queue processing with deque and sorting with list operations.

## How to Run Tests

From the repository root, run:

```bash
pytest -q
```

To run one test file:

```bash
pytest -q tests/test_challenges.py
```

## Required Problems

Complete these functions in `src/challenges.py`:

1. `count_evidence`
2. `first_repeated_id`
3. `valid_tags`
4. `lookup_alias`

## Optional Challenges

These are extra practice unless your instructor tells you otherwise:

1. `process_reports`
2. `largest_time_gap`

Optional tests are skipped by default. To run them, remove the `@pytest.mark.skip(...)` line above the optional test you want to check.

---

# Problem Notes

## 1. Evidence Counter

### Pattern

Frequency Counting

### Data Structure

Dictionary

### Approach

- Step 1: Create an empty dictionary.
- Step 2: Loop through each evidence label.
- Step 3: Update the count for each label and return the dictionary.

### Complexity

- Time: `O(n)`
- Space: `O(n)`

Explain briefly:

The function loops through the list once. The dictionary stores counts for unique evidence labels.

### Edge Cases Checked

- [x] Empty list
- [x] One item
- [x] Repeated items
- [x] Different labels

---

## 2. Repeat Suspect ID

### Pattern

Seen Before

### Data Structure

Set

### Approach

- Step 1: Create an empty set called `seen`.
- Step 2: Loop through each ID.
- Step 3: If the ID already exists in the set, return it. Otherwise add it to the set.

### Complexity

- Time: `O(n)`
- Space: `O(n)`

Explain briefly:

Each ID is checked and inserted into a set in constant average time.

### Edge Cases Checked

- [x] Empty list
- [x] No repeated IDs
- [x] First two IDs match
- [x] Multiple repeated IDs

---

## 3. Evidence Tag Validator

### Pattern

Stack Matching

### Data Structure

List used as a Stack

### Approach

- Step 1: Create an empty stack.
- Step 2: Push opening brackets onto the stack.
- Step 3: Match each closing bracket with the most recent opening bracket.

### Complexity

- Time: `O(n)`
- Space: `O(n)`

Explain briefly:

The string is scanned once. The stack stores unmatched opening brackets.

### Edge Cases Checked

- [x] Empty string
- [x] Correctly nested tags
- [x] Mismatched tags
- [x] Closing tag before opening tag
- [x] Unclosed opening tag
- [x] Non-bracket characters

---

## 4. Alias Directory

### Pattern

Lookup Table

### Data Structure

Dictionary

### Approach

- Step 1: Search the dictionary using the alias.
- Step 2: Return the real name if found, otherwise return `None`.

### Complexity

- Time: `O(1)`
- Space: `O(1)`

Explain briefly:

Dictionary lookup is constant time on average and requires no extra storage.

### Edge Cases Checked

- [x] Known alias
- [x] Unknown alias
- [x] Empty dictionary

---

# Assistance & Sources

## AI Used?

- [x] Yes
- [ ] No

## If yes, what did AI help with?

- Understanding data structure patterns.
- Reviewing time and space complexity.
- Formatting the README file.

## Other Sources

- Course lecture notes
- Class examples
- Python documentation