# 📘 Assignment: Python Text Processing

## 🎯 Objective

Practice string manipulation, file I/O, and text-processing techniques in Python by building utilities that analyze and transform plain-text files.

## 📝 Tasks

### 🛠️	Core: Text Analyzer

#### Description
Write a command-line Python program that reads a text file, performs basic analysis (counts lines, words, characters), computes the most common words, and reports simple statistics.

#### Requirements
Completed program should:

- Accept a filename as a command-line argument
- Print the number of lines, words, and characters in the file
- Produce a frequency list of the top 10 most common words (case-insensitive)
- Ignore common punctuation when counting words
- Handle missing files with a clear error message


### 🛠️	Optional: Text Transformer

#### Description
Add features that modify or clean the input text and write results to a new file.

#### Requirements
Completed enhancements may include (pick one or more):

- Remove stopwords from the text and save the cleaned version
- Implement find-and-replace for a target word or pattern (use `re`)
- Normalize whitespace and casing
- Output a summary JSON file with statistics

## Running the starter script

From the assignment folder:

```bash
cd assignments/python-text-processing
python3 starter-code.py sample.txt
```

Example output should include lines/words/characters counts and the top 10 words.

## Deliverables

- `starter-code.py` (starter script provided)
- `sample.txt` (example input file)
- Short README describing how to run the script and any optional features implemented
