class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num

        return res 

'''
🧠 Tính chất XOR
a ^ a = 0
a ^ 0 = a

👉 Nghĩa là:

số giống nhau → triệt tiêu nhau
số lẻ loi → còn lại
'''