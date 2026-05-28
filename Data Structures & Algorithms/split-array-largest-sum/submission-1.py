#Split Array Largest Sum
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check_if_split_possible(mid: int)->bool:
            sub_array_count = 1
            current_sum = 0
            for n in nums:
                if current_sum+n > mid:
                    sub_array_count += 1
                    current_sum = n
                    if sub_array_count > k:
                        return False
                else:
                    current_sum += n
            # print(sub_array_count, k)        
            return True

        low = max(nums)
        high = sum(nums)
        ans = high
        while low <= high:
            mid = (high+low) // 2
            if check_if_split_possible(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans            

                        
        