
class Solution:
    def minSubArrayLen(self, target: int, nums:[int]) -> int:

        if sum(nums) < target:
            return 0
        else:
            i = j = suma = 0
            ans = 1000000001
            while True:
                if suma >= target:
                    ans = min(ans, j - i)
                    suma -= nums[i]
                    i += 1

                else:
                    if j == len(nums):
                        break
                    suma += nums[j]
                    j += 1
            return ans
        
if __name__ == "__main__":
    '''
    Test case1- target = 7, nums = [2,3,1,2,4,3]
    Expected Output: 2
    '''
    ans=Solution().minSubArrayLen(target=7,nums=[2, 3, 1, 2, 4, 3])
    print(ans)
    
