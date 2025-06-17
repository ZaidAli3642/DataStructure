class ValidAnagram:
    @staticmethod
    def valid_anagram(s: str, t: str):
        alphabets = [0] * 26

        if len(s) != len(t):
            return False
        
        for i in range(len(t)):
            alphabets[ord(t[i]) - ord('a')] += 1
            alphabets[ord(s[i]) - ord('a')] -= 1
        
        for char in alphabets:
            if char != 0:
                return False
        
        return True

s = "racecar"
t = "carrace"
print(ValidAnagram.valid_anagram(s,t))