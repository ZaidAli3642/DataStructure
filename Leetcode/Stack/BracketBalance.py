class BracketBalance:
    def is_balanced(self, expression: str):
        stack = []

        # create a hashmap
        bracket_pairs = {
            '(': ')',
            '{': '}',
            '[': ']',
            '<': '>'
        }
        opening_brackets = bracket_pairs.keys()
        closing_brackets = bracket_pairs.values()

        for exp in expression:
            if exp in opening_brackets:
                stack.append(exp)
            
            if exp in closing_brackets:
                if len(stack) == 0: 
                    return False
                poped_exp = stack.pop()

                if bracket_pairs[poped_exp] != exp:
                    return False
        
        return len(stack) == 0
    
bracket_balance = BracketBalance()

result = bracket_balance.is_balanced('([1+2])')
print(result)