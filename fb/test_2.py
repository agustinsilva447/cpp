import numpy as np

def lengthOfLongestSubstring(s: str) -> int:
    max_cnt = 1
    left = 0
    while left < len(s) - max_cnt:
        right = left + max_cnt
        while right < (len(s) + 1):
            tot = set()
            cnt = 0
            for i in np.arange(left, right, 1):
                if s[i] not in tot:
                    tot.add(s[i])
                    cnt += 1
                else:
                    if cnt>max_cnt:
                        max_cnt = cnt
                    tot = set()
                    cnt = 0
            if cnt>max_cnt:
                max_cnt = cnt
            right += 1
        left += 1
    return max_cnt

a = "wllxdiklosdrdxfohgwringzefwbytmwgxtjhdxwycpbawphcnbmajmeokhoftlmsexakuyixplxmagoojdospvjbcxh"
b = lengthOfLongestSubstring(a)
print(a,b)