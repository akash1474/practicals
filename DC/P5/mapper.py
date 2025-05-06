#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split()
    if len(parts) == 3:
        year, min_temp, max_temp = parts
        print(f"{year} {min_temp} {max_temp}")