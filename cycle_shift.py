#https://www.hackerearth.com/practice/codemonk/
def count_ops(s, n , k ):
    t_max           = ''
    t_pos           = []
    t_hash          = {}

    for i in range(n):
        if s == t_max:
            t_pos.append(i - t_pos[-1])

        if s > t_max:
            t_max = s
            t_pos = [i]
        
        print(s)
        s   = s[1:] + s[:1]
        
    return t_pos


def total_ops(n, k ,t_pos):
    
    t_l   = len(t_pos)
    i     = 0
    t_ops = 0

    while k > 0:
        if i == t_l:
           t_ops = t_ops + (n - 1) - t_pos[i-1] + 1
           i = 0
           continue

        if i == 0:
          t_ops = t_ops + t_pos[i]
        else:
          t_ops = t_ops + t_pos[i] - t_pos[i-1]


        #print('k=%s t_pos=%s'%(k,t_pos[i]))
        k  = k -1
        i  = i + 1


    return t_ops


t = int(input())
temp_count       = 0 
while t > 0 :
    temp_inputs =  input()
    n, k  = temp_inputs.split()
    n = int(n)
    k = int(k)
    s = input()
    t_pos = count_ops(s, n , k )
    t_ops = total_ops(n , k , t_pos)
    print(t_ops)
    t = t - 1

