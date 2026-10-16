"""[LEARNING LOGS] Giraffe"""
n = int(input())
h = [int(input()) for _ in range(n)]

count = 0
for i in range(n):
    taller_left = not i or h[i] > h[i - 1]
    taller_right = i == n - 1 or h[i] > h[i + 1]
    if taller_left and taller_right:
        count += 1
print(count)