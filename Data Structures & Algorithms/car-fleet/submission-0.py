from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()

        print("Sorted cars:", cars)

        stack = []

        for pos, spd in reversed(cars):
            time = (target - pos) / spd
            print(f"\nCar at pos={pos}, speed={spd}, time={time}")

            if not stack:
                print("  No fleet ahead -> new fleet")
                stack.append(time)
            elif time > stack[-1]:
                print(f"  {time} > {stack[-1]} -> cannot catch -> new fleet")
                stack.append(time)
            else:
                print(f"  {time} <= {stack[-1]} -> merges with fleet ahead")

            print("  Fleet times:", stack)

        print("\nTotal fleets:", len(stack))
        return len(stack)
