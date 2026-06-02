"""Week 1 Homework: Evidence Desk Patterns.

Complete each function using the data structure pattern named in the docstring.

Rules:
- Python 3.11+
- Standard library only
- Do not change function names or parameters
- Run tests with: pytest -q
"""

from collections import deque


# -----------------------------------------------------------------------------
# Required Problem 1
# -----------------------------------------------------------------------------

def count_evidence(evidence: list[str]) -> dict[str, int]:
    """Return a dictionary counting how many times each evidence label appears."""
    counts = {}

    for item in evidence:
        counts[item] = counts.get(item, 0) + 1

    return counts


# -----------------------------------------------------------------------------
# Required Problem 2
# -----------------------------------------------------------------------------

def first_repeated_id(ids: list[str]) -> str | None:
    """Return the first suspect ID that appears a second time."""
    seen = set()

    for suspect_id in ids:
        if suspect_id in seen:
            return suspect_id
        seen.add(suspect_id)

    return None


# -----------------------------------------------------------------------------
# Required Problem 3
# -----------------------------------------------------------------------------

def valid_tags(tags: str) -> bool:
    """Return True if all bracket-style evidence tags are balanced."""
    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    openings = {"(", "[", "{"}

    for char in tags:
        if char in openings:
            stack.append(char)

        elif char in pairs:
            if not stack:
                return False

            top = stack.pop()

            if top != pairs[char]:
                return False

    return len(stack) == 0


# -----------------------------------------------------------------------------
# Required Problem 4
# -----------------------------------------------------------------------------

def lookup_alias(aliases: dict[str, str], alias: str) -> str | None:
    """Return the real name connected to an alias."""
    return aliases.get(alias)


# -----------------------------------------------------------------------------
# Optional Challenge 1
# -----------------------------------------------------------------------------

def process_reports(reports: list[str]) -> list[str]:
    """Return case reports in first-in, first-out processing order."""
    queue = deque(reports)
    processed = []

    while queue:
        processed.append(queue.popleft())

    return processed


# -----------------------------------------------------------------------------
# Optional Challenge 2
# -----------------------------------------------------------------------------

def largest_time_gap(times: list[int]) -> int:
    """Return the largest gap between neighboring event times after sorting."""
    if len(times) < 2:
        return 0

    sorted_times = sorted(times)

    largest_gap = 0

    for i in range(len(sorted_times) - 1):
        gap = sorted_times[i + 1] - sorted_times[i]

        if gap > largest_gap:
            largest_gap = gap

    return largest_gap
