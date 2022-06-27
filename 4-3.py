data=input()
row=int(data[1])
col=int(ord(data[0]))-int(ord('a'))+1

dirs=[(2,-1),(2,1),(-2,-1),(-2,1),(-1,2),(1,2),(-1,-2),(1,-2)]

count=0

for dir in dirs:
    next_row=row+dir[0]
    next_col=col+dir[1]

    if next_row>=1 and next_row<=8 and next_col>=1 and next_col<=8:
        count+=1

print(count)