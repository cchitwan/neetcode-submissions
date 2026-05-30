class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = -math.inf

        min_product = 1
        max_product = 1

        for num in nums:
           
            t_product = min(num*min_product, num*max_product, num)
            max_product = max(num*min_product, num*max_product, num)
            min_product = t_product

            result = max(max_product, result)

            
        return result        
        