#!/usr/bin/env python3

import sys
if len(sys.argv) == 1:
    print("none")
else:
    print(f"parameters: {len(sys.argv) - 1}")
    for param in sys.argv[1:]:
        count = 0
        for character in param:
            count += 1
        print(f"{param}: {count}")