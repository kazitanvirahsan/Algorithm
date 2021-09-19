class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        res = []
        slide_end   = len(A) - B
        slide_start = 0
        
        while slide_start <= slide_end:
            res.append(max(A[slide_start:slide_start + B]))
            slide_start = slide_start + 1
        return res


s = Solution()
print(s.slidingMaximum([12, 1, 78, 90, 57, 89, 56],3))