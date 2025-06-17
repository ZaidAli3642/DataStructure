class FirstRepeatedCharacter:
    def __init__(self) -> None:
        self.text = 'green apple'
    
    def getFirstRepeatedCharacter(self):
        char = set()

        for value in self.text:
            if value in char:
                return value
            
            char.add(value)
        
        return None

first_repeated_character = FirstRepeatedCharacter()
print(first_repeated_character.getFirstRepeatedCharacter())