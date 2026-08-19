class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        max_count = 0
        max_len = 0
        dic = {}

        for j in range(len(s)):

            dic[s[j]] = dic.get(s[j], 0) + 1

            max_count = max(max_count, dic[s[j]])

            while (j - i + 1) - max_count > k:
                dic[s[i]] -= 1
                i += 1

            max_len = max(max_len, j - i + 1)

        return max_len