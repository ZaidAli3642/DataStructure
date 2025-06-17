from collections import defaultdict

class GroupAnagram:
    @staticmethod
    def group_anagram(strs=["act", "pots", "tops", "cat", "stop", "hat"]):
        anagram_group = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)
            anagram_group[key].append(string)

        return list(anagram_group.values())

print(GroupAnagram.group_anagram())
