class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n - 1)
            count += 1

        return count

'''
🧠 Ý tưởng
n = n & (n - 1)

👉 Mỗi lần làm vậy sẽ xóa 1 bit 1 cuối cùng

🔍 Ví dụ
n = 101100
Bước 1:
n - 1 = 101011
AND:
101100
&101011
------
101000

👉 bit 1 cuối cùng bị xóa ✅
'''