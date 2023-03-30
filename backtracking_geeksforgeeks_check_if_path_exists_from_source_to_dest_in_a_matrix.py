# Title   : Check if any path exist from source(first cell) to destination (last cell) in a 2D matrix
# Source  : https://www.geeksforgeeks.org/check-possible-path-2d-matrix/
# Author  : Kazi Ahsan
# Written : 29.03.2023

def is_valid(row, col , row_max, col_max, a , visited):
  if row >=0 and row < row_max and col >= 0 and col < col_max and \
    visited[row][col] == False and a[row][col] == 0:
    return True
  return False

def find_path(start_row, start_col , row_max, col_max, a, visited, is_exists):

  visited[start_row][start_col] = True

  if start_row == row_max - 1 and  start_col == col_max - 1:
    return True

  # top
  r1 = r2 = r3 = r4 = False

  if is_valid(start_row, start_col -1 , row_max, col_max, a , visited):
    r1 = find_path(start_row, start_col -1 , row_max, col_max, a, visited, is_exists)
  
  # bottom
  if is_valid(start_row, start_col + 1, row_max, col_max, a , visited):
    r2 = find_path(start_row, start_col +1, row_max, col_max, a, visited, is_exists)
  # left
  if is_valid(start_row -1, start_col , row_max, col_max, a , visited):
    r3 = find_path(start_row -1, start_col , row_max, col_max, a, visited, is_exists)
  # right
  if is_valid(start_row + 1, start_col , row_max, col_max, a , visited):
    r4 = find_path(start_row + 1, start_col , row_max, col_max, a, visited, is_exists)

  visited[start_row][start_col] = False

  return r1 or r2 or r3 or r4

a = [
     [0,0],
     [0,-1],
]
row_max = 2
col_max = 2

visited = [ [ False for _ in range(col_max)] for _ in range(row_max)]

start_row = 0
start_col = 0

is_exists = False
result  = find_path(start_row, start_col , row_max, col_max, a, visited, is_exists)
print('Exists') if result == True else print('Not exists')
