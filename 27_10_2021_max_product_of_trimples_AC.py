import sys

class Solution:
    # @param A : list of integers
    # @return an integer

    
    def maxp3(self, A):
        
        A.sort()
        l = len(A)
        return max( A[0] * A[1] * A[l-1], A[l-1] * A[l-2] * A[l-3])          
