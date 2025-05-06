#!/usr/bin/env python3
import sys; from collections import defaultdict

counts = defaultdict(int)

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    counts[key] += int(value)

# Output characters and words separately
print("=== Character Counts ===")
for key in sorted(counts):
    if key.startswith("CHAR_"):
        print(f"{key[5:]}\t{counts[key]}")

print("\n=== Word Counts ===")
for key in sorted(counts):
    if key.startswith("WORD_"):
        print(f"{key[5:]}\t{counts[key]}")
