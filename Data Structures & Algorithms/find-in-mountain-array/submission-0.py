class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l,r = 0, n-1
        res = None
        cache = {}

        def find_peak(l, r):
            i,j = l, r
            
            while l < r:
                mid = (l+r) // 2
                mid_val = mountainArr.get(mid)
                left_val = mountainArr.get(mid-1)
                right_val = mountainArr.get(mid+1)
                cache[mid] = mid_val
                cache[mid-1] = left_val
                cache[mid+1] = right_val
                if left_val<mid_val>right_val:
                    return mid
                elif left_val<mid_val<right_val:
                    l = mid
                else:
                    r = mid        
            return -1
            
        peak = find_peak(l, r)
        print('peak ', peak)

        def binary_search(i:int, j:int, increasing: True):
            while i<=j:
                mid = (i+j) // 2
                mid_val = cache.get(mid, mountainArr.get(mid))
                cache[mid] = mid_val    
                if increasing:
                    if mid_val == target:
                        return mid
                    elif mid_val < target:
                        i = mid+1
                    else:
                        j = mid-1  
                else:
                    if mid_val == target:
                        return mid
                    elif mid_val > target:
                        i = mid+1
                    else:
                        j = mid-1 

            return -1          

        #search in first half
        
        res = binary_search(0, peak, True)

        if res > -1: return res

        res = binary_search(peak+1, r, False)


        return res            



        