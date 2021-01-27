i = int(input())
j = int(input())
i2 = int(input())
j2 = int(input())

if (i2,j2) == (i-2,j-1) or (i2,j2) == (i-2,j+1) or (i2,j2) == (i+2,j-1) or (i2,j2) == (i+2,j+1):
    print("YES")
elif (i2,j2) == (i-1,j-2) or (i2,j2) == (i-1,j+2) or (i2,j2) == (i+1,j-2) or (i2,j2) == (i+1,j+2):
    print("YES")
else:
    print("NO")
