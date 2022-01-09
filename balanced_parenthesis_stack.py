class Solution:
    def valid_parenthesis(self, arr):
        s   = []
        i = 0
        arr_len = len(arr)
        while i < arr_len:
            if arr[i] == '(':
                s.append('(')
            
            if arr[i] == ')':
                if len(s) == 0:
                    return 0
                s.pop()

            i = i + 1

        if len(s) > 0:
            return 0
        return 1

    # @param A : string
    # @return an integer
    def solve(self, A):
        return self.valid_parenthesis(list(A))

