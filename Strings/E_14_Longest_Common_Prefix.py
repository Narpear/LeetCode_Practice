class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        chars = []
        min_length = len(strs[0])
        for element in strs:
            min_length = min(min_length, len(element))
        # print(min_length)
        
        for i in range(min_length):
            flag = 1
            character = strs[0][i]
            # print(character)
            for element in strs:
                if character==element[i]:
                    continue
                else:
                    flag = 0
                    break
            if flag:
                chars.append(character)
            else:
                break

        result = "".join(chars)
        # print(result)
        return result

