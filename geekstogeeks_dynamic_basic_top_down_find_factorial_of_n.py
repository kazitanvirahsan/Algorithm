# Author : Kazi ahsan
# Date  : 20.02.2023
# Comment : Dynamic programming concept (top down approach)

def fact(n):
  if n == 1:
    return 1
  return n * fact(n-1)

print(fact(5))
