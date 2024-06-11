from typing import List

class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for number in nums:
            if number in counts:
                counts[number] += 1
                continue
            counts[number] = 1
      
        counts_items = list(counts.items())

        counts_items.sort(reverse = True, key = lambda x: x[1])
        # print(counts_items)
        return [element[0] for element in counts_items[:k]]

        