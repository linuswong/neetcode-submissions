class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(char for char in s if char.isalnum())
        clean_s = clean_s.lower()
        half_length = int(len(clean_s)/2)
        for i in range(half_length):
            if clean_s[i] != clean_s[-i-1]:
                return False

        return True