class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # count_map = {}
        # for number in nums:
        #     count_map[number] = count_map.get(number, 0) + 1
        #     if count_map[number]!=1:
        #         return number
        # return -1

        # floyd's cycle detection, with the values of nums being pointers to indices the cell is pointing to
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow==slow2:
                break
        
        return slow