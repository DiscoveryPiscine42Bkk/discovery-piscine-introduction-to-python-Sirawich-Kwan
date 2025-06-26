#!/usr/bin/env python3

import re
import sys

if len(sys.argv) != 3:
    print("none")
else:
    pattern = sys.argv[1]
    param = sys.argv[2]
    result = re.findall(pattern, param)
    print(len(result))