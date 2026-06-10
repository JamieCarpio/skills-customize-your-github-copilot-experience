#!/usr/bin/env python3
"""Starter script for Python Text Processing assignment.

Usage: python3 starter-code.py <filename>

Performs basic text analysis: lines, words, characters, and top word frequencies.
"""

import sys
import string
from collections import Counter


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {path}")
        sys.exit(1)


def normalize_text(text):
    # Lowercase and remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    return text.lower().translate(translator)


def analyze(text, top_n=10):
    lines = text.splitlines()
    words = text.split()
    chars = len(text)

    normalized = normalize_text(text)
    word_list = normalized.split()
    freq = Counter(word_list)

    return {
        "lines": len(lines),
        "words": len(words),
        "characters": chars,
        "top_words": freq.most_common(top_n),
    }


def print_report(path, stats):
    print(f"File: {path}")
    print(f"Lines: {stats['lines']}")
    print(f"Words: {stats['words']}")
    print(f"Characters: {stats['characters']}")
    print("Top words:")
    for word, count in stats["top_words"]:
        print(f"  {word}: {count}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 starter-code.py <filename>")
        sys.exit(1)

    path = sys.argv[1]
    text = read_file(path)
    stats = analyze(text)
    print_report(path, stats)


if __name__ == "__main__":
    main()
