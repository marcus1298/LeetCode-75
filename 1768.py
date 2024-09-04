class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def verifica_igualdade(candidate: str, s: str) -> bool:
            repetitions = len(s) // len(candidate)
            if candidate * repetitions == s:
                return True

        for i in range(min(len(str1), len(str2)), 0, -1):
            candidate = str1[:i]
            if verifica_igualdade(candidate, str1) and verifica_igualdade(candidate, str2):
                return(candidate)

        return ""