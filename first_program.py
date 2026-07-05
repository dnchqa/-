a, b, c, d = int(input()), int(input()), int(input()), int(input())  # 1 2 3 4 
minab = 0
mincd = 0
if a <= b:
    minab = a
else:
    minab = b
if c <= d:
    mincd = c
else: 
    mincd = d
if minab <= mincd:
    print(minab)
else:
    print:(mincd)
  
