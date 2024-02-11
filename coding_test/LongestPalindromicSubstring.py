class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_length = len(s)
        palindrome = ''
        for i in range(s_length):
            center = s[i]
            left, right = i-1, i+1
            candidate = center
            single_alph_palin = True

            while i >=0 and right <= s_length-1:
                if center == s[right] and single_alph_palin:
                    candidate = candidate + s[right]
                    right += 1
                elif left >=0 and s[left] == s[right]:
                    single_alph_palin = False
                    candidate = s[left] + candidate + s[right]
                    left -= 1
                    right += 1
                else:
                    break
            if len(palindrome) < len(candidate):
                palindrome = candidate
        return palindrome

if __name__ == "__main__":
    input_s = 'babad' 
    # input_s = 'cbbd'
    input_s = 'babadddddd' 
    # input_s = 'bb' 
    # input_s = ''
    solution = Solution()
    palindrome = solution.longestPalindrome(input_s)
    print(palindrome)