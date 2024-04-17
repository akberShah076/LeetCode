class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #Find max in candies 
        max = candies[0]
        result = []
        
        for num in candies:
            if (num > max):
                max = num 
        
        for i in range(len(candies)):
            if (candies[i] + extraCandies >= max):
                result.append(True)
            else:
                result.append(False)

        return result
