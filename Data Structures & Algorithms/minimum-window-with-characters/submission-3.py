class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)> len(s):
            return ""
        uq_t = Counter(t)
        total = 0
        counter = {}
        l, r = 0, 0
        ans = None
        n = len(s)
        while r < n:
            if s[r] in uq_t:
                counter[s[r]] = 1+counter.get(s[r], 0)
                if counter[s[r]] == uq_t[s[r]]:
                    total += 1
                while l <= r and total == len(uq_t):
                    if not ans: 
                        ans = s[l: r+1]    
                    else:
                        if len(ans) > (r-l+1):
                            ans = s[l: r+1]
                    if s[l] in uq_t:
                        counter[s[l]] = counter[s[l]]-1
                        if counter[s[l]] < uq_t[s[l]]:
                            total -= 1
                    l += 1
            r += 1
            
        return ans if ans else ""                   





        