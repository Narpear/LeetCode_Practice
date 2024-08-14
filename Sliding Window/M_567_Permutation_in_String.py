class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2)<len(s1):
            return False
        
        counts_s1 = {}
        counts_window = {}
        n_s1 = len(s1)
        
        for i in range(n_s1):
            counts_s1[s1[i]] = counts_s1.get(s1[i], 0) + 1
            counts_window[s2[i]] = counts_window.get(s2[i], 0) + 1
        
        if counts_s1==counts_window:
            return True
        
        lp = 0
        for rp in range(n_s1, len(s2)):
            counts_window[s2[lp]] -= 1
            if counts_window[s2[lp]] == 0:
                counts_window.pop(s2[lp])     
            counts_window[s2[rp]] = counts_window.get(s2[rp], 0) + 1
            if counts_s1 == counts_window:
                return True
            lp += 1

        return False

        