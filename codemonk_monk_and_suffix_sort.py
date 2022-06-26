# Title      : Monk and Suffix Sort
# Source     : https://www.hackerearth.com/practice/codemonk/
# Comment    : 
# Difficulty : Easy
# Author     : Kazi Ahsan
# Written    : 26.06.2022

s, k = input().split()

s_len = len(s)
arr   = []
for i in range(s_len):
    arr.append(s[i:])


arr.sort()
print(arr[int(k)-1])



