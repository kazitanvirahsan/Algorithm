# Title   : Minimum AND xor OR
# Source  : https://www.hackerearth.com/practice/codemonk/
# Comment : Slow version
# Author  : Kazi Ahsan
# Written : 13.06.2022

t_1    = int(input())                  # Reading input from STDIN

for _ in range(t_1):
    a_len    = int(input())
    a = [ int(e) for e in input().split()]
    t_pairs = {}
    for i in range(a_len):
        for j in range(a_len):
            if i != j:
                if not a[i] + a[j] in t_pairs:
                    t_key = a[i] + a[j]
                    t_pairs[t_key] = (a[i] & a[j]) ^ (a[i] | a[j])
            
    print(min(t_pairs.values()))
