# Title   : Minimum AND xor OR
# Source  : https://www.hackerearth.com/practice/codemonk/
# Comment : Easy
# Author  : Kazi Ahsan
# Written : 20.06.2022

t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
       arr.append([int(cell) for cell in input().split()])

    t_sum = 0
    for i in range(n):
      for j in range(n):
        for p in range(n):
          for q in range(n):
            if i <= p and j <= q and arr[i][j] > arr[p][q]:
              t_sum = t_sum + 1

    print(t_sum)
