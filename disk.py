#!/usr/bin/env python3

import shutil
import sys

DIR = sys.argv[1]
CRIT = "#FF0000"
NORMAL= "#F3E9C8"
total, used, free = shutil.disk_usage(DIR)

def convert(b):
    tags = [ "B", "K", "MB", "GB", "TB" ]

    i = 0
    d_b = b

    while (i < len(tags) and  b >= 1024):
            d_b = b / 1024.0
            i = i + 1
            b = b / 1024

    return str(round(d_b)) + " " + tags[i]

def used_percent(u, t):
    percent = round(u / t * 100)
    
    if percent >= 80:
        return True
    return False


if used_percent(used, total) == True:
    print(convert(free))
    print("")
    print(CRIT)
else:
    print(convert(free))
    print("")
    print(NORMAL)
