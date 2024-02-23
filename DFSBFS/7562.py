# 백준 7562
from collections import deque

n = int(input())

dx=[2, 2, 1, 1, -2, -2, -1, -1]
dy=[1, -1, 2, -2, 1, -1, 2, -2]

def bfs(x, y, l, dest_x, dest_y):
  graph = [[0] * l for _ in range(l)]
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    if x == dest_x and y == dest_y :
      return graph[x][y]
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= l or ny < 0 or ny >= l:
        continue
      if graph[nx][ny] == 0:
        queue.append((nx, ny))
        graph[nx][ny] = graph[x][y] + 1
  
  return graph[dest_x][dest_y]

for i in range(n):
  l = int(input())
  x, y = map(int, input().split())
  dest_x, dest_y = map(int, input().split())
  print(bfs(x, y, l, dest_x, dest_y))