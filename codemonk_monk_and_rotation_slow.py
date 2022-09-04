t = int(input())
for _ in range(t):
    n ,k = [int(e) for e in input().split()]

    arr = input().split()

    for _ in range(k):
      arr = [arr[len(arr)-1]] + arr[:len(arr) - 1]

    print(" ".join(arr))
