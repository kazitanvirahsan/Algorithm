# Title      : Monk being monitor
# Source     : https://www.hackerearth.com/practice/codemonk/
# Comment    : Slow
# Difficulty : Medium
# Author     : Kazi Ahsan
# Written    : 26.06.2022

t = int(input())

for _ in range(t):
    n    = int(input())
    arr  = input().split()
    arr_len = len(arr)
    arr  = [int(arr[i]) for i in range(arr_len)]

    arr_len = len(arr)
    f = {}
    for i in range(arr_len):
        if arr[i] in f:
          f[arr[i]] = f[arr[i]] + 1
        else:
          f[arr[i]] = 1

    t_keys = list(f.keys())

   
    if len(t_keys) == 1:
       print('-1')
    else:

        t_keys.sort()
        t_keys_len = len(t_keys)
        t_max = 0

        for i in range(t_keys_len):
          for j in range(i + 1,t_keys_len):
            t_max = max(t_max, abs(f[t_keys[i]] - f[t_keys[j]]))
            
        print(t_max)




