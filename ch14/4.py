import heapq

n = int(input())
card = []
for c in range(n):
    heapq.heappush(card, int(input()))

sol = 0

if len(card) == 1:
    print(sol)

else:
    while (len(card) > 1):
        min1 = heapq.heappop(card)
        min2 = heapq.heappop(card)
        sol += min1 + min2
        heapq.heappush(card, min1 + min2)

    print(sol)
