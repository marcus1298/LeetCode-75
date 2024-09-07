class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        len1, len2 = len(word1), len(word2)

        # Alternar entre as letras de word1 e word2
        while i < len1 and i < len2:
            result.append(word1[i])
            result.append(word2[i])
            i += 1
        
        # Adicionar as letras restantes de word1, se houver
        if i < len1:
            result.append(word1[i:])

        # Adicionar as letras restantes de word2, se houver
        if i < len2:
            result.append(word2[i:])

        # Unir a lista em uma string e retornar
        return ''.join(result)