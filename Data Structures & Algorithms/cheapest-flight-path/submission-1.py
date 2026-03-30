class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Step 1: init cheapest prices
        prices = [float("inf")] * n
        prices[src] = 0

        # Step 2: relax all edges k + 1 times
        for _ in range(k + 1):
            temp = prices.copy()

            # Step 3: try every flight
            for u, v, w in flights:
                if prices[u] == float("inf"):
                    continue

                temp[v] = min(temp[v], prices[u] + w)

            # Step 4: update prices
            prices = temp

        # Step 5: return result
        return -1 if prices[dst] == float("inf") else prices[dst]

'''
Bellman-Ford for at most k stops

- At most k stops = at most k + 1 edges
- prices[i] = cheapest cost to reach node i
- Relax all flights k + 1 times
- Use a copy array each round so one round only uses previous results
- If dst is still inf, return -1
'''