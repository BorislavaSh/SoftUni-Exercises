from collections import deque

food = int(input())

orders = input().split(' ')
orders = [int(i) for i in orders]
print(max(orders))
que = deque(orders)

for order in orders:
    if food >= order:
        food -= order
        que.popleft()

ll = []
if list(que):
    for left in que:
        ll.append(left)
        print(f'Orders left: {ll}')
else:
    print('Orders complete')