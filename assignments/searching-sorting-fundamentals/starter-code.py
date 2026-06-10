#!/usr/bin/env python3
"""Starter code for Searching & Sorting Fundamentals assignment.

Provides implementations of linear search, binary search (on sorted lists),
and insertion sort. Each algorithm returns operation counts to help compare
performance on small inputs.
"""

from typing import List, Tuple
import random
import sys


def linear_search(lst: List[int], target: int) -> Tuple[int, int]:
    """Return (index or -1, comparisons).
    comparisons: number of element comparisons performed.
    """
    comps = 0
    for i, v in enumerate(lst):
        comps += 1
        if v == target:
            return i, comps
    return -1, comps


def binary_search(lst: List[int], target: int) -> Tuple[int, int]:
    """Assumes `lst` is sorted. Returns (index or -1, comparisons).
    comparisons: number of value-to-target comparisons performed.
    """
    lo = 0
    hi = len(lst) - 1
    comps = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        comps += 1
        if lst[mid] == target:
            return mid, comps
        elif lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, comps


def insertion_sort(lst: List[int]) -> Tuple[List[int], int, int]:
    """Sorts a copy of lst using insertion sort.

    Returns (sorted_list, comparisons, writes)
    - comparisons: number of times elements were compared
    - writes: approximate number of element writes/swaps
    """
    a = lst.copy()
    comps = 0
    writes = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        # Compare key with sorted portion
        while j >= 0:
            comps += 1
            if a[j] > key:
                a[j + 1] = a[j]
                writes += 1
                j -= 1
            else:
                break
        a[j + 1] = key
        writes += 1
    return a, comps, writes


def demo():
    examples = [
        [1, 3, 5, 7, 9, 11],
        [5, 2, 9, 1, 5, 6],
        list(range(10)),
        list(range(9, -1, -1)),
    ]

    for idx, lst in enumerate(examples, 1):
        print(f"Example {idx}: {lst}")

        # Pick a target that exists and one that doesn't
        target_present = lst[len(lst) // 2]
        target_absent = max(lst) + 100 if lst else 1

        li_idx, li_comps = linear_search(lst, target_present)
        print(f"  Linear search (present): index={li_idx}, comps={li_comps}")

        bi_idx, bi_comps = binary_search(sorted(lst), target_present)
        print(f"  Binary search (present, on sorted list): index={bi_idx}, comps={bi_comps}")

        _, li_comps2 = linear_search(lst, target_absent)
        _, bi_comps2 = binary_search(sorted(lst), target_absent)
        print(f"  Linear search (absent): comps={li_comps2}")
        print(f"  Binary search (absent, on sorted list): comps={bi_comps2}")

        sorted_lst, comps, writes = insertion_sort(lst)
        print(f"  Insertion sort: sorted={sorted_lst}, comparisons={comps}, writes={writes}")
        print()


def random_experiment(n=100, trials=5):
    print(f"Random experiments: n={n}, trials={trials}")
    for t in range(trials):
        lst = [random.randint(0, n) for _ in range(n)]
        target = random.choice(lst)

        _, li_comps = linear_search(lst, target)
        _, bi_comps = binary_search(sorted(lst), target)
        _, ins_comps, ins_writes = insertion_sort(lst[:50])
        print(f"  trial {t+1}: linear={li_comps}, binary={bi_comps}, insertion_small=comps={ins_comps},writes={ins_writes}")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--random":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 100
        trials = int(sys.argv[3]) if len(sys.argv) > 3 else 5
        random_experiment(n, trials)
    else:
        demo()


if __name__ == "__main__":
    main()
