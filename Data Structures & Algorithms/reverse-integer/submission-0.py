INT_MAX = 2**31 - 1
INT_MIN = -2**31

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Step 1: define result
        res = 0
        
        # Step 2: loop while x != 0
        while x != 0:
            # Step 3: get last digit
            digit = x % 10
            
            # Step 4: remove last digit from x
            x = x // 10
            
            # Step 5: check overflow before adding digit
            if res > INT_MAX // 10 or res < INT_MIN // 10:
                return 0
            
            # Step 6: build result
            res = res*10 + digit
        
        res *= sign

        # Step 7: return result
        return res

'''
⚡ Tóm gọn để nhớ
# pop digit → check overflow → push digit
'''