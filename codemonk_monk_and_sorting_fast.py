# Last n digit means num % 100000 )
# First time num / 1 returns the original number
# Remove last 5 digit means num / 100000

t_numOfInputs = input()
t_arr =  [int(num) for num in input().split()]

t_max = max(t_arr)
t_divide  = 1

while(t_divide < t_max):
    t_arr.sort(key=lambda x: ((x / t_divide ) % 100000))
    t_result = ' '.join([str(num) for num in t_arr])
    print(t_result)
    t_divide  = t_divide  * pow(10 , 5)
