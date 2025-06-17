class FirstNonRepeatedCharacter:
    def __init__(self) -> None:
        self.text = 'a green apple'
    
    def getFirstNonRepeatedCharacter(self):
        char = {}
        
        for value in self.text:
            char[value] = (char.get(value, 0) + 1) or 1
        
        for ch in char:
            if char.get(ch) == 1 and ch != ' ':
                return ch
        
        return None

first_non_repeated_char = FirstNonRepeatedCharacter()
print(first_non_repeated_char.getFirstNonRepeatedCharacter())