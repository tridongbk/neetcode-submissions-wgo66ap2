class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if value in rows[r]:
                    return False
                if value in cols[c]:
                    return False
                if value in boxes[box_index]:
                    return False

                # Add value
                rows[r].add(value)
                cols[c].add(value)
                boxes[box_index].add(value)

                # 🔎 FULL STATE PRINT
                print("\n=================================")
                print(f"Added {value} at position ({r}, {c})")
                print("ROWS:")
                for i in range(9):
                    print(f"Row {i}: {rows[i]}")

                print("\nCOLS:")
                for i in range(9):
                    print(f"Col {i}: {cols[i]}")

                print("\nBOXES:")
                for i in range(9):
                    print(f"Box {i}: {boxes[i]}")
                print("=================================")

        return True
