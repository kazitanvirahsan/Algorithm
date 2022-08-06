# Title   : Monk and Sorting Algorithm
# Source  : https://www.hackerearth.com/practice/codemonk/
# Comment : Medium
# Author  : Kazi Ahsan
# Written : 02.07.2022

# 213456789 167890 123456789

n     = input()
t_arr = input().split()

i = 1
while True:
    w = {}
    for j in range(len(t_arr)):
        t_num = t_arr[j]
        t_len = len(t_num)

        sc = 5 * i
        ec = 1 + 5 * (i - 1)
        t_str = ''
        while ec <= sc:
           t_idx = t_len - ec
           if t_idx < 0:
             break
           t_str = t_num[t_idx] + t_str 
           ec = ec + 1

        t_wgt = 0
        if t_str == '':
          t_wgt = 0
        else:
          t_wgt = int(t_str)

        w[j] = t_wgt

    if sum(w.values()) == 0:
      #print(t_arr)
      break

    t_sorted = sorted(w.items(), key=lambda x: x[1])

    t_arr_1 = []
    # Check if all weights are zero
    for l in t_sorted:
      t_arr_1.append(t_arr[l[0]])
    t_arr =  t_arr_1
    
    print(*t_arr)

    i = i + 1
