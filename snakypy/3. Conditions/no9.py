col = int(input())
row = int(input())
col2 = int(input())
row2 = int(input())

if col == col2 or row == row2 or abs(col - col2) == abs(row - row2):
  print ("YES")
else:
  print ("NO")
