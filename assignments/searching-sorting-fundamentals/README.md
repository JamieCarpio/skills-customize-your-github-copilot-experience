# 📘 Assignment: Searching & Sorting Fundamentals

## 🎯 Objective

Implement basic search and sort algorithms and compare their operation counts to develop intuition about algorithmic performance and complexity.

## 📝 Tasks

### 🛠️	Implement search and sort

#### Description
Write Python implementations for linear search, binary search (on a sorted list), and insertion sort. Instrument the algorithms to count key operations (comparisons and swaps) so students can compare empirical costs on small inputs.

#### Requirements
Completed program should:

- Implement `linear_search(lst, target)` and return both index (or -1) and comparison count
- Implement `binary_search(lst, target)` (assumes `lst` is sorted) and return index and comparison count
- Implement `insertion_sort(lst)` and return the sorted list along with comparison and swap counts
- Provide a simple CLI or demo that runs the algorithms on example lists and prints operation counts for comparison
- Handle invalid inputs gracefully and include brief usage instructions


### 🛠️	Optional: Experiments and Reporting

#### Description
Extend the demo to run experiments varying input size and characteristics (random, sorted, reverse-sorted) and summarize results.

#### Requirements
Completed enhancements may include:

- Run multiple trials and print average operation counts
- Output results as CSV for plotting
- Add a short write-up interpreting the observed costs vs. theoretical expectations

## Running the starter script

From the assignment folder run the demo:

```bash
cd assignments/searching-sorting-fundamentals
python3 starter-code.py
```

The script runs small examples and prints comparison counts for each algorithm. Modify the `main()` in `starter-code.py` to run further experiments.

## Deliverables

- `starter-code.py` (starter implementation and demo)
- `README.md` (this file)
