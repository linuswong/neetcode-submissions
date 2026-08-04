class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(char for char in s if char.isalnum())
        clean_s = clean_s.lower()

        if len(clean_s) <=1:
            return True

        half_length = int(len(clean_s)/2)
        return clean_s[half_length:] == clean_s[:-half_length][::-1]