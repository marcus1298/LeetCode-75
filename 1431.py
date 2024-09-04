from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxV = candies[0] + extraCandies
        output = []
        for i in candies:
            if(i + extraCandies >= maxV):
                output.append(True)
            else:
                output.append(False')
        return(output)

# Testando a função com os parâmetros fornecidos
candies = [2,3,5,1,3]
extraCandies = 3
solution = Solution()
result = solution.kidsWithCandies(candies, extraCandies)
print(result)