"""
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        kvmaps = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
                 '7':'pqrs','8':'tuv','9':'wxyz'}
        return reduce(lambda og,digit:[x+y for x in og for y in kvmaps[digit]],digits,[''])
