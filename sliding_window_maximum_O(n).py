from collections import deque 

class Solution:

    def process(self, arr, k):

        Qi = deque()

        for i in range(0, k):
            
            while Qi and arr[i] >= arr[Qi[-1]]:
                Qi.pop()

            Qi.append(i)

        res = []

        n = len(arr)
        for i in range(k,n):

            res.append(arr[Qi[0]])

            cur_ele = arr[i]

            # Remove everything that is outside the window
            while Qi and Qi[0] <= i - k:
                Qi.popleft()

            # Keep removing element from end if current element id greater
            while Qi and arr[i] >= arr[Qi[-1]]:
                Qi.pop()

            Qi.append(i)

        res.append(arr[Qi[0]])

        return res


    def slidingMaximum(self, A, B):
        return self.process(A, B)


s = Solution()
print(s.slidingMaximum([12, 1, 78, 90, 57, 89, 56],3))
