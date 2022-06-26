# Title      : Monk and Nice Strings
# Source     : https://www.hackerearth.com/practice/codemonk/
# Comment    : 
# Difficulty : Easy
# Author     : Kazi Ahsan
# Written    : 24.06.2022

c   = int(input())
arr = []
for _ in range(c):
    d = input()
    arr.append(d)

l_arr = len(arr)
for i in range(l_arr):
  c = 0
  for j in range(0, i):
    if  arr[j] < arr[i]:
      c = c + 1
  print(f'{c}')

