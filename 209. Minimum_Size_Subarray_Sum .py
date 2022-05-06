
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
