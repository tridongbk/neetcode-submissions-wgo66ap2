from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        print("Temperatures:", temperatures)
        print("-----------------------------")

        for i, temp in enumerate(temperatures):
            print(f"\nDay {i}, Temp = {temp}")
            print("Stack before:", stack)

            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                wait_days = i - prev_index
                result[prev_index] = wait_days

                print(f"  Warmer than day {prev_index} ({temperatures[prev_index]})")
                print(f"  -> result[{prev_index}] = {wait_days}")

            stack.append(i)

            print("Stack after:", stack)
            print("Result so far:", result)

        print("\nFinal Result:", result)
        return result
