t = int(input())
for _ in range(t):
    n , k = [int(ele) for ele in input().split()]
    s = input()

    l = n
    i = 0
    t_max = ''
    ops = 0
    d = 0
    while i<l:
      if s > t_max:
        t_max = s
        ops = i
      elif s == t_max:
        d = i - ops
        break

      s = s[1:] + s[0]
      i = i + 1

    if d == 0:
      print(ops + (k - 1) * l )
    else:
      print(ops + (d * (k-1)))
