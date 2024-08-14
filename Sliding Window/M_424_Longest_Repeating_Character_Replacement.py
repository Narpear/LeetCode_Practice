class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        result = 0

        left = 0
        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right], 0)

            # make it a valid window
            while (right-left+1)-max(counts.values())>k:
                counts[s[left]] -= 1
                left += 1

            result = max(result, (right-left+1))
        
        return result