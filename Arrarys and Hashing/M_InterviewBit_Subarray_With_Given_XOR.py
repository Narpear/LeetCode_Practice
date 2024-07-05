class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # similar to leetcode 560 (Subarray Sum Equals K)
        current_xor = 0
        prefix_xors = {0:1}
        result = 0
        
        for number in A:
            current_xor = current_xor^number
            # xor is its own inverse
            difference_xor = B^current_xor
            result += prefix_xors.get(difference_xor, 0)
            prefix_xors[current_xor] = prefix_xors.get(current_xor, 0) + 1
        
        return result
        
