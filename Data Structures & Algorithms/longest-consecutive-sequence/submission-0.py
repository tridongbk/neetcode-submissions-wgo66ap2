class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        print("Input nums:", nums)
        
        num_set = set(nums)
        print("Converted to set (duplicates removed):", num_set)
        
        longest = 0
        
        for n in num_set:
            print("\nChecking number:", n)
            
            # Check if it's the start of a sequence
            if n - 1 not in num_set:
                print(f"{n} is a START of a sequence")
                
                current = n
                length = 1
                
                # Grow the sequence forward
                while current + 1 in num_set:
                    print(f"  {current + 1} exists → extend sequence")
                    current += 1
                    length += 1
                
                print(f"Sequence starting at {n} has length:", length)
                
                longest = max(longest, length)
                print("Current longest:", longest)
            
            else:
                print(f"{n} is NOT a start (because {n-1} exists)")
        
        print("\nFinal longest sequence length:", longest)
        return longest
