class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_longest = ''
        str_cur = ''
        
        for i in range(len(s)):
            if s[i] in str_cur:
                matching_idx = str_cur.index(s[i])
                if len(str_longest) <= len(str_cur):
                    str_longest = str_cur
                str_cur = str_cur[matching_idx+1:] + s[i]
            else:
                str_cur += s[i]
            # print('iter ({}), longest: {}, current: {}'.format(i, str_longest, str_cur))
            # # print(str_cur)
        if len(str_longest) <= len(str_cur):
            str_longest = str_cur
            
        return len(str_longest), str_longest

if __name__ == '__main__':
    solution = Solution()
    s = 'abcabcbb'
    s = 'pwwkew'
    s = ' '
    # s = "hkcpmprxxxqw"
    # from IPython import embed
    # embed()
    print(solution.lengthOfLongestSubstring(s))
    
    