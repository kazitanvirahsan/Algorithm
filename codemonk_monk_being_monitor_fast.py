# Title       : Monk being monitor
# Source      : https://www.hackerearth.com/practice/codemonk/
# Comment     : Fast
# Difficulty  : Medium
# Author      : Kazi Ahsan
# Written     : 26.06.2022

# Improvement : different of min and max of an array

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

    t_values = f.values()
    t_min = min(t_values)
    t_max = max(t_values)

    if len(t_values) == 1:
       print('-1')
    else:
       print(abs(t_min - t_max))
