# Author : Kazi ahsan
# Date  : 20.02.2023
# Problem statement 
# https://www.geeksforgeeks.org/connect-n-ropes-minimum-cost/


import heapq

s = input().split()
li = [ int(ele) for ele in s]
 
# using heapify to convert list into heap
heapq.heapify(li)

total_cost = 0
while len(li) >  1:
 first = heapq.heappop(li)
 second = heapq.heappop(li)
 temp_cost = first + second
 total_cost  = temp_cost  +  total_cost
 heapq.heappush(li, temp_cost)

print(total_cost)

