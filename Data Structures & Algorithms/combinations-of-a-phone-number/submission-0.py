class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        res = []
        letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtrack(index, current_string):
            if index == len(digits):
                res.append(current_string)
                return
            digit = digits[index]
            possible_letters = letter_map[digit]
            for letter in possible_letters:
                backtrack(index + 1, current_string + letter)
        backtrack(0, "")
        return res



