class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Step 1: handle edge case
        if not prices:
            return 0
        
        # Step 2: define memo
        memo = {}
        
        # Step 3: dfs(i, buying)
        # i = current day
        # buying = True  -> can buy now
        # buying = False -> currently holding a stock
        def dfs(i, buying):
            # Step 4: base case
            if i >= len(prices):
                return 0
            
            # Step 5: memo
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            # Step 6: if can buy
            if buying:
                buy = -prices[i] + dfs(i+1, False)
                skip = dfs(i+1, True)
                memo[(i, buying)] = max(buy, skip)
            
            # Step 7: if holding stock
            else:
                sell = prices[i] + dfs(i+2, True)
                skip = dfs(i+1, False)
                memo[(i, buying)] =max(sell, skip)
            
            # Step 8: return result
            return memo[(i, buying)]
        
        # Step 9: start from day 0, can buy
        return dfs(0, True)

        '''
		Khi buying = True (có quyền mua)

		Bạn có 2 lựa chọn:

		✔️ Mua:
		mất tiền → -prices[i]
		chuyển sang trạng thái holding
		buy = -prices[i] + dfs(i + 1, False)
		✔️ Skip:
		skip = dfs(i + 1, True)

		👉 chọn max:

		memo[(i, buying)] = max(buy, skip)

		====
		Khi buying = False (đang giữ cổ)
		✔️ Bán:
		kiếm tiền → +prices[i]
		cooldown 1 ngày → nhảy i + 2
		sell = prices[i] + dfs(i + 2, True)
		✔️ Skip:
		skip = dfs(i + 1, False)

		👉 chọn max:

		memo[(i, buying)] = max(sell, skip)
        '''