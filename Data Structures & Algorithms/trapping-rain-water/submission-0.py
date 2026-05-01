class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        
        for i in range(1, len(height)):
            if height[i-1] > left_max[i-1]:
                left_max[i] = height[i-1]
            else:
                left_max[i] = left_max[i-1]  
        # print(left_max)
        trapped_water = 0
        rt_max = 0
        for i in range(len(height)-2, -1, -1):
            rt_max = max(rt_max, height[i+1])
            min_val = min(left_max[i], rt_max)
            water = min_val-height[i] if height[i] < min_val else 0
            # print(rt_max, min_val, water)
            trapped_water +=  water

        return trapped_water    




        