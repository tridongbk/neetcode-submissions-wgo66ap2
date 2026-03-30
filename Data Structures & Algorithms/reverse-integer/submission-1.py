INT_MAX = 2**31 - 1
INT_MIN = -2**31

class Solution:
    def reverse(self, x: int) -> int:
        # Step 1: handle sign
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Step 2: define result
        res = 0

        # Step 3: process each digit
        while x != 0:
            # Step 3.1: get last digit
            digit = x % 10

            # Step 3.2: remove last digit
            x //= 10

            # Step 3.3: check overflow BEFORE adding digit
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                return 0

            # Step 3.4: build reversed number
            res = res * 10 + digit

        # Step 4: restore sign
        res *= sign

        # Step 5: final overflow check
        if res < INT_MIN or res > INT_MAX:
            return 0

        # Step 6: return result
        return res

'''
Reverse Integer:

- Extract digits from right to left using % 10
- Remove digit using // 10
- Build reversed number: res = res * 10 + digit

Key points:
- Handle negative using sign + abs
- Check overflow BEFORE pushing digit
- Condition:
    res > INT_MAX // 10
    or res == INT_MAX // 10 and digit > 7 (means: res > 2147483647)

- If overflow → return 0
'''