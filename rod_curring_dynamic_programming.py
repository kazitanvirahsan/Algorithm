# Title      : Cutting a Rod
# Source     : geekstogeek
# Difficulty : Easy
# Author     : Kazi Ahsan
# Written    : 26.03.2023

def rod_cutting(cost_arr, len_arr,rod_len):
  row_len = len(len_arr) + 1
  col_len = rod_len + 1

  d = [ [0 for _ in range(col_len)]  for _ in range(row_len)]

  for row in range(1, row_len):
    for col in range(col_len):
      f1 = col // len_arr[row - 1]
      t_cost = f1 * cost_arr[row - 1]
      l2 =  col % len_arr[row - 1]
      if l2 > 0:
        t_cost = t_cost + d[l2][l2]
      d[row][col] = max( d[row-1][col] , t_cost)

  return d[row_len-1][col_len-1]


rod_len = 8
cost_arr = [1,5,8,9,10,17,17,20]
cost_arr = [3,5,8,9,10,17,17,20]
len_arr = [1,2,3,4,5,6,7,8]

result = rod_cutting(cost_arr, len_arr, rod_len)
print('Max price = {}'.format(result))
