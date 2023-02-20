# Author : Kazi ahsan
# Date  : 20.02.2023
# Comment : Dynamic programming concept (bottom up approach)
n = int(input())
l = n + 1
dp = [0 for _ in range(l)]
dp[0] = 1
for i in range(1,l):
  dp[i] = dp[i-1] * i

print(dp[n])
