t = int(input())
for _ in range(t):
    n ,k = [int(e) for e in input().split()]

    arr = input().split()

    r  = k % n
    arr = arr[n-r:] + arr[:n-r]

    print(" ".join(arr))
