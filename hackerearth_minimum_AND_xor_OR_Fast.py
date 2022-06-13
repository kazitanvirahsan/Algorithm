# Title   : Minimum AND xor OR
# Source  : https://www.hackerearth.com/practice/codemonk/
# Comment : Fast version
# Author  : Kazi Ahsan
# Written : 13.06.2022

# Improvement : j = i + 1
# Improvement : (a[i] & a[j]) ^ (a[i] | a[j]) = a[i] ^ a[j]
# Improvement : sort input array
# Improvement : Remove inner loop
# Improvement : Use variable instead of using hash to track min

import sys

t_1     = int(input())

for _ in range(t_1):
    a_len    = int(input())
    a        = [int(e) for e in input().split()]

    a.sort()

    t_min = sys.maxsize

    for i in range(a_len-1):
      t_min = min(t_min, a[i] ^ a[i + 1]) 

    print(t_min)
