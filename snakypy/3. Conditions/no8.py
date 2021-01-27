col = int(input())
row = int(input())
colN = int(input())
rowN = int(input())

if abs(col - colN) == abs(row - rowN):
  print ("YES")
else:
  print ("NO")
