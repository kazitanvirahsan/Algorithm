# Problem : First circular tour that visits all station
# Source: https://www.geeksforgeeks.org/find-a-tour-that-visits-all-stations/
# Author : Kazi Tanvir Ahsan
# Written: 30.03.2023

arr = [[4,6],[6,5],[7,3],[4,5]]
arr_len = 4
start = -1

for i in range(arr_len):

  start = i
  index = start
  fuel = arr[index][0]

  # print(f'index={index}')

  has_reach = False

  while True:

    if fuel - arr[index][1] < 0 :
      # print('Unable to reach!')
      break

    current_station = index

    index = index + 1

    if index == arr_len:
      index = 0

    next_station = index

    fuel = fuel - arr[current_station][1] + arr[next_station][0]

    # print(f'from {current_station} to {next_station} fuel = {fuel}')

    if index == start:
      has_reach = True
      break

  if has_reach == True:
    break

print(f'status = {has_reach} From = {start}')
