#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    # Character counting
    for char in line:
        print(f"CHAR_{char}\t1")

    # Word counting
    words = line.split()
    for word in words:
        print(f"WORD_{word}\t1")
