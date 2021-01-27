x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

valid_move = abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1 and (x1, y1) != (x2, y2)
print("YES" if valid_move else "NO")
