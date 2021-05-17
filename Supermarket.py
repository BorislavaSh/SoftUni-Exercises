from collections import deque

names_queue = deque()
names = input().split(' ')
for n in names:
    names_queue.append(n)

while True:
    passes = int(input())
    for i in range(passes)